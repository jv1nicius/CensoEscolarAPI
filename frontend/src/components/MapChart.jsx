// BrazilMap.jsx
import React from "react";
import { ComposableMap, Geographies, Geography } from "react-simple-maps";

const geoUrl =
    "https://raw.githubusercontent.com/codeforgermany/click_that_hood/main/public/data/brazil-states.geojson";

const BrazilMap = () => {
    return (
        <ComposableMap projection="geoMercator" projectionConfig={{ scale: 600 }}>
            <Geographies geography={geoUrl}>
                {({ geographies }) =>
                    geographies.map((geo) => (
                        <Geography
                            key={geo.rsmKey}
                            geography={geo}
                            fill="#E0E0E0"
                            stroke="#333"
                            style={{
                                default: { outline: "none" },
                                hover: { fill: "#F53", outline: "none" },
                                pressed: { fill: "#E42", outline: "none" },
                            }}
                        />
                    ))
                }
            </Geographies>
        </ComposableMap>
    );
};

export default BrazilMap;
