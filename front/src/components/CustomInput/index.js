import React from "react";
import { Container, TextField, InputAdornment } from "@mui/material";
import DirectionsBikeIcon from "@mui/icons-material/DirectionsBike";
import useStyles from "./styles";

export default function CustomInput({ content }) {
  const classes = useStyles();

  return (
    <Container className={classes.container}>
      <TextField
        className={classes.textField}
        label={content}
        InputProps={{
          startAdornment: (
            <InputAdornment position="start">
              <DirectionsBikeIcon />
            </InputAdornment>
          ),
        }}
        variant="standard"
        fullWidth
      />
    </Container>
  );
}
