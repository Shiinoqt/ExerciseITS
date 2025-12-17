import { useState, useEffect } from 'react';

const URL_BASE = "https://todoapp-f0f30-default-rtdb.europe-west1.firebasedatabase.app/tasks/";

export default function useTasks() {
    const [tasks, setTasks] = useState([]);

    const fetchTasks = async () => {
        try {
            const response = await fetch(URL_BASE + ".json");
            const data = await response.json();
            if (data) {
                const loadedTasks = Object.keys(data).map(key => ({
                    id: key,
                    ...data[key]
                }));
                setTasks(loadedTasks);
            } else {
                setTasks([]);
            }
        } catch (e) {
            console.error("Error loading tasks:", e);
        }
    };

    const addTask = async (taskText) => {
        if (!taskText.trim()) return;
        try {
            const response = await fetch(URL_BASE + ".json", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    task: taskText,
                    done: false
                })
            });
            if (response.ok) {
                fetchTasks(); // Refresh tasks
            } else {
                console.error("Error adding task:", response.status);
            }
        } catch (e) {
            console.error(e);
        }
    };

    const toggleDone = async (id, isDone) => {
        try {
            await fetch(URL_BASE + id + ".json", {
                method: "PATCH",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ done: isDone })
            });
            fetchTasks(); // Refresh after update
        } catch (e) {
            console.error("Error updating task:", e);
        }
    };

    const deleteTask = async (id) => {
        try {
            await fetch(URL_BASE + id + ".json", {
                method: "DELETE"
            });
            fetchTasks(); // Refresh after delete
        } catch (e) {
            console.error("Error deleting task:", e);
        }
    };

    useEffect(() => {
        fetchTasks();
    }, []);

    return { tasks, addTask, toggleDone, deleteTask };
}