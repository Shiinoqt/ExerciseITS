import { useState } from "react";

const TodoForm = ({ onAddTask }) => {
  const [text, setText] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    
    // Controlla che il testo non sia vuoto
    if (text.trim()) {
      onAddTask(text); // Passa il task al componente genitore
      setText(""); // Resetta l'input
    }
  };

  return (
    <form className="d-flex mb-3" onSubmit={handleSubmit}>
      <input
        type="text"
        className="form-control me-2"
        value={text}
        onChange={(e) => setText(e.target.value)}
        placeholder="Inserisci un nuovo task..."
      />
      <button className="btn btn-primary" type="submit">
        Aggiungi task
      </button>
    </form>
  );
};

export default TodoForm;