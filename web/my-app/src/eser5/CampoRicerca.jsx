import React, { useState } from 'react';

function CampoRicerca() {
    const [testo, setTesto] = React.useState('');

    function onChange(event) {
        setTesto(event.target.value);
    }

    return (
        <div>
            <input type="text" value={testo} onChange={onChange} />
            <p>Testo inserito: {testo}</p>
        </div>
    );
}

export default CampoRicerca;