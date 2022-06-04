import React from 'react';
import { Route, Redirect } from 'react-router-dom';

function PublicRoute({ component: Component, isConfigSent, ...rest }) {
  return (
    <Route
      {...rest}
      render={(props) =>
        isConfigSent ? (
          <Redirect
            to={{
              pathname: '/home',
              state: { from: props.location },
            }}
          />
        ) : (
          <Component {...props} />
        )
      }
    />
  );
}

export default PublicRoute;
