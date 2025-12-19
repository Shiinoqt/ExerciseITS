import React from 'react'
import { useState, useEffect } from 'react'

const urlUsers = "https://jsonplaceholder.typicode.com/users";
const urlAlbums = "https://jsonplaceholder.typicode.com/albums";
const urlPhotos = "https://jsonplaceholder.typicode.com/photos";

const User = () => {
    const [users, setUsers] = useState([]);
    const [userSelected, setUserSelected] = useState(null);

    const [albums, setAlbums] = useState([]);
    const [albumSelected, setAlbumSelected] = useState("");

    const [photos, setPhotos] = useState([]);

    const handleUserSelected = (e) => {
        setUserSelected(e.target.value)
    };

    const handleAlbumSelected = (e) => {
        setAlbumSelected(e.target.value)
    };

    const fetchUser = async () => {
        try {
            const response = await fetch(urlUsers);
            if (!response.ok) {
                throw new Error(`HTTP error: Status ${response.status}`);
            }
            let userData = await response.json();
            setUsers(userData)
        } catch (err) {
            console.log(err)
        }
    }

    const getAlbums = async () => {
        if (!userSelected) {
            setAlbums([]);
            setAlbumSelected("");
            setPhotos([]);
            return;
        }

        try {
            const response = await fetch(urlAlbums + `?userId=${userSelected}`);
            if (!response.ok) {
                throw new Error(`HTTP error: Status ${response.status}`);
            }
            let albumData = await response.json();
            setAlbums(albumData);
            setAlbumSelected("");
            setPhotos([]);
        } catch (err) {
            console.log(err)
        }
    }

    const getPhotos = async () => {
        if (!albumSelected) {
            setPhotos([]);
            return;
        }

        try {
            const response = await fetch(urlPhotos + `?albumId=${albumSelected}`);
            if (!response.ok) {
                throw new Error(`HTTP error: Status ${response.status}`);
            }
            let photos = await response.json();
            setPhotos(photos);
        } catch (err) {
            console.log(err)
        }
    }

    useEffect(() => {
        fetchUser()
    }, []);

    useEffect(() => {
        getAlbums()
    }, [userSelected]);

    useEffect(() => {
        getPhotos()
    }, [albumSelected])

    // useEffect(() => {
    //     fetch(urlUsers)
    //         .then(response => {
    //             console.log('Response ok:', response.ok);
    //             return response.json();
    //         })
    //         .then(userData => setUsers(userData))
    //         .catch(err => console.log(err))
    //     }, []);
    return (
        <>
            <select
                value={userSelected}
                onChange={handleUserSelected}
            >
                <option>Select a user</option>
                {users.map(user => (
                    <option key={user.id} value={user.id}>{user.name}</option>
                ))}
            </select>

            <select
                value={albumSelected}
                onChange={handleAlbumSelected}
            >
                <option>Select album</option>
                {albums.map(album => (
                    <option key={album.id} value={album.id}>{album.title}</option>
                ))}
            </select>

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
        </>
    )
}

export default User
