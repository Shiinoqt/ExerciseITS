import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Saluto from './Saluto'
import CardUtente from './eser2/CardUtente'
import MenuRistorante from './eser3/MenuRistorante'
import Termostato from './eser4/Termostato'

function App() {

  return (
    <div>
    <Saluto />
    <CardUtente />
    <MenuRistorante />
    <Termostato />
    </div>
  )
}

export default App
