import React, { useState, useEffect } from 'react'
import TodoList from './TodoList';
import TodoForm from './TodoForm';

const API_URL = 'http://localhost:4000/tasks';

const TodoApp = () => {
  const [tasks, setTasks] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const getTasks = async () => {
    try {
      setLoading(true); // Aggiungi questo
      setError(null); // Reset errore
      const response = await fetch(API_URL);
      if (!response.ok) throw new Error("Errore nella fetch");
      const data = await response.json();
      setTasks(data);
    } catch (err) {
      setError(err.message); // Usa err.message invece di err
    } finally {
      setLoading(false);
    }
  };

  const addTask = async (text) => {
    try {
      const response = await fetch(API_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text, completed: false }),
      });
      if (!response.ok) throw new Error("Errore nell'aggiunta del task");
      getTasks();
    } catch (err) {
      setError(err.message);
    }
  };

  const deleteTask = async (id) => {
    try {
      const response = await fetch(`${API_URL}/${id}`, { method: "DELETE" });
      if (!response.ok) throw new Error("Errore nell'eliminazione del task");
      getTasks();
    } catch (err) {
      setError(err.message);
    }
  };

  const toggleTask = async (id, completed) => {
    try {
      const response = await fetch(`${API_URL}/${id}`, {
        method: "PATCH",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ completed: !completed }),
      });
      if (!response.ok) throw new Error("Errore nell'aggiornamento del task");
      getTasks();
    } catch (err) {
      setError(err.message);
    }
  };

  const updateTask = async (id, text) => {
    try {
      const response = await fetch(`${API_URL}/${id}`, {
        method: "PATCH",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text }),
      });
      if (!response.ok) throw new Error("Errore nella modifica del task");
      getTasks();
    } catch (err) {
      setError(err.message);
    }
  };

  useEffect(() => {
    getTasks();
  }, []);

  return (
    <div className="container mt-5">
      <h1 className="text-center mb-4">📝 Todo App</h1>
      
      {error && (
        <div className="alert alert-danger alert-dismissible fade show" role="alert">
          <strong>Errore!</strong> {error}
          <button 
            type="button" 
            className="btn-close" 
            onClick={() => setError(null)}
          ></button>
        </div>
      )}

      <TodoForm onAddTask={addTask} />

      {loading ? (
        <div className="text-center my-5">
          <div className="spinner-border text-primary" role="status">
            <span className="visually-hidden">Caricamento...</span>
          </div>
          <p className="mt-3">Caricamento tasks...</p>
        </div>
      ) : (
        <TodoList
          tasks={tasks}
          onDeleteTask={deleteTask}
          onToggleTask={toggleTask}
          onUpdateTask={updateTask}
        />
      )}
    </div>
  );
};

export default TodoApp;