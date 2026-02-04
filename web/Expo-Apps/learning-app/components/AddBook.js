import React, { useState } from 'react';
import { TextInput, View, StyleSheet, TouchableOpacity, Text, Alert, ActivityIndicator } from 'react-native';

// FIX: Ensure the URL points to the collection AND ends in .json
const DB_URL = "https://learning-app-48aef-default-rtdb.europe-west1.firebasedatabase.app/books.json";

const AddBook = ({ navigation }) => {
    const [title, setTitle] = useState('');
    const [author, setAuthor] = useState('');
    const [genre, setGenre] = useState('');
    const [isSaving, setIsSaving] = useState(false); // Added loading state

    const handleSave = async () => {
        if (!title || !author || !genre) {
            Alert.alert('Please fill all fields');
            return;
        }

        setIsSaving(true);

        const newBook = {
            title,
            author,
            genre,
            addedAt: new Date().toISOString()
        };

        try {
            const response = await fetch(DB_URL, {
                method: 'POST', // POST creates a new unique ID automatically
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(newBook),
            });

            if (response.ok) {
                const data = await response.json(); 
                console.log('Success! New ID:', data.name);
                
                Alert.alert('Success', 'Book added successfully');
                navigation.goBack();
            } else {
                const errorData = await response.text();
                throw new Error(errorData || 'Failed to save');
            }
        } catch (error) {
            Alert.alert('Error', error.message);
        } finally {
            setIsSaving(false);
        }
    };

    return (
        <View style={styles.container}>
            <TextInput
                placeholder='Title'
                style={styles.input}
                value={title}
                onChangeText={setTitle}
                editable={!isSaving}
            />
            <TextInput
                placeholder='Author'
                style={styles.input}
                value={author}
                onChangeText={setAuthor}
                editable={!isSaving}
            />
            <TextInput
                placeholder='Genre'
                style={styles.input}
                value={genre}
                onChangeText={setGenre}
                editable={!isSaving}
            />
            
            <TouchableOpacity
                style={[styles.saveButton, isSaving && { backgroundColor: '#ccc' }]}
                onPress={handleSave}
                disabled={isSaving}>
                {isSaving ? (
                    <ActivityIndicator color="white" />
                ) : (
                    <Text style={styles.saveButtonText}>Save Book</Text>
                )}
            </TouchableOpacity>
        </View>
    );
};

export default AddBook;

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