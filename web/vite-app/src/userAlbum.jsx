import React, { useEffect, useState } from "react";

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
           
  return (
    <div className="max-w-6xl mx-auto p-6 bg-gray-50 min-h-screen">
      <h1 className="text-3xl font-bold text-gray-800 mb-8 text-center">
        Gestione Albums e Photos
      </h1>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mb-8">
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
          <h2 className="text-xl font-semibold text-gray-800 mb-4">
            Photos ({photos.length})
          </h2>
          <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
            {photos.map((photo) => (
              <div 
                key={photo.id} 
                className="bg-white rounded-lg shadow-lg overflow-hidden hover:shadow-xl transition-shadow duration-300"
              >
                <div className="aspect-square">
                  <img
                    src={photo.thumbnailUrl}
                    alt={photo.title}
                    className="w-full h-full object-cover"
                    loading="lazy"
                  />
                </div>
                <div className="p-3">
                  <h3 className="text-sm font-medium text-gray-800 mb-1">
                    {photo.title}
                  </h3>
                  <p className="text-xs text-gray-500">
                    ID: {photo.id}
                  </p>
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