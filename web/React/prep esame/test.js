const url="https://jsonplaceholder.typicode.com/posts/1";

let post = null;

// using fetch with promises
fetch(url)
  .then(response => response.json())
  .then(data => {
    post = data;
    console.log("Post fetched:", post);
  })
  .catch(error => {
    console.error("Error fetching post:", error);
  });

// async function to get the post
async function getPost() {
  try {
    const response = await fetch(url);
    const data = await response.json();
    return data;
  } catch (error) {
    console.error("Error fetching post:", error);
  }
}

getPost().then(data => {
  console.log("Post from async function:", data);
});