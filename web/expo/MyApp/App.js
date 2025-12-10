import { useState } from "react";
import {
  StyleSheet,
  View,
} from "react-native";
import TaskInput from "./TaskInput";
import TaskContainer from "./TaskContainer";


export default function App() {
  const [taskInput, setTaskInput] = useState("");
  const [tasks, setTasks] = useState([]);
  
  function deleteTaskHandler(id) {
    setTasks((currentTasks) => 
      currentTasks.filter((task) => task.id !== id)
    );
  }

  function taskInputHandler(enteredTask) {
    setTaskInput(enteredTask);
  }
  
  function addTaskHandler() {
    if (taskInput.trim() === "") return; 
    setTasks((currentTasks) => [
      ...currentTasks,
      {text: taskInput, id: Math.random().toString()}
    ]);
    setTaskInput("");
  }
  
  return (
    <View style={styles.appContainer}>
      <TaskInput 
        taskInput={taskInput}
        onChangeText={taskInputHandler}
        onAddTask={addTaskHandler}
      />
      <TaskContainer 
        tasks={tasks}
        onDeleteTask={deleteTaskHandler}
      />
    </View>
  );
}

const styles = StyleSheet.create({
  appContainer: {
    flex: 1,
    gap: 20,
    backgroundColor: "#ffffff",
    paddingTop: '20%',
    paddingHorizontal: 16,
    paddingBottom: '5%',
  },
});