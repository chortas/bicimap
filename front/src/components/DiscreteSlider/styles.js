import { makeStyles } from "@mui/styles";

const useStyles = makeStyles((theme) => ({
  title: {
    marginTop: theme.spacing(10),
    marginBottom: theme.spacing(5),
  },
  container: {
    marginTop: theme.spacing(1),
    paddingLeft: "5px",
    marginLeft: "10px",
    width: "15px",
    height: "15px",
    marginBottom: theme.spacing(15),
  },
  slider: {
    "&.MuiSlider-root": {
      color: "#4db6ac",
    },
  },
}));

export default useStyles;
