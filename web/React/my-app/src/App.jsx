import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Saluto from './Saluto'
import CardUtente from './eser2/CardUtente'
import MenuRistorante from './eser3/MenuRistorante'
import Termostato from './eser4/Termostato'
import CampoRicerca from './eser5/CampoRicerca'
import MessaggioSegreto from './eser6/MessaggioSegreto'
import AggiornaTitolo from './eser7/AggiornaTitolo'
import GalleriaFoto from './eser8/GalleriaFoto'
import ModuloContatti from './eser9/ModuloContatti'

function App() {

  return (
    <div>
    <Saluto />
    <CardUtente />
    <MenuRistorante />
    <Termostato />
    <CampoRicerca />
    <MessaggioSegreto />
    <AggiornaTitolo />
    <GalleriaFoto />
    <ModuloContatti />
    </div>
  )
}

export default App
