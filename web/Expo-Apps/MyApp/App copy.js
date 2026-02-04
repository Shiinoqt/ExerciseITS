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
  const [messaggio, setMessaggio] = useState("Ciao");
  const [visible, setVisible] = useState(false);
  const [nome, setNome] = useState("");
  const [openModal, setOpenModal] = useState(false);
  const [counter, setCounter] = useState(0);
  const [number1, setNumber1] = useState(0);
  const [number2, setNumber2] = useState(0);

  const result = (number1 && number2) ? parseInt(number1) + parseInt(number2) : 0;
  const dati = [
    { id: "1", nome: "Mario" },
    { id: "2", nome: "Rob" },
    { id: "3", nome: "Gino" },
  ];
  return (
    <View style={styles.container}>
      <Text>{nome}</Text>
      {visible && <Text>{messaggio}</Text>}
      <TextInput
        placeholder="Inserisci testo"
        onChangeText={setNome}
        style={styles.inputText}
        value={nome}
      ></TextInput>
      <Button
        title="Cambia testo"
        onPress={() => setMessaggio("Ho premuto il pulsante")}
      />
      <Button
        title={visible ? "Nascondi" : "Visualizza"}
        onPress={() => setVisible(!visible)}
      />
      <Button
        title="+"
        onPress={() => setCounter(counter + 1)}
      />
      <Button
        title="-"
        onPress={() => setCounter(counter - 1)}
      />
      <Text>{counter}</Text>

      <TextInput
        placeholder="Insert number 1"
        inputMode="numeric"
        style={styles.inputText}
        onChangeText={setNumber1}
        value={number1}
      />
      <TextInput
        placeholder="Insert number 2"
        inputMode="numeric"
        style={styles.inputText}
        onChangeText={setNumber2}
        value={number2}
      />
      <Text>Result is: {result}</Text>

      <View style={styles.containerList}>
        <FlatList
          data={dati}
          renderItem={(dato) => <Text>{dato.item.nome}</Text>}
          keyExtractor={(item) => item.id}
        />
      </View>
      <View style={styles.containerList}>
        <Button title="Apri" onPress={() => setOpenModal(true)}></Button>
        <Modal visible={openModal} animationType="slide">
          <View style={{padding:50}}>
            <Text>Sono una moda</Text>
            <Button title="Chiudi" onPress={() => setOpenModal(false)}></Button>
          </View>
        </Modal>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#fff",
    alignItems: "center",
    justifyContent: "center",
    padding: 50,
  },
  containerList: {
    flex: 2,
    backgroundColor: "#fff",
    alignItems: "center",
    justifyContent: "center",
  },
  inputText: {
    borderWidth: 1,
    padding: 10,
  },
});