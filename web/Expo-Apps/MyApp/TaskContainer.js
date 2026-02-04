import { FlatList, Pressable, StyleSheet, Text, View } from "react-native";

const TaskItem = ({ task, done, onDelete, onToggle }) => (
  <View style={styles.taskItem}>
    <Pressable onPress={onToggle} style={styles.checkbox}>
      <View style={[styles.checkboxInner, done && styles.checkboxChecked]}>
        {done && <Text style={styles.checkmark}>✓</Text>}
      </View>
    </Pressable>
    <Pressable onPress={onDelete} style={styles.taskTextContainer}>
      <Text style={[styles.taskText, done && styles.doneText]}>{task}</Text>
    </Pressable>
  </View>
);

export default function TaskContainer({ tasks, onDeleteTask, onToggleDone }) {
  return (
    <View style={styles.tasksContainer}>
      <FlatList 
        alwaysBounceVertical={true}
        data={tasks}
        renderItem={({ item }) => (
          <TaskItem 
            task={item.task} 
            done={item.done}
            onDelete={() => onDeleteTask(item.id)}
            onToggle={() => onToggleDone(item.id, !item.done)}
          />
        )}
        keyExtractor={item => item.id}
      />
    </View>
  );
}

const styles = StyleSheet.create({
  tasksContainer: {
    borderRadius: 40,
    borderWidth: 1,
    borderColor: '#cccccc',
    flex: 2,
    padding: 16,
  },
  taskItem: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: '#0088ff1c',
    height: 60,
    padding: 8,
    borderRadius: 40,
    marginBottom: 8,
  },
  checkbox: {
    marginRight: 12,
    marginLeft: 12,
  },
  checkboxInner: {
    width: 24,
    height: 24,
    borderRadius: 15,
    borderWidth: 2,
    borderColor: '#0088ff',
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: 'white',
  },
  checkboxChecked: {
    backgroundColor: '#0088ff',
  },
  checkmark: {
    color: 'white',
    fontSize: 16,
    fontWeight: 'bold',
  },
  taskTextContainer: {
    flex: 1,
    justifyContent: 'center',
  },
  taskText: {
    fontWeight: 'bold',
    fontSize: 16,
  },
  doneText: {
    textDecorationLine: 'line-through',
    color: '#888',
  },
});