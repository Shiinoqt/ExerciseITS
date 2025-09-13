import React, { useState, useEffect } from "react";

const API_URL = "/api/users";

const UserCrud = () => {
  const [users, setUsers] = useState([]);
  const [formData, setFormData] = useState({
    id: "",
    nome: "",
    cognome: "",
    telefono: "",
    email: "",
  });
  const [isEditing, setIsEditing] = useState(false);

  const getUsers = async () => {
    try {
      const response = await fetch(API_URL);
      const data = await response.json();
      setUsers(data);
    } catch (error) {
      console.error("Error fetching users:", error);
    }
  };

  useEffect(() => {
    getUsers();
  }, []);

  const deleteUser = async (id) => {
    if (window.confirm("Sei sicuro di voler eliminare questo utente?")) {
      try {
        const response = await fetch(`${API_URL}/${id}`, {
          method: "DELETE",
        });
        if (response.ok) {
          setUsers((prevUsers) => prevUsers.filter((user) => user.id !== id));
        } else {
          console.error("Error deleting user:", response.statusText);
        }
      } catch (error) {
        console.error("Error deleting user:", error);
      }
    }
  };

  const editUser = (user) => {
    setFormData({
      id: user.id,
      nome: user.nome,
      cognome: user.cognome,
      telefono: user.telefono,
      email: user.email,
    });
    setIsEditing(true);
  };

  const cancelEdit = () => {
    setFormData({
      id: "",
      nome: "",
      cognome: "",
      telefono: "",
      email: "",
    });
    setIsEditing(false);
  };

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const method = formData.id ? "PUT" : "POST";
      const url = formData.id ? `${API_URL}/${formData.id}` : API_URL;

      const response = await fetch(url, {
        method: method,
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(formData),
      });

      if (response.ok) {
        const updatedUser = await response.json();
        if (method === "POST") {
          setUsers((prevUsers) => [...prevUsers, updatedUser]);
        } else {
          setUsers((prevUsers) =>
            prevUsers.map((user) =>
              user.id === updatedUser.id ? updatedUser : user
            )
          );
        }
        setFormData({
          id: "",
          nome: "",
          cognome: "",
          telefono: "",
          email: "",
        });
        setIsEditing(false);
      } else {
        console.error("Error saving user:", response.statusText);
      }
    } catch (error) {
      console.error("Error saving user:", error);
    }
  };

  return (
    <div className="col">
      <h1>Gestione Utenti</h1>

      <div>
        <h2>{isEditing ? "Modifica Utente" : "Aggiungi Nuovo Utente"}</h2>
        <div>
          <div>
            <div>
              <label htmlFor="nome">Nome *</label>
              <input
                type="text"
                id="nome"
                name="nome"
                value={formData.nome}
                onChange={handleInputChange}
                required
                placeholder="Inserisci il nome"
              />
            </div>
            <div>
              <label htmlFor="cognome">Cognome *</label>
              <input
                type="text"
                id="cognome"
                name="cognome"
                value={formData.cognome}
                onChange={handleInputChange}
                required
                placeholder="Inserisci il cognome"
              />
            </div>
            <div>
              <label htmlFor="telefono">Telefono</label>
              <input
                type="tel"
                id="telefono"
                name="telefono"
                value={formData.telefono}
                onChange={handleInputChange}
                placeholder="Inserisci il telefono"
              />
            </div>
            <div>
              <label htmlFor="email">Email *</label>
              <input
                type="email"
                id="email"
                name="email"
                value={formData.email}
                onChange={handleInputChange}
                required
                placeholder="Inserisci l'email"
              />
            </div>
          </div>
          <div>
            <button type="button" onClick={handleSubmit}>
              {isEditing ? "Aggiorna Utente" : "Aggiungi Utente"}
            </button>
            {isEditing && (
              <button type="button" onClick={cancelEdit}>
                Annulla
              </button>
            )}
          </div>
        </div>
      </div>

      <div>
        <div>
          <h2>Lista Utenti</h2>
        </div>
        <div>
          <table>
            <thead>
              <tr>
                <th>Nome</th>
                <th>Cognome</th>
                <th>Telefono</th>
                <th>Email</th>
                <th>Azioni</th>
              </tr>
            </thead>
            <tbody>
              {users.length === 0 ? (
                <tr>
                  <td colSpan="5">Nessun utente trovato</td>
                </tr>
              ) : (
                users.map((user) => (
                  <tr key={user.id}>
                    <td>{user.nome}</td>
                    <td>{user.cognome}</td>
                    <td>{user.telefone || "N/A"}</td>
                    <td>{user.email}</td>
                    <td>
                      <button onClick={() => editUser(user)}>Modifica</button>
                      <button onClick={() => deleteUser(user.id)}>
                        Elimina
                      </button>
                    </td>
                  </tr>
                ))
              )}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};

export default UserCrud;
