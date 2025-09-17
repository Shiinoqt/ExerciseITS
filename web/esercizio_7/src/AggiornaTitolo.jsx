import React, { useState, useEffect } from "react";

function AggiornaTitolo() {
  const [nome, setNome] = useState("");

  useEffect(() => {
    if (nome === "") {
      document.title = "Benvenuto!";
    } else {
      document.title = `Ciao, ${nome}!`;
    }
  }, [nome]);

  return (
    <div>
      <input
        type="text"
        value={nome}
        onChange={e => setNome(e.target.value)}
      />
      <p>{nome}</p>
    </div>
  );
}

export default AggiornaTitolo;