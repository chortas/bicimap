import "./App.css";
import Config from "./screens/Config";
import React, { useState, useCallback } from "react";
import PrivateRoute from "./components/PrivateRoute";
import { BrowserRouter, Switch, Redirect } from "react-router-dom";
import PublicRoute from "./components/PublicRoute";

/*function App() {
  return <Config/>;
}*/

export default function App() {
  const [isConfigSent, setIsConfigSent] = useState(false);

  const configSuccess = useCallback(() => {
    setIsConfigSent(true);
  }, []);

  const onLogout = useCallback(() => {
    setIsConfigSent(false);
  }, []);

  return (
    <BrowserRouter>
      <Switch>
        <PublicRoute
          path="/config"
          component={() => Config({ configSuccess })}
          isConfigSent={isConfigSent}
        />
        <PrivateRoute
          key="/home"
          path="/home"
          component={<div />}
          //component={() => Home({ onLogout, itemSelected: route.component })}
          isConfigSent={isConfigSent}
        />
        <Redirect to="/home" />
      </Switch>
    </BrowserRouter>
  );
}
