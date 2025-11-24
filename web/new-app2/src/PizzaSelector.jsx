import React, { useState } from 'react'

const PizzaSelector = () => {
    const pizzas = ['Margherita', 'Pepperoni', 'Hawaiian', 'Veggie', 'BBQ Chicken']

    const [selectedPizza, setSelectedPizza] = useState('')

    const handleSelectPizza = (selected) => {
        setSelectedPizza(selected)
    }


  return (
    <div>
        <h2>Choose Your Favorite Pizza</h2>
        <select onChange={(e) => handleSelectPizza(e.target.value)} value={selectedPizza || ''}>
            <option value="" disabled>Select a pizza</option>
            {pizzas.map((pizzaOption) => (
                <option key={pizzaOption} value={pizzaOption}>
                    {pizzaOption}
                </option>
            ))}
        </select>

        <p> {selectedPizza} </p>
    </div>
  )
}

export default PizzaSelector