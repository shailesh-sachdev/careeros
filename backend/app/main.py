from fastapi import FastAPI

app = FastAPI(
    title="CareerOS API",
    version="1.0.0",
)


@app.get("/")
async def root():
    return {
        "message": "CareerOS API is running"
    }