import { useState } from 'react'
import './App.css'
import CardPosts from './cardPosts.jsx'
import Testeser from './Testeser.jsx'
import Echoinput from './Echoinput.jsx'
import PizzaSelector from './PizzaSelector.jsx'

export function App() {
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
        <Testeser />
        <Echoinput />
        <PizzaSelector />
      </div>
    </>
  )
}




export default App
