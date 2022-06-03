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

export default function DiscreteSlider({
  onChange,
  title,
  mark1,
  mark2,
  mark3,
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
          marks={marks(mark1, mark2, mark3)}
          min={-9}
          max={9}
          width={10}
        />
      </Box>
    </Container>
  );
}
