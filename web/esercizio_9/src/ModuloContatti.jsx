import React, { useState } from "react";

function ModuloContatti() {
  const [datiForm, setDatiForm] = useState({
    nome: "",
    email: "",
    messaggio: ""
  });

  function handleChange(e) {
    const { name, value } = e.target;
    setDatiForm(prev => ({ ...prev, [name]: value }));
  }

  function handleSubmit(e) {
    e.preventDefault();
    console.log(datiForm);
  }

  return (
    <form onSubmit={handleSubmit}>
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