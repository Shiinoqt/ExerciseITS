import { useState } from 'react'
import './App.css'
import Card from './Card.jsx'

function App() {
  const [isDarkMode, setIsDarkMode] = useState(false);
  
  const handleDarkMode = () => {
    setIsDarkMode(!isDarkMode);
    document.body.style.backgroundColor = isDarkMode ? 'white' : 'black';
  }
  
  return (
    <>
      <div className='cards-container'>
        <Card 
          title="Card 1"
          description="This is a card."
          isDarkMode={isDarkMode}/>
        <Card 
          title="Card 2"
          description="This is a card."
          isDarkMode={isDarkMode}/>
        <Card 
          title="Card 3"
          description="This is a card."
          isDarkMode={isDarkMode}/>
      </div>
      <button onClick={handleDarkMode}>
        {isDarkMode ? 'Light Mode' : 'Dark Mode'}
      </button>
    </>
  )
}

export default App