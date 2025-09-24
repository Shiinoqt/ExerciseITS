import React from 'react'

const TodoItem = ({task, onDeleteTask}) => {
  return (
    <li>
        <input
          type="checkbox"
          checked={task.completed}
          className="form-check-input me-2"
          
        ></input>
        <span
          style={{ textDecoration: task.completed ? "line-through" : "none" }}
        >
          {" "}
          {task.text}
        </span>
        <button onClick={() => {
            onDeleteTask(task.id);
        }}>Delete</button>
    </li>
  )
}

export default TodoItem
