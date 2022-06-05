import { makeStyles } from "@mui/styles";
import teal from "@mui/material/colors/teal";

const useStyles = makeStyles((theme) => ({
  container: {
    marginTop: theme.spacing(2),
    marginBottom: theme.spacing(2),
    marginLeft: theme.spacing(2),
    marginRight: theme.spacing(2),
    width: "500px",
  },
  map: {
    "height": "100px",
    "width": "500px",
  },
  button: {
    color: "#ffff",
    backgroundColor: "#4db6ac",
    borderColor: "#4db6ac",
    "&:hover": {
      backgroundColor: teal[300],
    },
  },
}));

export default useStyles;