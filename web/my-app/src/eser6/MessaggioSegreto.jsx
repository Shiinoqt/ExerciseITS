import React from 'react';

function MessaggioSegreto() {
    const [show, setShow] = React.useState(false);

    function toggleShow() {
        setShow(!show);
    }

    return (
        <div>
            <button onClick={toggleShow}>
                {show ? 'Nascondi' : 'Mostra'} messaggio segreto
            </button>
            {show && <p>Questo è un messaggio segreto!</p>}
        </div>
    );
}

export default MessaggioSegreto;