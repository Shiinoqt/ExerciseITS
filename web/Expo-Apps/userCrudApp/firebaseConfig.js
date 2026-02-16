// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getFirestore } from "firebase/firestore";
import { getAuth } from "firebase/auth";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyADQq1sUucuGQfCA_wheT9vigAbTDZjkJ4",
  authDomain: "user-crud-719d9.firebaseapp.com",
  databaseURL: "https://user-crud-719d9-default-rtdb.europe-west1.firebasedatabase.app",
  projectId: "user-crud-719d9",
  storageBucket: "user-crud-719d9.firebasestorage.app",
  messagingSenderId: "855267273502",
  appId: "1:855267273502:web:1cfab8aa6c018b82a6b70f"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const db = getFirestore(app);
const auth = getAuth(app);

export {app, db, auth}