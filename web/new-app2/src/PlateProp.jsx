import React, { useState } from 'react'

const PlateProp = () => {
  const [entries, setEntries] = useState([])  // Array to store all submissions
  const [owner, setOwner] = useState('')      // Current input value
  const [plate, setPlate] = useState('')      // Current input value
  
  function handleSubmit(event) {
    event.preventDefault()
    // Add new entry to the array
    setEntries([...entries, { owner, plate }])
    // Clear the input fields
    setOwner('')
    setPlate('')
    console.log('Submitted:', { owner, plate })
  }
  
  function handleInputChange(event) {
    const { id, value } = event.target
    if (id === 'owner') {
      setOwner(value)
    } else if (id === 'plate') {
      setPlate(value)
    }
  }   
  
  return (
    <div>
      <table>
        <thead>
          <tr>
            <th>Owner</th>
            <th>Plate</th>
          </tr>
        </thead>
        <tbody>
          {entries.map((entry, index) => (
            <tr key={index}>
              <td>{entry.owner}</td>
              <td>{entry.plate}</td>
            </tr>
          ))}
        </tbody>
      </table>
      
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="owner">Owner:</label>
          <input
            type="text"
            id="owner"
            value={owner}
            onChange={handleInputChange}
          />
        </div>
        <div>
          <label htmlFor="plate">Plate:</label>
          <input
            type="text"
            id="plate"
            value={plate}
            onChange={handleInputChange}
          />
        </div>
        <div>
          <button type="submit">Submit</button>
        </div>
      </form>
    </div>
  )
}

export default PlateProp