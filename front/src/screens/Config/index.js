import React, { useState, useCallback } from "react";
import { Typography, Container, Stack, Button } from "@mui/material";
import useStyles from "./styles";
import DiscreteSlider from "../../components/DiscreteSlider";
import CriteriaForm from "../../components/CriteriaForm";
import CustomDialog from "../../components/CustomDialog";
import CustomSnackBar from "../../components/CustomSnackBar";
import CustomAppBar from "../../components/CustomAppBar";
import { saveComparisons } from "../../services/BiciMapService";
import { getComparisonBody } from "../../utils/comparison";

export default function Config({ configSuccess }) {
  const classes = useStyles();

  const [cycleway, setCycleway] = useState(true);
  const [surface, setSurface] = useState(true);
  const [length, setLength] = useState(true);
  const [time, setTime] = useState(true);

  const [cyclewaySurface, setCyclewaySurface] = useState(1);
  const [cyclewayLength, setCyclewayLength] = useState(1);
  const [cyclewayTime, setCyclewayTime] = useState(1);
  const [surfaceLength, setSurfaceLength] = useState(1);
  const [surfaceTime, setSurfaceTime] = useState(1);
  const [lengthTime, setLengthTime] = useState(1);

  const [openSnackBar, setOpenSnackBar] = useState(false);

  const onClickComparisons = useCallback(async () => {
    const body = getComparisonBody(
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
    );
    const response = await saveComparisons(body);
    if (response.status !== 201) {
      setOpenSnackBar(true);
    } else {
      configSuccess();
    }
  }, [
    cycleway,
    surface,
    length,
    time,
    cyclewaySurface,
    cyclewayLength,
    cyclewayTime,
    surfaceLength,
    surfaceTime,
    lengthTime,
    configSuccess,
  ]);

  return (
    <Container>
      <CustomAppBar title="Configuración" />

      <Stack direction="row" spacing={1}>
        <Typography
          variant="h5"
          gutterBottom
          component="div"
          className={classes.title}
        >
          Criterios a tener en cuenta
        </Typography>
        <CustomDialog content="Se busca seleccionar qué criterios tener en cuenta para calcular un camino." />
      </Stack>
      <CriteriaForm
        setCycleway={setCycleway}
        setSurface={setSurface}
        setLength={setLength}
        setTime={setTime}
      />
      <Stack direction="row" spacing={1}>
        <Typography
          variant="h5"
          gutterBottom
          component="div"
          className={classes.comparisons}
        >
          Comparaciones
        </Typography>
        <CustomDialog content="Se busca determinar la importancia de un criterio por sobre otro para poder encontrar el camino que más se ajuste a sus preferencias." />
      </Stack>
      {cycleway && surface ? (
        <DiscreteSlider
          onChange={setCyclewaySurface}
          title="Comparación entre ir por bicisenda e ir por un camino que no esté empedrado"
          mark1="Camino no empedrado"
          minValue="Prefiero ampliamente ir por un camino que no esté empedrado antes que ir por bicisenda"
          minIntervalValue="Prefiero ir por un camino que no esté empedrado antes que ir por bicisenda"
          mark2="Me da igual"
          neutralValue="Me da igual ir por bicisenda que ir por un camino no empedrado"
          maxIntervalValue="Prefiero ir por bicisenda antes que ir por un camino que no esté empedrado"
          maxValue="Prefiero ampliamente ir por bicisenda antes que ir por un camino que no esté empedrado"
          mark3="Bicisenda"
        />
      ) : (
        <div />
      )}
      {cycleway && length ? (
        <DiscreteSlider
          onChange={setCyclewayLength}
          title="Comparación entre ir por bicisenda e ir por un camino de menor distancia"
          mark1="Camino de menor distancia"
          minValue="Prefiero ampliamente ir por un camino de menor distancia antes que ir por bicisenda"
          minIntervalValue="Prefiero ir por un camino de menor distancia antes que ir por bicisenda"
          mark2="Me da igual"
          neutralValue="Me da igual ir por bicisenda que ir por un camino de menor distancia"
          maxIntervalValue="Prefiero ir por bicisenda antes que ir por un camino de menor distancia"
          maxValue="Prefiero ampliamente ir por bicisenda antes que ir por un camino de menor distancia"
          mark3="Bicisenda"
        />
      ) : (
        <div />
      )}
      {cycleway && time ? (
        <DiscreteSlider
          onChange={setCyclewayTime}
          title="Comparación entre ir por bicisenda e ir por un camino de menor tiempo de recorrido"
          mark1="Camino de menor tiempo de recorrido"
          minValue="Prefiero ampliamente ir por un camino de menor tiempo de recorrido antes que ir por bicisenda"
          minIntervalValue="Prefiero ir por un camino de menor tiempo de recorrido antes que ir por bicisenda"
          mark2="Me da igual"
          neutralValue="Me da igual ir por bicisenda que ir por un camino de menor tiempo de recorrido"
          maxIntervalValue="Prefiero ir por bicisenda antes que ir por un camino de menor tiempo de recorrido"
          maxValue="Prefiero ampliamente ir por bicisenda antes que ir por un camino de menor tiempo de recorrido"
          mark3="Bicisenda"
        />
      ) : (
        <div />
      )}
      {surface && length ? (
        <DiscreteSlider
          onChange={setSurfaceLength}
          title="Comparación entre ir por un camino que no esté empedrado e ir por un camino de menor distancia"
          mark1="Camino de menor distancia"
          minValue="Prefiero ampliamente ir por un camino de menor distancia antes que ir por un camino que no esté empedrado"
          minIntervalValue="Prefiero ir por un camino de menor distancia antes que ir por un camino que no esté empedrado"
          mark2="Me da igual"
          neutralValue="Me da igual ir por un camino que no esté empedrado que ir por un camino de menor distancia"
          maxIntervalValue="Prefiero ir por un camino que no esté empedrado antes que ir por un camino de menor distancia"
          maxValue="Prefiero ampliamente ir por un camino que no esté empedrado antes que ir por un camino de menor distancia"
          mark3="Camino que no esté empedrado"
        />
      ) : (
        <div />
      )}
      {surface && time ? (
        <DiscreteSlider
          onChange={setSurfaceTime}
          title="Comparación entre ir por un camino que no esté empedrado e ir por un camino de menor tiempo de recorrido"
          mark1="Camino de menor tiempo de recorrido"
          minValue="Prefiero ampliamente ir por un camino de menor tiempo de recorrido antes que ir por un camino que no esté empedrado"
          minIntervalValue="Prefiero ir por un camino de menor tiempo de recorrido antes que ir por un camino que no esté empedrado"
          mark2="Me da igual"
          neutralValue="Me da igual ir por un camino que no esté empedrado que ir por un camino de menor tiempo de recorrido"
          maxIntervalValue="Prefiero ir por un camino que no esté empedrado antes que ir por un camino de menor tiempo de recorrido"
          maxValue="Prefiero ampliamente ir por un camino que no esté empedrado antes que ir por un camino de menor tiempo de recorrido"
          mark3="Camino que no esté empedrado"
        />
      ) : (
        <div />
      )}
      {length && time ? (
        <DiscreteSlider
          onChange={setLengthTime}
          title="Comparación entre ir por un camino de menor distancia e ir por un camino de menor tiempo de recorrido"
          mark1="Camino de menor tiempo de recorrido"
          minValue="Prefiero ampliamente ir por un camino de menor tiempo de recorrido antes que ir por un camino de menor distancia"
          minIntervalValue="Prefiero ir por un camino de menor tiempo de recorrido antes que ir por un camino de menor distancia"
          mark2="Me da igual"
          neutralValue="Me da igual ir por un camino de menor distancia que ir por un camino de menor tiempo de recorrido"
          maxIntervalValue="Prefiero ir por un camino de menor distancia antes que ir por un camino de menor tiempo de recorrido"
          maxValue="Prefiero ampliamente ir por un camino de menor distancia antes que ir por un camino de menor tiempo de recorrido"
          mark3="Camino de menor distancia"
        />
      ) : (
        <div />
      )}
      <Button
        variant="outlined"
        onClick={onClickComparisons}
        className={classes.button}
      >
        Enviar
      </Button>
      <CustomSnackBar
        open={openSnackBar}
        setOpenSnackBar={setOpenSnackBar}
        errorMessage="Las comparaciones no son consistentes. Recomendación: revisar si se da un caso donde se dice que el criterio A es más importante que el B, el criterio A es menos importante que el C y el criterio B es más importante que el C"
        severity="error"
      />
    </Container>
  );
}
