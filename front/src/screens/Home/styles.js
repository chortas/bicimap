import { makeStyles } from "@mui/styles";
import teal from "@mui/material/colors/teal";

const useStyles = makeStyles((theme) => ({
  boxOut: {
    marginTop: theme.spacing(2),
    marginBottom: theme.spacing(2),
    marginLeft: theme.spacing(2),
    marginRight: theme.spacing(2),
    width: "500px",
  },
  map: {
    height: "100px",
    width: "500px",
  },
  button: {
    color: "#ffff !important",
    backgroundColor: "#4db6ac !important",
    borderColor: "#4db6ac !important",
    "&:hover": {
      backgroundColor: teal[300],
    },
  },
  circularProgress: {
    color:  "#4db6ac !important",
  },
}));

export default useStyles;
