import React, { useState } from 'react'

const Testeser = () => {
    const [color, setColor] = useState('black')

    const textStyle = { color }

    return (
        <div>
            <h1 style={textStyle}>Ciao Mondo!</h1>

            <div style={{ display: 'flex', gap: '8px', marginTop: '12px' }}>
                <button
                    onClick={() => setColor('red')}
                    style={{ backgroundColor: 'red', color: '#fff', padding: '8px 12px', border: 'none', borderRadius: 4 }}
                >
                    Rosso
                </button>

                <button
                    onClick={() => setColor('green')}
                    style={{ backgroundColor: 'green', color: '#fff', padding: '8px 12px', border: 'none', borderRadius: 4 }}
                >
                    Verde
                </button>

                <button
                    onClick={() => setColor('blue')}
                    style={{ backgroundColor: 'blue', color: '#fff', padding: '8px 12px', border: 'none', borderRadius: 4 }}
                >
                    Blu
                </button>
            </div>
        </div>
    )
}

export default Testeser