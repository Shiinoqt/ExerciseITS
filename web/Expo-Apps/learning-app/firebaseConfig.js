// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getFirestore } from "firebase/firestore";
import { getAuth } from "firebase/auth";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyDU0gAzqBpvkreEu1lU5Mwi4EzaDw69W50",
  authDomain: "learning-app-48aef.firebaseapp.com",
  projectId: "learning-app-48aef",
  storageBucket: "learning-app-48aef.firebasestorage.app",
  messagingSenderId: "451565253773",
  appId: "1:451565253773:web:803bb2393cdc38df471ec4"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const db = getFirestore(app);
const auth = getAuth(app);

export {app, db, auth}