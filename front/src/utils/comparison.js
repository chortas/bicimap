export const getComparisonBody = (
  cyclewaySurface,
  cyclewayLength,
  cyclewayTime,
  surfaceLength,
  surfaceTime,
  lengthTime,
  cycleway,
  surface,
  length,
  time
) => {
  var body = {};
  if (cycleway && surface) {
    body["cycleway,surface"] = cyclewaySurface;
  }
  if (cycleway && length) {
    body["cycleway,length"] = cyclewayLength;
  }
  if (cycleway && time) {
    body["cycleway,travel_time"] = cyclewayTime;
  }
  if (surface && length) {
    body["surface,length"] = surfaceLength;
  }
  if (surface && time) {
    body["surface,travel_time"] = surfaceTime;
  }
  if (length && time) {
    body["length,travel_time"] = lengthTime;
  }
  return body;
};
