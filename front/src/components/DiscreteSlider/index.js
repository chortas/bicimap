import * as React from "react";
import { Box, Slider, Typography, Container } from "@mui/material";
import useStyles from "./styles";

function marks(mark1, mark2, mark3) {
  return [
    {
      value: -9,
      label: mark1,
    },
    {
      value: 1,
      label: mark2,
    },
    {
      value: 9,
      label: mark3,
    },
  ];
}

function renderToolTip(
  value,
  minValue,
  minIntervalValue,
  neutralValue,
  maxIntervalValue,
  maxValue
) {
  if (value === -9) {
    return minValue;
  }
  if (value < 1 && value > -9) {
    return minIntervalValue;
  }
  if (value === 1) {
    return neutralValue;
  }
  if (value > 1 && value < 9) {
    return maxIntervalValue;
  }
  return maxValue;
}

export default function DiscreteSlider({
  onChange,
  title,
  mark1,
  mark2,
  mark3,
  minValue,
  minIntervalValue,
  neutralValue,
  maxIntervalValue,
  maxValue,
}) {
  const classes = useStyles();

  return (
    <Container className={classes.container}>
      <Typography
        variant="h6"
        gutterBottom
        component="div"
        className={classes.title}
      >
        {title}
      </Typography>
      <Box>
        <Slider
          valueLabelDisplay="auto"
          valueLabelFormat={(value) => {
            return (
              <div style={{ textAlign: "center" }}>
                {renderToolTip(
                  value,
                  minValue,
                  minIntervalValue,
                  neutralValue,
                  maxIntervalValue,
                  maxValue
                )}
              </div>
            );
          }}
          track={false}
          defaultValue={1}
          onChange={(event) =>
            onChange(
              event.target.value > 0
                ? event.target.value
                : 1 / Math.abs(event.target.value)
            )
          }
          step={1}
          marks={marks(mark1, mark2, mark3)}
          min={-9}
          max={9}
          width={10}
        />
      </Box>
    </Container>
  );
}
