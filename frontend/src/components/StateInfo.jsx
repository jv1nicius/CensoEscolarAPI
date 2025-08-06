import React from "react";
import "../css/StateInfo.css";
/* API utilizada para pegar as bandeiras

    https://docs.apis.codante.io/bandeiras-dos-estados

*/

const bandeiras = {
    "11": "https://assets.codante.io/codante-apis/bandeiras-dos-estados/ro-rounded.svg",
    "12": "https://assets.codante.io/codante-apis/bandeiras-dos-estados/ac-rounded.svg",
    "13": "https://assets.codante.io/codante-apis/bandeiras-dos-estados/am-rounded.svg",
    "14": "https://assets.codante.io/codante-apis/bandeiras-dos-estados/rr-rounded.svg",
    "15": "https://assets.codante.io/codante-apis/bandeiras-dos-estados/pa-rounded.svg",
    "16": "https://assets.codante.io/codante-apis/bandeiras-dos-estados/ap-rounded.svg",
    "17": "https://assets.codante.io/codante-apis/bandeiras-dos-estados/to-rounded.svg",
    "21": "https://assets.codante.io/codante-apis/bandeiras-dos-estados/ma-rounded.svg",
    "22": "https://assets.codante.io/codante-apis/bandeiras-dos-estados/pi-rounded.svg",
    "23": "https://assets.codante.io/codante-apis/bandeiras-dos-estados/ce-rounded.svg",
    "24": "https://assets.codante.io/codante-apis/bandeiras-dos-estados/rn-rounded.svg",
    "25": "https://assets.codante.io/codante-apis/bandeiras-dos-estados/pb-rounded.svg",
    "26": "https://assets.codante.io/codante-apis/bandeiras-dos-estados/pe-rounded.svg",
    "27": "https://assets.codante.io/codante-apis/bandeiras-dos-estados/al-rounded.svg",
    "28": "https://assets.codante.io/codante-apis/bandeiras-dos-estados/se-rounded.svg",
    "29": "https://assets.codante.io/codante-apis/bandeiras-dos-estados/ba-rounded.svg",
    "31": "https://assets.codante.io/codante-apis/bandeiras-dos-estados/mg-rounded.svg",
    "32": "https://assets.codante.io/codante-apis/bandeiras-dos-estados/es-rounded.svg",
    "33": "https://assets.codante.io/codante-apis/bandeiras-dos-estados/rj-rounded.svg",
    "35": "https://assets.codante.io/codante-apis/bandeiras-dos-estados/sp-rounded.svg",
    "41": "https://assets.codante.io/codante-apis/bandeiras-dos-estados/pr-rounded.svg",
    "42": "https://assets.codante.io/codante-apis/bandeiras-dos-estados/sc-rounded.svg",
    "43": "https://assets.codante.io/codante-apis/bandeiras-dos-estados/rs-rounded.svg",
    "50": "https://assets.codante.io/codante-apis/bandeiras-dos-estados/ms-rounded.svg",
    "51": "https://assets.codante.io/codante-apis/bandeiras-dos-estados/mt-rounded.svg",
    "52": "https://assets.codante.io/codante-apis/bandeiras-dos-estados/go-rounded.svg",
    "53": "https://assets.codante.io/codante-apis/bandeiras-dos-estados/df-rounded.svg"
}

const StateInfo = ({ selectedYear, selectedState, states, dataState }) => {
    const nomeDoEstado = states.find((state) => state.idUf == selectedState)?.nomeUf;

    if (!selectedState) return null;

    const dados = dataState[selectedState] || {};

    return (
        <>
            <p>Matrículas</p>
            <div className="state-info-card">
                <div className="state-info-header">
                    <img src={bandeiras[selectedState]} alt={`Bandeira de ${nomeDoEstado}`} />
                    <div className="state-info-title">
                        <h2>{nomeDoEstado} - {selectedYear}</h2>
                    </div>
                </div>

                <div className="info-grid">
                    <div><strong>Educação Básica:</strong> {dados.bas ?? "Carregando..."}</div>
                    <div><strong>Educação Infantil:</strong> {dados.inf ?? "Carregando..."}</div>
                    <div><strong>Ensino Fundamental:</strong> {dados.fund ?? "Carregando..."}</div>
                    <div><strong>Ensino Médio:</strong> {dados.med ?? "Carregando..."}</div>
                    <div><strong>Educação Profissional:</strong> {dados.prof ?? "Carregando..."}</div>
                    <div><strong>Educação Especial:</strong> {dados.esp ?? "Carregando..."}</div>
                    <div><strong>Educação de Jovens e Adultos:</strong> {dados.eja ?? "Carregando..."}</div>
                    <div className="total"><strong>Total:</strong> {dados.total ?? "Carregando..."}</div>
                </div>
            </div>
        </>
    );
};

export default StateInfo;
