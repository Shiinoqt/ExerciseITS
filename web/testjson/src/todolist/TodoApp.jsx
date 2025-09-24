import React, { useState, useEffect } from 'react'
import TodoList from './TodoList';
import TodoForm from './TodoForm';

const API_URL = 'http://localhost:4000/tasks';
const todoapp = () => {
    const [tasks, setTasks] = useState([]);
    const [isLoading, setIsLoading] = useState(false);
    const [error, setError] = useState(null);

    const getTasks = async () => {
        try {
            setIsLoading(true);
            setError(null);
            const response = await fetch(API_URL);
            if (!response.ok) throw new Error('Failed to fetch tasks');
            const data = await response.json();
            setTasks(data);
        } catch (err) {
            setError(err.message);
        } finally {
            setIsLoading(false);
        }
    };

    const deleteTask = async (id) =>{
        await fetch(API_URL+"/"+id,{method:"DELETE"});
            getTasks();
    };
    
    useEffect(() => {
        getTasks();
    }, []);

  return (
    <div><h1>Todo App</h1>
      <TodoForm></TodoForm>
      <TodoList tasks={tasks} onDeleteTask={deleteTask}></TodoList>
    </div>
  )
}

export default todoapp
