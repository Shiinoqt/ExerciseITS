import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import TodoApp from './todolist/TodoApp'
import ProvaRoutes from './router/ProvaRoutes'

function App() {
  return (
    <>
      <ProvaRoutes></ProvaRoutes>
      <TodoApp></TodoApp>
    </>
  )
}

export default App
