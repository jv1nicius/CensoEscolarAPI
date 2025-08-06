import './App.css';
import BrazilMap from './components/BrazilMap';
import MapFilters from './components/MapFilters';
import React, { useState } from 'react';

function App() {
  const [selectedYear, setSelectedYear] = useState("2024");
  const [selectedState, setSelectedState] = useState("");
  const [dataState, setDataState] = useState({});

  return (
    <>
      <div style={{ margin: "1rem 2rem 1rem" }}>
        <div style={{ backgroundColor: "#f5f5f5", padding: "1rem 4rem 1rem", borderRadius: "25px", textAlign: "center", border: " 3px solid #a4a4a4" }}>
          <h1 style={{ backgroundColor: "#2c3e50", padding: "1rem 0rem 1rem", margin: "1rem 20rem 1rem", borderRadius: "25px", color: "#f39c12", border: " 3px solid"}}>Contagem do Censo Escolar</h1>
        </div>
        <div
          style={{
            display: "flex",
            justifyContent: "start",
            alignItems: "flex-start",
            gap: "2rem",
            margin: "1rem 0rem 1rem",
            padding: "1rem 4rem 1rem",
            backgroundColor: "#f5f5f5",
            border: " 3px solid #a4a4a4",
            borderRadius: "25px",
          }}
        >
          <BrazilMap
            selectedYear={selectedYear}
            selectedState={selectedState}
            setSelectedState={setSelectedState}
            setDataState={setDataState}
          />
          <MapFilters
            selectedYear={selectedYear}
            setSelectedYear={setSelectedYear}
            selectedState={selectedState}
            setSelectedState={setSelectedState}
            dataState={dataState}
          />
        </div>
      </div>

    </>
  );
}


export default App
