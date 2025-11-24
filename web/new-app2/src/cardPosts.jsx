import { useState, useEffect } from 'react';

const CardPosts = () => {
    const url = "https://jsonplaceholder.typicode.com/posts/1";
    const urlUser = "https://jsonplaceholder.typicode.com/users/";
    const urlComments = "https://jsonplaceholder.typicode.com/posts/";
    const [post, setPost] = useState(null);
    const [user, setUser] = useState(null);
    const [comments, setComments] = useState([]);
    const [error, setError] = useState(null);

    useEffect(() => {
        let mounted = true;

        (async () => {
            try {
                const resp = await fetch(url);
                if (!resp.ok) throw new Error(`Post fetch failed: ${resp.status}`);
                const data = await resp.json();
                if (!mounted) return;
                setPost(data);

                const userResp = await fetch(urlUser + data.userId);
                if (!userResp.ok) throw new Error(`User fetch failed: ${userResp.status}`);
                const userData = await userResp.json();
                if (!mounted) return;
                setUser(userData);

                const commentsResp = await fetch(urlComments + data.id + '/comments');
                if (!commentsResp.ok) throw new Error(`Comments fetch failed: ${commentsResp.status}`);
                const commentsData = await commentsResp.json();
                if (!mounted) return;
                setComments(commentsData);
            } catch (err) {
                console.error('Error fetching data:', err);
                if (mounted) setError(err.message || 'Unknown error');
            }
        })();

        return () => { mounted = false; };
    }, []);

    if (error) return <div className="cardPost">Error: {error}</div>;
    if (!post) return <div className="cardPost">Loading...</div>;

    return (
        <div className="cardPost">
            <h2>{post.title}</h2>
            <p>{post.body}</p>
            {user && <h3>Author: {user.name} ({user.email})</h3>}
            <h4>Comments:</h4>
            <ul>
                {comments.map(comment => (
                    <li key={comment.id}>
                        <strong>{comment.name}:</strong> {comment.body}
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default CardPosts;