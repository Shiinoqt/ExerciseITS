import { useState, useEffect } from 'react';

export default function PostsDisplay() {
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    const fetchPosts = async () => {
      try {
        const response = await fetch('https://jsonplaceholder.typicode.com/posts/');
        const postsData = await response.json();

        // Fetch user and comments for each post
        const postsWithDetails = await Promise.all(
          postsData.map(async (post) => {
            const [userResponse, commentsResponse] = await Promise.all([
              fetch(`https://jsonplaceholder.typicode.com/users/${post.userId}`),
              fetch(`https://jsonplaceholder.typicode.com/comments?postId=${post.id}`)
            ]);

            const user = await userResponse.json();
            const comments = await commentsResponse.json();

            return {
              ...post,
              userName: user.name,
              commentsCount: comments.length
            };
          })
        );

        setPosts(postsWithDetails);
      } catch (err) {
        console.error('Error fetching posts:', err);
      }
    };

    fetchPosts();
  }, [])

  return (
    <div className="container">
      <style>{`
        * {
          box-sizing: border-box;
        }
        .container {
          display: flex;
          flex-wrap: wrap;
          gap: 20px;
          justify-content: center;
          padding: 20px;
        }
        .card {
          border: 2px solid #b9b9b9;
          border-radius: 8px;
          padding: 10px;
          max-width: 300px;
          background-color: #ffffff;
          box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        }
        .card h2 {
          font-size: 18px;
          margin-top: 0;
          color: #333;
        }
        .card p {
          color: #666;
          line-height: 1.5;
        }
        .user-info {
          font-size: 14px;
          color: #888;
          margin: 10px 0;
          font-weight: bold;
        }
        .comments-count {
          font-size: 12px;
          color: #999;
          margin-top: 10px;
        }`}
        </style>
      {posts.map((post) => (
        <div key={post.id} className="card">
          <h2>{post.title}</h2>
          <div className="user-info">By: {post.userName}</div>
          <p>{post.body}</p>
          <div className="comments-count">{post.commentsCount} comment(s)</div>
        </div>
      ))}
    </div>
  );
}