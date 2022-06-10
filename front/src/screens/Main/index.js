import React, { useState } from "react";
import Config from "../Config";
import Home from "../Home";

export default function Main() {
  const [configSuccess, setConfigSuccess] = useState(false);

  return configSuccess ? (
    <Home />
  ) : (
    <Config setConfigSuccess={setConfigSuccess} />
  );
}
