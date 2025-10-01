import React from 'react'
import TodoItem from './TodoItem'

const TodoList = ({ tasks, onDeleteTask, onToggleTask }) => {
  return (
    <ul className="list-group">
      {tasks.map(task => (
        <TodoItem 
          key={task.id} 
          task={task} 
          onDeleteTask={onDeleteTask}
          onToggleTask={onToggleTask}
        />
      ))}
    </ul>
  )
}

export default TodoList