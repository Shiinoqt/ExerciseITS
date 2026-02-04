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
  const [tasks,setTasks] = useState("");
  
  function taskInputHandler(enteredTask){
    console.log(enteredTask)
    setTasks(enteredTask)
  }

  return (
    <View style={styles.appContainer}>
      <View style={styles.inputContainer}>
        <TextInput
          placeholder="Type your task"
          style={styles.textInput}
          onChangeText={taskInputHandler}
        ></TextInput>
        <Button title="Add task"></Button>
      </View>
      <View style={styles.tasksContainer}>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  appContainer: {
    flex: 1,
    gap: 20,
    backgroundColor: "#ffffffff",
    paddingTop: '20%',
    paddingHorizontal: 16,
    paddingBottom: '5%',
  },
  textInput: {
    textAlign: 'center',
    borderColor: "#cccccc",
    borderWidth: 1,
    borderRadius: 20,
    gap: 20,
    width: '70%',
    height: '100%',
  },
  inputContainer: {
    justifyContent: 'space-between',
    alignItems: 'center',
    flexDirection: "row",
  },
  tasksContainer: {
    borderRadius: 40,
    borderWidth: 1,
    borderColor: '#cccccc',
    flex: 2,
    alignItems: 'center',
  },
});