import React, { useEffect, useState } from "react";
import { ComposableMap, Geographies, Geography } from "react-simple-maps";

const geoUrl = "https://raw.githubusercontent.com/codeforgermany/click_that_hood/main/public/data/brazil-states.geojson";

const siglaToId = {
    RO: "11",
    AC: "12",
    AM: "13",
    RR: "14",
    PA: "15",
    AP: "16",
    TO: "17",
    MA: "21",
    PI: "22",
    CE: "23",
    RN: "24",
    PB: "25",
    PE: "26",
    AL: "27",
    SE: "28",
    BA: "29",
    MG: "31",
    ES: "32",
    RJ: "33",
    SP: "35",
    PR: "41",
    SC: "42",
    RS: "43",
    MS: "50",
    MT: "51",
    GO: "52",
    DF: "53",
};

const BrazilMap = ({ selectedYear, selectedState, setSelectedState, setDataState }) => {
    const [highlightedState, setHighlightedState] = useState(null);
    const [matriculasData, setMatriculasData] = useState({});

    useEffect(() => {
        const fetchMatriculasData = async () => {
            const response = await fetch(`http://localhost:5000/censoescolar?nu_ano_censo=${selectedYear}`);
            const data = await response.json();
            setMatriculasData(data);
        };

        fetchMatriculasData();
    }, [selectedYear]);
    
    useEffect(() => {
        const fetchRegistrationStates = async () => {
            const response = await fetch(`http://localhost:5000/censoescolar?nu_ano_censo=${selectedYear}&co_uf=${selectedState}`);
            const data = await response.json();
            setDataState(data);
            console.log(data)
        };

        fetchRegistrationStates();

        if (selectedState !== highlightedState) {
            setHighlightedState(selectedState);
        }
    }, [selectedState, selectedYear]);

    const getFillColor = (stateId) => {
        const matriculasEntry = matriculasData[stateId];
        const matriculas = matriculasEntry ? matriculasEntry.total : null;

        if (matriculas != null) {
            const values = Object.values(matriculasData).map(entry => entry.total);
            const maxMatriculas = Math.max(...values);
            const minMatriculas = Math.min(...values);

            if (maxMatriculas === minMatriculas) {
                return "rgb(200, 255, 200)";
            }

            const percentage = (matriculas - minMatriculas) / (maxMatriculas - minMatriculas);

            const red = Math.floor(200 - percentage * 150);
            const green = Math.floor(255 - percentage * 100);
            const blue = Math.floor(200 - percentage * 200); 

            return `rgb(${red}, ${green}, ${blue})`;
        }

        return "#E0E0E0";
    };



    return (
        <div style={{ width: "100%", maxWidth: "650px", backgroundColor: "#2c3e50", borderRadius: "25px", border: " 3px solid #f39c12" }}>
            <ComposableMap
                projection="geoMercator"
                width={510}
                height={510}
                projectionConfig={{ center: [-54, -15], scale: 700 }}
                style={{
                    width: "100%",
                    height: "auto",
                }}
            >
                <Geographies geography={geoUrl}>
                    {({ geographies }) =>
                        geographies.map((geo) => {
                            const sigla = geo.properties.sigla;
                            const id_uf = siglaToId[sigla];
                            const isSelected = selectedState === id_uf;

                            let fillColor;

                            if (selectedState) {
                                fillColor = isSelected ? "#56FF95" : "#D3D3D3";
                            } else {
                                fillColor = getFillColor(id_uf);
                            }
                            return (
                                <Geography
                                    key={geo.rsmKey}
                                    geography={geo}
                                    fill={fillColor}
                                    stroke="#333"
                                    style={{
                                        default: { outline: "none", cursor: "pointer" },
                                        hover: { fill: "#56FF95", outline: "none" },
                                        pressed: { fill: "#0d7f37ff", outline: "none" },
                                    }}
                                    onClick={() => setSelectedState(id_uf)}
                                />
                            );
                        })
                    }
                </Geographies>
            </ComposableMap>
        </div>
    );
};

export default BrazilMap;
