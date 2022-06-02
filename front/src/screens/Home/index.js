import React from "react";
import {
  Avatar,
  Button,
  CssBaseline,
  TextField,
  Typography,
  Container,
} from "@mui/material";
import useStyles from "./styles";
import DiscreteSlider from "../../components/DiscreteSlider";

export default function Home() {
  const classes = useStyles();

  return (
    <Container>
      <CssBaseline />
      <div className={classes.paper}>
        <DiscreteSlider
          onChange={(event) => {
            console.log(event.target.value);
          }}
          criteria1="Bicisenda"
          criteria2="Camino empedrado"
        />
      </div>
    </Container>
  );
}
