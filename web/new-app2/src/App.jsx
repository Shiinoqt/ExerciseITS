import { useState } from 'react'
import './App.css'
import CardPosts from './cardPosts.jsx'
import ChangeColor from './ChangeColor.jsx'
import Echoinput from './Echoinput.jsx'
import PizzaSelector from './PizzaSelector.jsx'
import SelectCarM from './SelectCarM.jsx'
import PlateProp from './PlateProp.jsx'
import PostsDisplay from './PostsDIsplay.jsx'

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
        <ChangeColor />
        <Echoinput />
        <PizzaSelector />
        <SelectCarM />
        <PlateProp />
        <PostsDisplay />
      </div>
    </>
  )
}




export default App
