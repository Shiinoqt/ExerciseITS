import { Button, StyleSheet, TextInput, View } from "react-native";

export default function TaskInput({ taskInput, onChangeText, onAddTask }) {
  return (
    <View style={styles.inputContainer}>
      <TextInput
        placeholder="Type your task"
        style={styles.textInput}
        onChangeText={onChangeText}
        value={taskInput}
      />
      <Button 
        title="Add task"
        onPress={onAddTask}
      />
    </View>
  );
}

const styles = StyleSheet.create({
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
});
