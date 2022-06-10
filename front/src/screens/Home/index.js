import React, { useState, useCallback } from "react";
import { Button, Box, CircularProgress, IconButton } from "@mui/material";
import CustomInput from "../../components/CustomInput";
import { getPaths } from "../../services/BiciMapService";
import CustomSnackBar from "../../components/CustomSnackBar";
import useStyles from "./styles";
import CustomAppBar from "../../components/CustomAppBar";
import ArrowBackIosNewIcon from "@mui/icons-material/ArrowBackIosNew";

export default function Home({ setConfigSuccess }) {
  const classes = useStyles();

  const [points, setPoints] = useState([]);
  const [openSnackBar, setOpenSnackBar] = useState(false);
  const [contentToRender, setContentToRender] = useState("");
  const [idxPath, setIdxPath] = useState(0);
  const [paths, setPaths] = useState([]);
  const [directionAsked, setDirectionAsked] = useState(false);
  const [loadingPath, setLoadingPath] = useState(false);

  const [stops, setStops] = useState(0);

  const onClickPath = useCallback(async () => {
    setLoadingPath(true);
    const response = await getPaths(points);
    if (response.status !== 200) {
      setOpenSnackBar(true);
    } else {
      setPaths(response.data["paths"]);
      setContentToRender(response.data["paths"][idxPath]);
      setDirectionAsked(true);
    }
    setLoadingPath(false);
  }, [points, idxPath]);

  const onClickOtherPath = useCallback(async () => {
    console.log(idxPath);
    const newIdxPath = idxPath === 1 ? 0 : 1;
    setIdxPath(newIdxPath);
    setContentToRender(paths[newIdxPath]);
  }, [paths, idxPath]);

  const onClickStops = useCallback(async () => {
    setStops(stops + 1);
  }, [stops]);

  const onChangePoints = useCallback(
    async (newDestination, idx) => {
      var destinationCopy = [...points];
      destinationCopy[idx] = newDestination;
      setPoints(destinationCopy);
    },
    [points]
  );

  const onClickBack = useCallback(async () => {
    setConfigSuccess(false);
  }, [setConfigSuccess]);

  return (
    <Box className={classes.boxOut}>
      <CustomAppBar
        title="BiciMap"
        element={
          <IconButton style={{ color: "#ffff" }} onClick={onClickBack}>
            <ArrowBackIosNewIcon />
          </IconButton>
        }
      />
      <CustomInput
        key={0}
        idx={0}
        content="Dirección de salida"
        setProperty={onChangePoints}
        onClick={onClickStops}
      />

      {[...Array(stops).keys()].map((x) => (
        <CustomInput
          key={x + 1}
          idx={x + 1}
          content="Parada"
          setProperty={onChangePoints}
          onClick={onClickStops}
        />
      ))}

      <Box m={2} pt={1}>
        {loadingPath ? (
          <CircularProgress size={30} className={classes.circularProgress} />
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
          style={{ height: "600px", width: "1000px", paddingLeft: "20px" }}
          dangerouslySetInnerHTML={{ __html: contentToRender }}
        />
      ) : (
        <div />
      )}
      {directionAsked ? (
        <Box m={2} pt={1}>
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
    </Box>
  );
}
