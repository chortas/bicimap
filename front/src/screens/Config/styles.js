import { makeStyles } from '@mui/styles';

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
