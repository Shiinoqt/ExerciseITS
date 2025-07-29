import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import UserAlbums from './userAlbum'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <UserAlbums></UserAlbums>
    </>
  )
}

export default App
