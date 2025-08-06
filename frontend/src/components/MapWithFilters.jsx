// components/MapWithFilters.jsx
import React from "react";
import BrazilMap from "./BrazilMap";
import MapFilters from "./MapFilters";

const MapWithFilters = () => {
    return (
        <div
            style={{
                display: "flex",
                justifyContent: "end",
                alignItems: "flex-start",
                gap: "2rem",
                padding: "2rem",
                backgroundColor: "#000000",
            }}
        >
            <MapFilters />
            <BrazilMap />
        </div>
    );
};

export default MapWithFilters;