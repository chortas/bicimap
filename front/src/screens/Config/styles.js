import { makeStyles } from "@mui/styles";
import teal from "@mui/material/colors/teal";

const useStyles = makeStyles((theme) => ({
  title: {
    marginTop: theme.spacing(3),
    marginBottom: theme.spacing(7),
  },
  comparisons: {
    marginTop: theme.spacing(1),
    marginBottom: theme.spacing(3),
  },
  button: {
    marginBottom: theme.spacing(3),
    color: "#ffff !important",
    backgroundColor: "#4db6ac !important",
    borderColor: "#4db6ac !important",
    "&:hover": {
      backgroundColor: teal[300],
    },
  },
  container: {
    marginTop: theme.spacing(2),
    marginBottom: theme.spacing(2),
    marginLeft: theme.spacing(2),
    marginRight: theme.spacing(2),
  },
  boxOut: {
    backgroundColor: "#f5f6f7",
    padding: "1rem",
  },
  boxIn1: {
    margin: "4px 8px",
    borderRadius: "16px",
    boxShadow: "rgb(0 0 0 / 10%) 0px 2px 12px 0px",
    padding: "12px",
    maxHeight: "220px"
  },
  boxIn2: {
    margin: "16px 8px",
    borderRadius: "16px",
    boxShadow: "rgb(0 0 0 / 10%) 0px 2px 12px 0px",
    padding: "12px",
    minWidth: "1400px"
  }
}));

export default useStyles;
