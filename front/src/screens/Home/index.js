import React, { useState, useCallback } from "react";
import { Container, Button, Box, CircularProgress } from "@mui/material";
import CustomInput from "../../components/CustomInput";
import { getPaths } from "../../services/BiciMapService";
import CustomSnackBar from "../../components/CustomSnackBar";
import useStyles from "./styles";
import CustomAppBar from "../../components/CustomAppBar";

export default function Home() {
  const classes = useStyles();

  const [origin, setOrigin] = useState("");
  const [destination, setDestination] = useState("");
  const [openSnackBar, setOpenSnackBar] = useState(false);
  const [contentToRender, setContentToRender] = useState("");
  const [idxPath, setIdxPath] = useState(0);
  const [paths, setPaths] = useState([]);

  const [directionAsked, setDirectionAsked] = useState(false);
  const [loadingPath, setLoadingPath] = useState(false);

  const onClickPath = useCallback(async () => {
    setLoadingPath(true);
    const response = await getPaths(origin, destination);
    if (response.status !== 200) {
      setOpenSnackBar(true);
    } else {
      setPaths(response.data["paths"]);
      setContentToRender(response.data["paths"][idxPath]);
      setDirectionAsked(true);
      setIdxPath(1);
    }
    setLoadingPath(false);
  }, [origin, destination, idxPath]);

  const onClickOtherPath = useCallback(async () => {
    setContentToRender(paths[idxPath]);
    const newIdxPath = (idxPath === 1 ? 0 : 1);
    console.log(newIdxPath);
    setIdxPath(newIdxPath);
  }, [paths, idxPath]);

  return (
    <Container className={classes.container}>
      <CustomAppBar title="BiciMap" />
      <CustomInput content="Dirección de salida" setProperty={setOrigin} />
      <CustomInput
        content="Dirección de llegada"
        setProperty={setDestination}
      />
      <Box m={3} pt={1}>
        {loadingPath ? (
          <CircularProgress
            size={30}
            className={classes.circularProgress}
          />
        ) : (
          <Button
            variant="outlined"
            onClick={onClickPath}
            className={classes.button}
          >
            Obtener camino
          </Button>
        )}
      </Box>
      <CustomSnackBar
        open={openSnackBar}
        setOpenSnackBar={setOpenSnackBar}
        errorMessage="El formato de las direcciones no es válido. Revisar si la calle existe y escribirla con el formato <Nombre de calle, altura>"
        severity="error"
      />
      {directionAsked ? (
        <div
          style={{ height: "600px", width: "1000px", paddingLeft: "25px" }}
          dangerouslySetInnerHTML={{ __html: contentToRender }}
        />
      ) : (
        <div />
      )}
      {directionAsked ? (
        <Box m={3} pt={1}>
          <Button
            variant="outlined"
            onClick={onClickOtherPath}
            className={classes.button}
          >
            Obtener otro camino
          </Button>
        </Box>
      ) : (
        <div />
      )}
    </Container>
  );
}
