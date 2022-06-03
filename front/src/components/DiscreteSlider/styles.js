import { makeStyles } from "@mui/styles";

const useStyles = makeStyles((theme) => ({
  title: {
    marginTop: theme.spacing(10),
    marginBottom: theme.spacing(5),
  },
  container: {
    marginTop: theme.spacing(2),
    paddingLeft: "5px",
    marginLeft: "10px",
    width: "30px",
    height: "30px",
    marginBottom: theme.spacing(20)
  },
}));

export default useStyles;
