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
  
  return (
    <View style={styles.appContainer}>
      <Button title="Add New Task" onPress={startAddTask} />
      
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
        tasks={tasks}
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