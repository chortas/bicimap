import { create } from "apisauce";

const api = create({
  baseURL: "https://bicimap.herokuapp.com/",
});

export const saveComparisons = (body) => api.post("/comparisons", body);
export const getPaths = (points) =>
  api.post("/path", { stops: points });
