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
  }
}));

export default useStyles;