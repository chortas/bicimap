import React, { useState, useCallback } from "react";
import { Container } from "@mui/material";
import CustomInput from "../../components/CustomInput";

export default function Home() {
  return (
    <Container>
      <CustomInput content="Dirección de salida" />
      <CustomInput content="Dirección de llegada" />
    </Container>
  );
}
