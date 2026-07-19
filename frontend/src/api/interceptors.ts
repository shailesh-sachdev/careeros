import { api } from "./client";

export function registerInterceptors() {
  api.interceptors.request.use(
    (config) => {
      return config;
    },
    (error) => Promise.reject(error)
  );

  api.interceptors.response.use(
    (response) => response,
    (error) => Promise.reject(error)
  );
}