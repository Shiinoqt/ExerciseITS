import React, { useEffect, useState } from "react";
import './App.css'

const urlUsers = "https://jsonplaceholder.typicode.com/users";
const urlAlbums = "https://jsonplaceholder.typicode.com/albums";
const urlPhotos = "https://jsonplaceholder.typicode.com/photos";

const UserAlbums = () => {
  const [users, setUsers] = useState([]);
  const [userSelected, setUserSelected] = useState("");

  const [albums, setAlbums] = useState([]);
  const [albumSelected, setAlbumSelected] = useState("");

  const [photos, setPhotos] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const getUsers = async () => {
    try {
      setLoading(true);
      setError("");
      const response = await fetch(urlUsers);
      if (!response.ok) throw new Error("Failed to fetch users");
      const result = await response.json();
      setUsers(result);
    } catch (err) {
      setError("Error loading users: " + err.message);
      console.log(err);
    } finally {
      setLoading(false);
    }
  };

  const getAlbums = async () => {
    if (!userSelected) {
      setAlbums([]);
      setAlbumSelected("");
      setPhotos([]);
      return;
    }

    try {
      setLoading(true);
      setError("");
      const url = urlAlbums + `?userId=${userSelected}`;
      const response = await fetch(url);
      if (!response.ok) throw new Error("Failed to fetch albums");
      const result = await response.json();
      setAlbums(result);
      setAlbumSelected(""); // Reset album selection
      setPhotos([]); // Reset photos
    } catch (err) {
      setError("Error loading albums: " + err.message);
      console.log(err);
    } finally {
      setLoading(false);
    }
  };

  const getPhotos = async () => {
    if (!albumSelected) {
      setPhotos([]);
      return;
    }

    try {
      setLoading(true);
      setError("");
      const url = urlPhotos + `?albumId=${albumSelected}`;
      const response = await fetch(url);
      if (!response.ok) throw new Error("Failed to fetch photos");
      const result = await response.json();
      setPhotos(result);
    } catch (err) {
      setError("Error loading photos: " + err.message);
      console.log(err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    getUsers();
  }, []);

  useEffect(() => {
    getAlbums();
  }, [userSelected]);

  useEffect(() => {
    getPhotos();
  }, [albumSelected]);

  const handleUserChange = (e) => {
    setUserSelected(e.target.value);
  };

  const handleAlbumChange = (e) => {
    setAlbumSelected(e.target.value);
  };

  if (loading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div>{error}</div>;
  }

  return (
    <div>
      <h1>
        Gestione Albums e Photos
      </h1>
      <div>
        <div>
          <select
            className="form-select"
            value={userSelected}
            onChange={handleUserChange}
          >
            <option value="">-- Seleziona Utente --</option>
            {users.map((u) => (
              <option key={u.id} value={u.id}>
                {u.name}
              </option>
            ))}
          </select>
        </div>

        <div>
          <select
            className="form-select"
            value={albumSelected}
            onChange={handleAlbumChange}
          >
            <option value="">-- Seleziona Album --</option>
            {albums.map((a) => (
              <option key={a.id} value={a.id}>
                {a.title}
              </option>
            ))}
          </select>
        </div>
      </div>

      {photos.length > 0 && (
        <div>
          <h2>
            Photos ({photos.length})
          </h2>
          <div>
            {photos.map((photo) => (
              <div key={photo.id}>
                <div>
                  <img
                    src={photo.thumbnailUrl}
                    alt={photo.title}
                  />
                </div>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
};

export default UserAlbums;