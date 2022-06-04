import React from 'react';
import { Route, Redirect } from 'react-router-dom';

function PrivateRoute({ component: Component, isConfigSent, ...rest }) {
  return (
    <Route
      {...rest}
      render={(props) =>
        isConfigSent ? (
          <Component {...props} />
        ) : (
          <Redirect
            to={{
              pathname: '/config',
              state: { from: props.location },
            }}
          />
        )
      }
    />
  );
}

export default PrivateRoute;
