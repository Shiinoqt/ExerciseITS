import React, { useState, useEffect } from 'react'
import './Card.css'

const Card = ({title, description, isDarkMode}) => {
  const [colorBg, setColorBg] = useState(isDarkMode ? '#000000ff' : '#ffffffff');
  
  useEffect(() => {
    setColorBg(isDarkMode ? '#000000ff' : '#ffffffff');
  }, [isDarkMode]);
  
  const handleCardClick = () => {
    setColorBg(colorBg === 'blue' ? (isDarkMode ? '#000000ff' : '#ffffffff') : 'blue');
  };
  
  return (
    <div 
      style={{backgroundColor: colorBg}} 
      onClick={handleCardClick} 
      className={isDarkMode ? 'card dark' : 'card'}
    >
      <img 
        style={{height: 180}} 
        src="https://placehold.co/362x180" 
        alt="Placeholder"
      />
      <div className='card-content'>
        <h2 style={{ color: isDarkMode ? 'white' : 'black' }}>{title}</h2>
        <p>{description}</p>
      </div>
    </div>
  )
}

export default Card