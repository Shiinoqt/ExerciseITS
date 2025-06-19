const StampaNumeri = () => {
    const num = [1, 2, 3, 4, 5];
    return (
        <div>
            <h2>Numeri da 1 a 5:</h2>
            <ul>
                {num.map((numero) => (
                    <li><p>{numero}</p></li>
                ))}
            </ul>
        </div>
    )
}

export default StampaNumeri