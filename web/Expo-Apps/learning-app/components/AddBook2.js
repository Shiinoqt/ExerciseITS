import React, { useState } from 'react'
import { addDoc, collection, updateDoc, doc} from 'firebase/firestore';
import { TextInput, View, StyleSheet, Button, TouchableOpacity, Text, Alert } from 'react-native'
import { db } from '../firebaseConfig';

const AddBook = ({ navigation }) => {
    const [title, setTitle] = useState('');
    const [author, setAuthor] = useState('');
    const [genre, setGenre] = useState('');

    const handleSave = async () => {
        if (!title || !author || !genre) {
            Alert.alert('Please fill all fields');
            return;
        }
        try {
            await addDoc(collection(db, 'books'), {
                title,
                author,
                genre,
                addedAt: new Date()
            });
            Alert.alert('Book added successfully');
            navigation.goBack();
        } catch (error) {
            Alert.alert('Error adding book: ', error.message);
        };
        console.log('Saving:', { title, author, genre });
    }

    return (
        <View style={styles.container}>
            <TextInput
                placeholder='Title'
                keyboardType="default"
                style={styles.input}
                value={title}
                onChangeText={setTitle} />
            <TextInput
                placeholder='Author'
                keyboardType="default"
                style={styles.input}
                value={author}
                onChangeText={setAuthor} />
            <TextInput
                placeholder='Genre'
                keyboardType="default"
                style={styles.input}
                value={genre}
                onChangeText={setGenre} />
            <TouchableOpacity
                style={styles.saveButton}
                onPress={handleSave}>
                <Text style={styles.saveButtonText}>Save</Text>
            </TouchableOpacity>
        </View>
    )
}

export default AddBook

const styles = StyleSheet.create({
    container: {
        flex: 1,
        justifyContent: 'center',
        alignItems: 'center',
        backgroundColor: '#fff',
    },
    input: {
        height: 40,
        borderColor: 'gray',
        borderWidth: 1,
        borderRadius: 12,
        marginBottom: 10,
        paddingHorizontal: 10,
        width: '60%',
    },
    fab: {
        position: "absolute",
        width: 60,
        height: 60,
        bottom: 30,
        right: 30,
        backgroundColor: "#5067FF",
        borderRadius: 30,
        justifyContent: "center",
        alignItems: "center",
        elevation: 8,
    },
    fabText: { color: "white", fontSize: 45, bottom: 10 },
    saveButton: {
        backgroundColor: "#23b35f",
        paddingHorizontal: 20,
        paddingVertical: 12,
        borderRadius: 30,
        marginBottom: 20,
    },
    saveButtonText: { color: "white", fontSize: 14, fontWeight: "bold" },
})