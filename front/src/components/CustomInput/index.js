import React, { useState } from "react";
import { Stack, TextField, InputAdornment, IconButton, Box } from "@mui/material";
import DirectionsBikeIcon from "@mui/icons-material/DirectionsBike";
import AddIcon from "@mui/icons-material/Add";
import useStyles from "./styles";

export default function CustomInput({ idx, content, setProperty, onClick }) {
  const classes = useStyles();
  const [showButton, setShowButton] = useState(true);

  return (
    <Stack direction="row" spacing={1} className={classes.stack}>
      <Box>
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
          onChange={(event) => setProperty(event.target.value, idx)}
        />
      </Box>
      {showButton ? (
        <IconButton
          onClick={() => {
            onClick();
            setShowButton(false);
          }}
        >
          <AddIcon />
        </IconButton>
      ) : (
        <div />
      )}
    </Stack>
  );
}
