import * as React from "react";
import FormGroup from "@mui/material/FormGroup";
import FormControlLabel from "@mui/material/FormControlLabel";
import Checkbox from "@mui/material/Checkbox";
import useStyles from "./styles";

export default function CriteriaForm({
  setCycleway,
  setSurface,
  setLength,
  setTime,
}) {
  const classes = useStyles();

  return (
    <FormGroup className={classes.form}>
      <FormControlLabel
        control={
          <Checkbox
            defaultChecked
            onChange={(event) => setCycleway(event.target.checked)}
          />
        }
        label="Bicisenda"
      />
      <FormControlLabel
        control={
          <Checkbox
            defaultChecked
            onChange={(event) => setSurface(event.target.checked)}
          />
        }
        label="Camino no empedrado"
      />
      <FormControlLabel
        control={
          <Checkbox
            defaultChecked
            onChange={(event) => setLength(event.target.checked)}
          />
        }
        label="Camino con menor distancia"
      />
      <FormControlLabel
        control={
          <Checkbox
            defaultChecked
            onChange={(event) => setTime(event.target.checked)}
          />
        }
        label="Camino con menor tiempo de recorrido"
      />
    </FormGroup>
  );
}
