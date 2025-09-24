import React from 'react'
import TodoItem from './TodoItem'

const TodoList = ({tasks, onDeleteTask}) => {
  return (
    <div>
  {
    tasks.map(task => (
      <TodoItem key={task.id} task={task} onDeleteTask={onDeleteTask}></TodoItem>
    ))
  }
    </div>
  )
}

export default TodoList
