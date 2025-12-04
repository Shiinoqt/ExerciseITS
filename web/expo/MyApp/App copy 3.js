import { useState } from "react";
import {
  Button,
  FlatList,
  Modal,
  StyleSheet,
  Text,
  TextInput,
  View,
} from "react-native";

export default function App() {
  const [taskInput, setTaskInput] = useState("");
  const [tasks, setTasks] = useState([]);
  
  const Item = ({text}) => (
    <View style={styles.taskItem}>
      <Text style={styles.taskText}>{text}</Text>
    </View>
  );
  
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
      <View style={styles.inputContainer}>
        <TextInput
          placeholder="Type your task"
          style={styles.textInput}
          onChangeText={taskInputHandler}
          value={taskInput} // Add this to clear input visually
        />
        <Button 
          title="Add task"
          onPress={addTaskHandler}
        />
      </View>
      <View style={styles.tasksContainer}>
        <FlatList 
          data={tasks}
          renderItem={({item}) => <Item text={item.text} />}
          keyExtractor={item => item.id}
        />
      </View>
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
  textInput: {
    textAlign: 'center',
    borderColor: "#cccccc",
    borderWidth: 1,
    borderRadius: 40,
    width: '70%',
    height: '100%',
    paddingHorizontal: 8,
  },
  inputContainer: {
    justifyContent: 'space-between',
    alignItems: 'center',
    flexDirection: "row",
    height: 50,
  },
  tasksContainer: {
    // borderRadius: 40,
    // borderWidth: 1,
    // borderColor: '#cccccc',
    flex: 2,
    padding: 16,
  },
  taskItem: {
    alignItems: 'center',        // Centers horizontally
    justifyContent: 'center',    // Centers vertically
    backgroundColor: '#e4e4e469',
    height: 60,
    padding: 8,
    borderRadius: 40,
    marginBottom: 8,
  },
  taskText: {
    textAlign: 'center',         // Centers the text content
    fontSize: 16,
  },
});