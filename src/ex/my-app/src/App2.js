import React from 'react';
import './App.css';
import { anagrafica } from './dati/dati';
import StampaNumeri from './printNumbers';
import Tabellina from './tabellina';
import CambiaNome from './cambianome';

function getDate() {
  return new Date().toLocaleDateString() + " " + new Date().toLocaleTimeString();
}

function App() {
  return (
    <div className="App">
      <h1>Benvenuti in React!</h1>
      {
        anagrafica.map((persona) => {
          return (
            <div key={persona.id}>
              <h2>{persona.nome} {persona.cognome}</h2>
            </div>
          );
        })
      }

      <header className="App-header">
        <Componente1/>
        <img src="https://www.its-ictacademy.com/wp-content/uploads/2023/12/Logo_ITS_Academy_bianco.png" className="App-logo" alt="logo" />
        <h2>
          {
            getDate()
          }
        </h2>
        <StampaNumeri />
        <Tabellina n={2} />
        <p>learn how to sybau!</p>
        <CambiaNome/>
          
      </header>
    </div>
  );
}

export default App;
