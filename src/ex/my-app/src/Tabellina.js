import React from 'react'

const Tabellina = ({ n }) => {
    const numeri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
    return (
        <div>
            {numeri.map((numero) => (
                <p>{n} x {numero} = {n * numero}</p>
            ))}
        </div>
    )
}

export default Tabellina
