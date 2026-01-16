import { View, Text, TextInput, Button } from "react-native";
import { useState } from "react";
import { submitFormData } from "./FormService";

export default function Form() {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [message, setMessage] = useState("");

  const handleSubmit = () => {
    const success = submitFormData({ name, email, message });
    
    if (success) {
      // Clear form after successful submission
      setName("");
      setEmail("");
      setMessage("");
    }
  };

  return (
    <View>
      <Text>Name</Text>
      <TextInput
        placeholder="Enter your name"
        value={name}
        onChangeText={setName}
      />

      <Text>Email</Text>
      <TextInput
        placeholder="Enter your email"
        value={email}
        onChangeText={setEmail}
        keyboardType="email-address"
      />

      <Text>Message</Text>
      <TextInput
        placeholder="Enter your message"
        value={message}
        onChangeText={setMessage}
        multiline
      />

      <Button title="Submit" onPress={handleSubmit} />
    </View>
  );
}
