import React from "react";
import { AppBar, Toolbar, Typography, Box, IconButton } from "@mui/material";
import ArrowBackIosIcon from "@mui/icons-material/ArrowBackIos";
import useStyles from "./styles";

export default function CustomAppBar() {
  const classes = useStyles();

  return (
    <Box m={8} pt={1}>
      <AppBar position="fixed" className={classes.appBar}>
        <Toolbar>
          <div>
            <Typography variant="h6" noWrap style={{ color: "#ffffff" }}>
              BiciMap
            </Typography>
          </div>
          <div>
            <IconButton className={classes.button}>
              <ArrowBackIosIcon style={{ color: "#ffffff" }} />
            </IconButton>
          </div>
        </Toolbar>
      </AppBar>
    </Box>
  );
}
