import { FlatList, Pressable, StyleSheet, Text, View } from "react-native";

const TaskItem = ({ text, onDelete }) => (
  <Pressable onPress={onDelete} style={styles.taskItem}>
    <Text style={styles.taskText}>{text}</Text>
  </Pressable>
);

export default function TaskContainer({ tasks, onDeleteTask }) {
  return (
    <View style={styles.tasksContainer}>
      <FlatList 
        alwaysBounceVertical={true}
        data={tasks}
        renderItem={({ item }) => (
          <TaskItem 
            text={item.text} 
            onDelete={() => onDeleteTask(item.id)}
          />
        )}
        keyExtractor={item => item.id}h
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
    alignItems: 'center',
    justifyContent: 'center',
    backgroundColor: '#0088ff1c',
    height: 60,
    padding: 8,
    borderRadius: 40,
    marginBottom: 8,
  },
  taskText: {
    fontWeight: 'bold',
    textAlign: 'center',
    fontSize: 16,
  },
});
