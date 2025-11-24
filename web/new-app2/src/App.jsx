import { useState } from 'react'
import './App.css'
import CardPosts from './cardPosts.jsx'

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
        <CardPosts />
      </div>
    </>
  )
}

export default App
