import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import CardUtente from './CardUtente'

function App() {
  return (
    <CardUtente nome="Mario Rossi" email="okdwok" immagine= "https:placehold.co/300x300" />
  )
}

export default App
