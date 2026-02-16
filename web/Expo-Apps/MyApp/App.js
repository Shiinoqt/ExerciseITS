import { useState } from "react";
import {
  StyleSheet,
  View,
  Modal,
  Button,
} from "react-native";
import TaskInput from "./TaskInput";
import TaskContainer from "./TaskContainer";
import useTasks from "./TaskService";

export default function App() {
  const [taskInput, setTaskInput] = useState("");
  const [modalVisible, setModalVisible] = useState(false);
  const [filter, setFilter] = useState("all"); // "all", "todo", "done"
  const { tasks, addTask, toggleDone, deleteTask } = useTasks();

  function startAddTask() {
    setModalVisible(true);
  }
  
  function endAddTask() {
    setModalVisible(false);
    setTaskInput("");
  }

  function deleteTaskHandler(id) {
    deleteTask(id);
  }

  function taskInputHandler(enteredTask) {
    setTaskInput(enteredTask);
  }
  
  function addTaskHandler() {
    if (taskInput.trim() === "") return; 
    addTask(taskInput);
    setTaskInput("");
    endAddTask();
  }

  // Filter tasks based on the selected filter
  const filteredTasks = tasks.filter(task => {
    if (filter === "todo") return !task.done;
    if (filter === "done") return task.done;
    return true; // "all"
  });
  
  return (
    <View style={styles.appContainer}>
      <Button title="Add New Task" onPress={startAddTask} />
      
      {/* Filter buttons */}
      <View style={styles.filterContainer}>
        <View style={styles.filterButton}>
          <Button 
            title="All" 
            onPress={() => setFilter("all")}
            color={filter === "all" ? "#0088ff" : "#888888"}
          />
        </View>
        <View style={styles.filterButton}>
          <Button 
            title="Todo" 
            onPress={() => setFilter("todo")}
            color={filter === "todo" ? "#0088ff" : "#888888"}
          />
        </View>
        <View style={styles.filterButton}>
          <Button 
            title="Done" 
            onPress={() => setFilter("done")}
            color={filter === "done" ? "#0088ff" : "#888888"}
          />
        </View>
      </View>
      
      <Modal 
        visible={modalVisible} 
        animationType="fade"
        transparent={true}
      >
        <View style={styles.modalOverlay}>
          <View style={styles.modalContent}>
            <TaskInput 
              taskInput={taskInput}
              onChangeText={taskInputHandler}
              onAddTask={addTaskHandler}
              onCancel={endAddTask}
            />
          </View>
        </View>
      </Modal>

      <TaskContainer 
        tasks={filteredTasks}
        onDeleteTask={deleteTaskHandler}
        onToggleDone={toggleDone}
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
  filterContainer: {
    flexDirection: 'row',
    gap: 12,
    justifyContent: 'space-between',
  },
  filterButton: {
    flex: 1,
  },
  modalOverlay: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    //backgroundColor: 'rgba(0, 0, 0, 0.5)',
    backgroundColor: 'transparent',
  },
  modalContent: {
    width: '80%',
    backgroundColor: 'white',
    borderRadius: 20,
    padding: 20,
    shadowColor: '#000',
    shadowOffset: {
      width: 0,
      height: 5,
    },
    shadowOpacity: 0.15,
    shadowRadius: 4,
    elevation: 5,
  },
});