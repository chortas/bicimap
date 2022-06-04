import React, { useState, useCallback } from "react";
import { Container, Button, Box } from "@mui/material";
import CustomInput from "../../components/CustomInput";
import { getPath } from "../../services/BiciMapService";
import CustomSnackBar from "../../components/CustomSnackBar";
import useStyles from "./styles";

export default function Home() {
  const classes = useStyles();

  const [origin, setOrigin] = useState("");
  const [destination, setDestination] = useState("");
  const [openSnackBar, setOpenSnackBar] = useState(false);
  const [contentToRender, setContentToRender] = useState("");

  const onClickPath = useCallback(async () => {
    const response = await getPath(origin, destination);
    if (response.status !== 200) {
      setOpenSnackBar(true);
    } else {
      setContentToRender(response.data);
      console.log(contentToRender);
    }
  }, [origin, destination, contentToRender]);

  return (
    <Container className={classes.container}>
      <CustomInput content="Dirección de salida" setProperty={setOrigin} />
      <CustomInput
        content="Dirección de llegada"
        setProperty={setDestination}
      />
      <Box m={3} pt={1}>
        <Button variant="outlined" onClick={onClickPath}>
          Obtener camino
        </Button>
      </Box>
      <CustomSnackBar
        open={openSnackBar}
        setOpenSnackBar={setOpenSnackBar}
        errorMessage="El formato de las direcciones no es válido. Revisar si la calle existe y escribirla con el formato <Nombre de calle, altura>"
        severity="error"
      />
      <div
        style={{ height: "1000px", width: "1000px", paddingLeft: "25px" }}
        dangerouslySetInnerHTML={{ __html: contentToRender }}
      />
    </Container>
  );
}
