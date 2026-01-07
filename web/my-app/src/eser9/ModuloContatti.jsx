import React, { useState } from "react";

const ModuloContatti = () => {
  const [datiForm, setDatiForm] = useState({
    nome: "",
    email: "",
    messaggio: ""
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setDatiForm({ ...datiForm, [name]: value });
  };

  // Questa è la funzione corretta per gestire il submit
  const handleSubmit = (e) => {
    e.preventDefault();
    console.log("Dati inviati:", datiForm);
  };  

  return (
    <form onSubmit={handleSubmit}> {/* Usa onSubmit qui */}
      <input
        type="text"
        name="nome"
        value={datiForm.nome}
        onChange={handleChange}
        placeholder="Nome"
      />
      <input
        type="email"
        name="email"
        value={datiForm.email}
        onChange={handleChange}
        placeholder="Email"
      />
      <textarea
        name="messaggio"
        value={datiForm.messaggio}
        onChange={handleChange}
        placeholder="Messaggio"
      />
      <button type="submit">Invia</button>
    </form>
  );
}

export default ModuloContatti;