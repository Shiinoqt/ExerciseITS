import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import Home from './components/Home';
import AddBook from './components/AddBook';

const Stack = createNativeStackNavigator();


export default function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName='Home'>
        <Stack.Screen name="Home" component={Home} options={{
          title: 'My Library 📚',
          headerTitleAlign: 'center', // Centers the title on Android
          headerStyle: {
            backgroundColor: '#f8f9fa', // Match your screen background
            elevation: 0, // Removes shadow on Android
            shadowOpacity: 0, // Removes shadow on iOS
            borderBottomWidth: 0, // Clean look without bottom line
          },
          headerTitleStyle: {
            fontWeight: 'bold',
            fontSize: 20,
            color: '#1a1a1a',
          },
        }} />
        <Stack.Screen name="AddBook" component={AddBook} options={{ title: "Aggiungi libro" }} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}

