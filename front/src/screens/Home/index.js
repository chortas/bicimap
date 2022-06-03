import React from "react";
import {
  Typography,
  Container,
} from "@mui/material";
import useStyles from "./styles";
import DiscreteSlider from "../../components/DiscreteSlider";

export default function Home() {
  const classes = useStyles();

  return (
    <Container>
      <Typography variant="h3" gutterBottom component="div" className={classes.title}>
        Configuración
      </Typography>
      <DiscreteSlider
        onChange={(event) => {
          console.log(event.target.value);
        }}
        title="Comparación entre ir por bicisenda e ir por un camino que no esté empedrado"
        mark1="Prefiero ampliamente ir por un camino que no esté empedrado antes que ir por bicisenda"
        mark2="Prefiero ampliamente ir por bicisenda antes que ir por un camino que no esté empedrado"
      />
    </Container>
  );
}
