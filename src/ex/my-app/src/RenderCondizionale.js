import React, { useEffect, useState } from 'react'

const url = "https://jsonplaceholder.typicode.com/photos";
const RenderCondizionale = () => {
    const [isLoading, setIsLoading] = useState(false);
    const [isError, setIsError] = useState(false);
    const [photos, setPhotos] = useState([]);

    const getData = async () => {
        setIsError(false);
        setIsLoading(true);
        try {
            const resp = await fetch(url);
            const data = await resp.json();
            setPhotos(data);
        } catch (error) {
            console.log(error)
            setIsError(true);
        }
        setIsLoading(false);
    }

    useEffect(() => {
        getData();
    }, []);

    if (isLoading) {
        return <h1>Loading...</h1>
    }

    if (isError) {
        return <h1>Error...</h1>
    }

    return (
        <div>
            {photos.map((p) => (
                <p key={p.id}>{p.title}</p>
            ))}
        </div>
    )
}
export default RenderCondizionale
