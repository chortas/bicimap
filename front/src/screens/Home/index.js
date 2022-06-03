import React, { useState } from "react";
import { Typography, Container } from "@mui/material";
import useStyles from "./styles";
import DiscreteSlider from "../../components/DiscreteSlider";
import CriteriaForm from "../../components/CriteriaForm";

export default function Home() {
  const classes = useStyles();

  const [cycleway, setCycleway] = useState(true);
  const [surface, setSurface] = useState(true);
  const [length, setLength] = useState(true);
  const [time, setTime] = useState(true);

  return (
    <Container>
      <Typography
        variant="h3"
        gutterBottom
        component="div"
        className={classes.title}
      >
        Configuración
      </Typography>
      <Typography
        variant="h5"
        gutterBottom
        component="div"
        className={classes.title}
      >
        Criterios a tener en cuenta
      </Typography>
      <CriteriaForm
        setCycleway={setCycleway}
        setSurface={setSurface}
        setLength={setLength}
        setTime={setTime}
      />
      <Typography
        variant="h5"
        gutterBottom
        component="div"
        className={classes.comparisons}
      >
        Comparaciones
      </Typography>
      {cycleway && surface ? (
        <DiscreteSlider
          onChange={(event) => {
            console.log(event.target.value);
          }}
          title="Comparación entre ir por bicisenda e ir por un camino que no esté empedrado"
          mark1="Prefiero ampliamente ir por un camino que no esté empedrado antes que ir por bicisenda"
          mark2="Me da igual ir por bicisenda que ir por un camino no empedrado"
          mark3="Prefiero ampliamente ir por bicisenda antes que ir por un camino que no esté empedrado"
        />
      ) : (
        <div />
      )}
      {cycleway && length ? (
        <DiscreteSlider
          onChange={(event) => {
            console.log(event.target.value);
          }}
          title="Comparación entre ir por bicisenda e ir por un camino de menor distancia"
          mark1="Prefiero ampliamente ir por un camino de menor distancia antes que ir por bicisenda"
          mark2="Me da igual ir por bicisenda que ir por un camino de menor distancia"
          mark3="Prefiero ampliamente ir por bicisenda antes que ir por un camino de menor distancia"
        />
      ) : (
        <div />
      )}
      {cycleway && time ? (
        <DiscreteSlider
          onChange={(event) => {
            console.log(event.target.value);
          }}
          title="Comparación entre ir por bicisenda e ir por un camino de menor tiempo de recorrido"
          mark1="Prefiero ampliamente ir por un camino de menor tiempo de recorrido antes que ir por bicisenda"
          mark2="Me da igual ir por bicisenda que ir por un camino de menor tiempo de recorrido"
          mark3="Prefiero ampliamente ir por bicisenda antes que ir por un camino de menor tiempo de recorrido"
        />
      ) : (
        <div />
      )}
      {surface && length ? (
        <DiscreteSlider
          onChange={(event) => {
            console.log(event.target.value);
          }}
          title="Comparación entre ir por un camino que no esté empedrado e ir por un camino de menor distancia"
          mark1="Prefiero ampliamente ir por un camino de menor distancia antes que ir por un camino que no esté empedrado"
          mark2="Me da igual ir por un camino que no esté empedrado que ir por un camino de menor distancia"
          mark3="Prefiero ampliamente ir por un camino que no esté empedrado antes que ir por un camino de menor distancia"
        />
      ) : (
        <div />
      )}
      {surface && time ? (
        <DiscreteSlider
          onChange={(event) => {
            console.log(event.target.value);
          }}
          title="Comparación entre ir por un camino que no esté empedrado e ir por un camino de menor tiempo de recorrido"
          mark1="Prefiero ampliamente ir por un camino de menor tiempo de recorrido antes que ir por un camino que no esté empedrado"
          mark2="Me da igual ir por un camino que no esté empedrado que ir por un camino de menor tiempo de recorrido"
          mark3="Prefiero ampliamente ir por un camino que no esté empedrado antes que ir por un camino de menor tiempo de recorrido"
        />
      ) : (
        <div />
      )}
      {length && time ? (
        <DiscreteSlider
          onChange={(event) => {
            console.log(event.target.value);
          }}
          title="Comparación entre ir por un camino de menor distancia e ir por un camino de menor tiempo de recorrido"
          mark1="Prefiero ampliamente ir por un camino de menor tiempo de recorrido antes que ir por un camino de menor distancia"
          mark2="Me da igual ir por un camino de menor distancia que ir por un camino de menor tiempo de recorrido"
          mark3="Prefiero ampliamente ir por un camino de menor distancia antes que ir por un camino de menor tiempo de recorrido"
        />
      ) : (
        <div />
      )}
    </Container>
  );
}
