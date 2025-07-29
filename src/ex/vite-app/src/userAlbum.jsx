import { useEffect, useState } from "react";

const urlUsers = "https://jsonplaceholder.typicode.com/users";
//const urlAlbums="https://jsonplaceholder.typicode.com/albums";
//const urlPhotos="https://jsonplaceholder.typicode.com/photos";
const UserAlbums = () => {
  const [users, setUsers] = useState([]);
  const [userSelected, setUserSelected] = useState(0);
  const [albums, setAlbums] = useState([]);

  // Con questo useEffect si caricano gli utenti al caricamento del componente
  const getUsers = async () => {
    try {
      const response = await fetch(urlUsers);
      const result = await response.json();
      setUsers(result);
    } catch (error) {
      console.error("Errore nel recupero degli utenti:", error);
    }
  };

  useEffect(() => {
    getUsers();
  }, []);

  // Con questo useEffect si caricano gli albums dell'utente selezionato
  const getAlbums = async (userId) => {
    if (!userId) return; // Se non c'è un utente selezionato
    const urlAlbums = `https://jsonplaceholder.typicode.com/albums?userId=${userId}`;
    try {
      const response = await fetch(urlAlbums);
      const result = await response.json();
      setAlbums(result);
    } catch (error) {
      console.error("Errore nel recupero degli albums:", error);
    }
  };

  return (
    <div className="container">
      <h1>Gestione albums photos</h1>
      <div className="row">
        <div className="col-6">
          <select
            className="form-select"
            value={userSelected}
            onChange={(e) => {
              setUserSelected(e.target.value);
            }}
          >
            <option value="">Seleziona utente</option>
            {users.map((u) => {
              return (
                <option key={u.id} value={u.id}>
                  {u.name}
                </option>
              );
            })}
          </select>
        </div>
        <div className="col-6">{userSelected}</div>
            <select className="form-select">
                <option value="">Seleziona album</option>
                {/* Qui andranno gli albums dell'utente selezionato */}
            </select>
      </div>
      <div className="row">
        <div className="col-12"></div>
      </div>
    </div>
  );
};

export default UserAlbums;
