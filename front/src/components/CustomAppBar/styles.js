import { makeStyles } from "@mui/styles";
import teal from "@mui/material/colors/teal";

const useStyles = makeStyles((theme) => ({
  button: {
    color: theme.palette.getContrastText(teal[300]),
    backgroundColor: "#4db6ac",
    "&:hover": {
      backgroundColor: teal[300],
    },
    marginTop: theme.spacing(3),
    marginBottom: theme.spacing(2),
    marginLeft: "10px",
  },
  appBar: {
    minHeight: 50
  },
}));

export default useStyles;
