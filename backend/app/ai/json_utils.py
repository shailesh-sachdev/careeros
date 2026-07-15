import json
import re


class AIJSONError(Exception):
    """Raised when no valid JSON can be extracted from an AI response."""
    pass


def parse_llm_json(response: str) -> dict:
    """
    Extract the LAST valid JSON object from an LLM response.

    Handles:
    - ```json ... ```
    - Multiple JSON objects
    - Extra explanations before/after JSON
    - Local model self-corrections

    Returns:
        dict

    Raises:
        AIJSONError
    """

    if not response:
        raise AIJSONError("Empty response from AI.")

    response = (
        response
        .replace("```json", "")
        .replace("```", "")
        .strip()
    )

    decoder = json.JSONDecoder()

    valid_objects = []

    index = 0

    while index < len(response):

        start = response.find("{", index)

        if start == -1:
            break

        try:

            obj, end = decoder.raw_decode(
                response[start:]
            )

            valid_objects.append(obj)

            index = start + end

        except json.JSONDecodeError:

            index = start + 1

    if not valid_objects:

        raise AIJSONError(
            f"No valid JSON found.\n\n{response}"
        )

    result = valid_objects[-1]

    # -----------------------------
    # Normalize common AI mistakes
    # -----------------------------

    if isinstance(result, dict):

        if (
            "details" in result
            and isinstance(result["details"], dict)
        ):
            result["details"] = result["details"].get(
                "description",
                "",
            )

    return result