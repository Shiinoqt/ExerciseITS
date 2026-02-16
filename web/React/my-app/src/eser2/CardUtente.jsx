import React from 'react';

const CardUtente = (props) => {
    return (
        <div className="card">
            <img src={props.immagine} alt="Immagine Utente" />
            <h2>{props.nome}</h2>
            <p>{props.email}</p>
        </div>
    );
};

export default CardUtente;
