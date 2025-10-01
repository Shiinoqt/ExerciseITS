import React, { useState } from "react";

const TodoItem = ({ task, onDeleteTask, onToggleTask, onUpdateTask }) => {
  const [isEditing, setIsEditing] = useState(false);
  const [editText, setEditText] = useState(task.text);
  
  const handleSave = () => {
    if (editText.trim()) {
      onUpdateTask(task.id, editText);
    } else {
      setEditText(task.text); // Ripristina il testo originale se vuoto
    }
    setIsEditing(false);
  };

  const handleCancel = () => {
    setEditText(task.text);
    setIsEditing(false);
  };

  return (
    <li className="list-group-item d-flex justify-content-between align-items-center">
      {isEditing ? (
        <input
          type="text"
          className="form-control"
          value={editText}
          onChange={(e) => setEditText(e.target.value)}
          onKeyDown={(e) => {
            if (e.key === "Enter") {
              e.preventDefault();
              handleSave();
            }
            if (e.key === "Escape") handleCancel();
          }}
          onBlur={handleSave}
          autoFocus
        />
      ) : (
        <>
          <div>
            <input
              type="checkbox"
              checked={task.completed}
              className="form-check-input me-2"
              onChange={() => onToggleTask(task.id, task.completed)}
            />
            <span
              style={{
                textDecoration: task.completed ? "line-through" : "none",
                cursor: "pointer"
              }}
              onDoubleClick={() => !task.completed && setIsEditing(true)}
            >
              {task.text}
            </span>
          </div>

          <button
            className="btn btn-danger btn-sm"
            onClick={() => onDeleteTask(task.id)}
          >
            Delete
          </button>
        </>
      )}
    </li>
  );
};

export default TodoItem;