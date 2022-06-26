import { create } from "apisauce";

const api = create({
  baseURL: "http://localhost:5000/"
});

export const saveComparisons = (body) => api.post("/comparisons", body);
export const getPaths = (points) =>
  api.post("/path", { stops: points });
