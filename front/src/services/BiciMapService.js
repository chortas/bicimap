import { create } from 'apisauce';

const api = create({
  baseURL: "http://192.168.0.164:5000/",
});

export const saveComparisons = (body) => api.post('/comparisons', body);
