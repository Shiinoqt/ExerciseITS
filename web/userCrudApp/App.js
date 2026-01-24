import { StatusBar } from 'expo-status-bar';
import { StyleSheet } from 'react-native';
// 1. Added NavigationContainer import
import { NavigationContainer } from '@react-navigation/native'; 
// 2. Corrected the package name for the stack navigator
import { createNativeStackNavigator } from '@react-navigation/native-stack'; 

import Home from './components/Home';
import AddEditUser from './components/AddEditUser';

const Stack = createNativeStackNavigator();

export default function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="Home">
        <Stack.Screen 
          name="Home" 
          component={Home}
          options={{ title: "Lista Utenti"}}
          />
        <Stack.Screen 
          name="AddEditUser" 
          component={AddEditUser}
          options={{ title: "Aggiungi/Modifica Utente"}}
          />
      </Stack.Navigator>
      <StatusBar style="auto" />
    </NavigationContainer>
  );
}