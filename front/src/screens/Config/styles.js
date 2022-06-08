import { makeStyles } from '@mui/styles';
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
    width: "500px",
  },
}));

export default useStyles;
