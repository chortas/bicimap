import React, { useState, useCallback } from "react";
import { Container, Button } from "@mui/material";
import CustomInput from "../../components/CustomInput";
import { getPath } from "../../services/BiciMapService";
import CustomSnackBar from "../../components/CustomSnackBar";
import useStyles from "./styles";

export default function Home() {
  const classes = useStyles();

  const [origin, setOrigin] = useState("");
  const [destination, setDestination] = useState("");
  const [openSnackBar, setOpenSnackBar] = useState(false);

  const onClickPath = useCallback(async () => {
    const response = await getPath(origin, destination);
    if (response.status !== 200) {
      setOpenSnackBar(true);
    } else {
      console.log("Funciono");
    }
  }, [origin, destination]);

  return (
    <Container className={classes.container}>
      <CustomInput content="Dirección de salida" setProperty={setOrigin} />
      <CustomInput content="Dirección de llegada" setProperty={setDestination} />
      <Button variant="outlined" onClick={onClickPath}>
        Obtener camino
      </Button>
      <CustomSnackBar
        open={openSnackBar}
        setOpenSnackBar={setOpenSnackBar}
        errorMessage="El formato de las direcciones no es válido. Revisar si la calle existe y escribirla con el formato <Nombre de calle, altura>"
        severity="error"
      />
    </Container>
  );
}
