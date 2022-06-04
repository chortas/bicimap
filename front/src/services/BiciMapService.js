import { create } from "apisauce";

const api = create({
  baseURL: "http://192.168.0.164:5000/",
});

export const saveComparisons = (body) => api.post("/comparisons", body);
export const getPath = (originParam, destinationParam) =>
  api.get("/path", { origin: originParam, destination: destinationParam });
