import React, { useEffect , useState } from "react";
import StateInfo from "./StateInfo";


const MapFilters = ({ selectedYear, setSelectedYear, selectedState, setSelectedState, dataState }) => {
    const [states, setStates] = useState([]);
    const APIESTADOS = "http://localhost:5000/estados";

    useEffect(()=>{
        fetch(APIESTADOS)
        .then((res) => res.json())
        .then((data) => setStates(data))
        .catch((e) => console.log("Erro", e))
    }, []);

    return (
        <div
            style={{
                display: "flex",
                flexDirection: "column",
                justifyContent: "start",
                gap: "1rem",
                color: "#f39c12",
                backgroundColor: "#2c3e50",
                padding: "1rem",
                borderRadius: "25px",
                border: " 3px solid",
            }}
        >
            <label>Ano:</label>
            <select value={selectedYear} onChange={(e) => setSelectedYear(e.target.value)} style={{ width: "150px", padding: "0.5rem" }}>
                <option value="">Selecione</option>
                <option value="2023">2023</option>
                <option value="2024">2024</option>
            </select>
                

            <label>Estados:</label>
            <select value={selectedState} onChange={(e) => setSelectedState(e.target.value)} style={{ width: "150px", padding: "0.5rem" }}>
                <option value="">Selecione</option>
                {states.map((state) => (
                    <option key={state.idUf} value={state.idUf}>
                        {state.nomeUf}
                    </option>
                ))}
            </select>
            <StateInfo
                selectedYear={selectedYear}
                selectedState={selectedState}
                states={states}
                dataState={dataState}
            />
        </div>
    );
};

export default MapFilters;
