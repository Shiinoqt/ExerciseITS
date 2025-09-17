import React from "react";
import { useState } from "react";
import { useEffect } from "react";

const url = "https://jsonplaceholder.typicode.com/photos?_limit=10";

const GalleriaFoto = () => {
    const [pictures, setPictures] = useState([]);
    const [isLoading, setIsLoading] = useState(true);
    const [isError, setIsError] = useState(false);

    const getPictures = async () => {
        setIsError(false);
        setIsLoading(true);
        try {
            const resp = await fetch(url);
            const data = await resp.json();
            setPictures(data);
        } catch (error) {
            console.log(error);
            setIsError(true);
        }
        setIsLoading(false);
    };
    
    useEffect(() => {
        getPictures();
    }, []);

    if (isLoading) {
        return <h1>Loading...</h1>;
    }

    if (isError) {
        return <h1>Error...</h1>;
    }

    return (
        <div>
            {pictures.map((p) => (
                <img key={p.id} src={p.thumbnailUrl} alt={p.title} />
            ))}
        </div>
    );
};

export default GalleriaFoto;