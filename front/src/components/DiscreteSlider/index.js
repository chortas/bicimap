import * as React from "react";
import { Box, Slider, Typography, Container, Stack } from "@mui/material";
import useStyles from "./styles";
import CustomDialog from "../CustomDialog";

function marks(criteria1, criteria2) {
  return [
    {
      value: -9,
      label: `${criteria1} es extremadamente menos importante que ${criteria2.toLowerCase()}`,
    },
    {
      value: 1,
      label: "Son igualmente importantes",
    },
    {
      value: 9,
      label: `${criteria1} es extremadamente menos importante que ${criteria2.toLowerCase()}`,
    },
  ];
}

export default function DiscreteSlider({ onChange, criteria1, criteria2 }) {
  const classes = useStyles();

  return (
    <Container className={classes.container}>
      <Stack direction="row" spacing={1}>
        <Typography
          variant="h6"
          gutterBottom
          component="div"
          className={classes.title}
        >
          Comparación entre {criteria1} y {criteria2}
        </Typography>
        <CustomDialog />
      </Stack>
      <Box sx={{ width: 600 }}>
        <Slider
          sx={{
            "& .MuiSlider-markLabel": {
              width: "200px",
              whiteSpace: "break-spaces",
            },
          }}
          track={false}
          defaultValue={1}
          onChange={onChange}
          step={1}
          marks={marks(criteria1, criteria2)}
          min={-9}
          max={9}
          width={10}
        />
      </Box>
    </Container>
  );
}
