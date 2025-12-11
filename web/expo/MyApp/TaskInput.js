import { Button, StyleSheet, TextInput, View } from "react-native";

export default function TaskInput({ taskInput, onChangeText, onAddTask, onCancel }) {
  return (
    <View style={styles.inputContainer}>
      <TextInput
        placeholder="Type your task"
        style={styles.textInput}
        onChangeText={onChangeText}
        value={taskInput}
      />
      <View style={styles.buttonContainer}>
        <View style={styles.button}>
          <Button 
            title="Add task"
            onPress={onAddTask}
          />
        </View>
        {onCancel && (
          <View style={styles.button}>
            <Button 
              title="Cancel"
              onPress={onCancel}
              color="#ff4444"
            />
          </View>
        )}
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  inputContainer: {
    gap: 16,
  },
  textInput: {
    textAlign: 'center',
    borderColor: "#cccccc",
    borderWidth: 1,
    borderRadius: 40,
    width: '100%',
    height: 50,
    paddingHorizontal: 8,
  },
  buttonContainer: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    gap: 12,
  },
  button: {
    flex: 1,
  },
});