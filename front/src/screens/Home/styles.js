import { makeStyles } from "@mui/styles";

const useStyles = makeStyles((theme) => ({
  container: {
    marginTop: theme.spacing(2),
    marginBottom: theme.spacing(2),
    width: "500px",
  },
  map: {
    "height": "100px",
    "width": "500px",
  }
}));

export default useStyles;