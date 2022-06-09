import "./App.css";
import Config from "./screens/Config";
import Home from "./screens/Home";
import React, { useState, useCallback } from "react";
import PrivateRoute from "./components/PrivateRoute";
import { BrowserRouter, Switch, Redirect } from "react-router-dom";
import PublicRoute from "./components/PublicRoute";

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
          path="/bicimap"
          component={() => Config({ configSuccess })}
          isConfigSent={isConfigSent}
        />
        <PrivateRoute
          key="/bicimap/home"
          path="/bicimap/home"
          component={() => Home()}
          isConfigSent={isConfigSent}
        />
        <Redirect to="/bicimap/home" />
      </Switch>
    </BrowserRouter>
  );
}
