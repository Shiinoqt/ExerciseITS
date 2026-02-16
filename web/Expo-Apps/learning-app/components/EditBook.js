import React, { useState } from 'react';
import { TextInput, View, StyleSheet, TouchableOpacity, Text, Alert } from 'react-native';

// Base URL
const BASE_URL = "https://learning-app-48aef-default-rtdb.europe-west1.firebasedatabase.app";

const EditBook = ({ route, navigation }) => {
    // 1. Get the book data passed from the Home screen
    const { book } = route.params;

    const [title, setTitle] = useState(book.title);
    const [author, setAuthor] = useState(book.author);
    const [genre, setGenre] = useState(book.genre);

    const handleUpdate = async () => {
        if (!title || !author || !genre) {
            Alert.alert('Please fill all fields');
            return;
        }

        const updatedData = {
            title,
            author,
            genre,
            lastEditedAt: new Date().toISOString()
        };

        try {
            // 2. The URL must target the specific ID: /books/ID.json
            const url = `${BASE_URL}/books/${book.id}.json`;

            const response = await fetch(url, {
                method: 'PATCH', // Use PATCH to merge changes
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(updatedData),
            });

            if (response.ok) {
                Alert.alert('Success', 'Book updated successfully');
                navigation.goBack(); // Return to Home
            } else {
                throw new Error('Failed to update database');
            }
        } catch (error) {
            Alert.alert('Error updating book', error.message);
        }
    };

    return (
        <View style={styles.container}>
            <TextInput
                placeholder='Title'
                style={styles.input}
                value={title}
                onChangeText={setTitle} />
            <TextInput
                placeholder='Author'
                style={styles.input}
                value={author}
                onChangeText={setAuthor} />
            <TextInput
                placeholder='Genre'
                style={styles.input}
                value={genre}
                onChangeText={setGenre} />
            
            <TouchableOpacity
                style={styles.saveButton}
                onPress={handleUpdate}>
                <Text style={styles.saveButtonText}>Update Book</Text>
            </TouchableOpacity>

            <TouchableOpacity
                onPress={() => navigation.goBack()}>
                <Text style={{color: 'gray'}}>Cancel</Text>
            </TouchableOpacity>
        </View>
    );
};

export default EditBook;

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
        width: '70%',
    },
    saveButton: {
        backgroundColor: "#5067FF", // Blue for update
        paddingHorizontal: 30,
        paddingVertical: 12,
        borderRadius: 30,
        marginBottom: 20,
        marginTop: 10,
    },
    saveButtonText: { color: "white", fontSize: 14, fontWeight: "bold" },
});