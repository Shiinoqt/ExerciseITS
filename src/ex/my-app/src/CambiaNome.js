import React from 'react';

const CambiaNome = () => {
    const [nome, setNome] = React.useState("Mario");
    const cambia = () => {
        if (nome === "Mario") {
            setNome("Luigi");
        }else {
            setNome("Mario");
        }
    };
    return (
        <div>
            {nome}
            <button onClick={cambia}>Cambia Nome</button>
        </div>
    );
}

export default CambiaNome;