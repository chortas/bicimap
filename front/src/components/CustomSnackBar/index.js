import React from 'react';
import { Snackbar } from '@mui/material';
import MuiAlert from '@mui/material/Alert';
import { func, bool, string } from 'prop-types';

export default function CustomSnackBar({ open, setOpenSnackBar, errorMessage, severity }) {
  const vertical = 'top';
  const horizontal = 'center';

  const handleClose = (event, reason) => {
    if (reason !== 'clickaway') {
      setOpenSnackBar(false);
    }
  };

  return (
    <Snackbar
      open={open}
      autoHideDuration={6000}
      onClose={handleClose}
      anchorOrigin={{ vertical, horizontal }}
      key={vertical + horizontal}
    >
      <MuiAlert elevation={10} variant="filled" onClose={handleClose} severity={severity}>
        {errorMessage}
      </MuiAlert>
    </Snackbar>
  );
}

CustomSnackBar.propTypes = {
  open: bool,
  setOpenSnackBar: func,
  errorMessage: string,
  severity: string,
};
