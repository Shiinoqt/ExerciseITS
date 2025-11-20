import { useState } from 'react'
import './App.css'

function App() {
  const [showMessage, setShowMessage] = useState(false)

  const onButtonClick = () => {
    if (!showMessage) {
      setShowMessage(true)
    }
    else {
      setShowMessage(false)
    }
  }

  return (
    <> 
      <div className="app-container">
        <button onClick={onButtonClick}>Click me</button>
        {showMessage && <p>Hello! You clicked the button.</p>}
      </div>
    </>
  )
}

export default App
