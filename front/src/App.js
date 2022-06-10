import "./App.css";
import Main from "./screens/Main";
import React from "react";
import { BrowserRouter, Switch } from "react-router-dom";
import PublicRoute from "./components/PublicRoute";

export default function App() {

  return (
    <BrowserRouter>
      <Switch>
        <PublicRoute
          path="/bicimap"
          component={() => Main()}
        />
      </Switch>
    </BrowserRouter>
  );
}
