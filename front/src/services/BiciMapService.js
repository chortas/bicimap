import { create } from "apisauce";

const api = create({
  //baseURL: "https://bicimap.herokuapp.com/",
  baseURL: "http://192.168.0.164:5000/"
});

export const saveComparisons = (body) => api.post("/comparisons", body);
export const getPaths = (points) =>
  api.post("/path", { stops: points });
