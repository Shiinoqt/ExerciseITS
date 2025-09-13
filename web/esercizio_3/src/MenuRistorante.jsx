import React from 'react';
import piatti from './piatti';

const MenuRistorante = () => {
    return (
        <div>
            <h1>Menu del Ristorante</h1>
            <ul>
                {piatti.map((piatto) => (
                    <li key={piatto.id}>
                        {piatto.nome} - {piatto.prezzo} €
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default MenuRistorante;