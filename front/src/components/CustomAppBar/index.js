import React from "react";
import {
  AppBar,
  Toolbar,
  Typography,
  Box,
  Stack,
} from "@mui/material";
import useStyles from "./styles";

export default function CustomAppBar({ title, element }) {
  const classes = useStyles();

  return (
    <Box m={5} pt={1}>
      <AppBar
        position="fixed"
        style={{ backgroundColor: "#4db6ac" }}
        className={classes.appBar}
      >
        <Toolbar>
          <Stack direction="row" spacing={1}>
            <Typography variant="h6" noWrap style={{ color: "#ffffff" }}>
              {title}
            </Typography>
            <Box m={2}>{element}</Box>
          </Stack>
        </Toolbar>
      </AppBar>
    </Box>
  );
}
