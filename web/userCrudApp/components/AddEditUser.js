import React, { useEffect, useState } from 'react'
import { Button, TextInput, View, StyleSheet, Alert } from 'react-native'
import { addDoc, collection, updateDoc, doc} from 'firebase/firestore';
import { db } from '../firebaseConfig';

const AddEditUser = ({ navigation, route }) => {
    const [name, setName] = useState('');
    const [surname, setSurname] = useState('');
    const [email, setEmail] = useState('');
    const [phone, setPhone] = useState('');

    const userEdit = route.params ? route.params.user.id : null;

    const handleSave = async () => {
        // Logic to save user details
        if (!name || !surname || !email || !phone) {
            Alert.alert('Please fill all fields');
            return;
        }
        try {
            if (userEdit) {
                const userRef = doc(db, 'users', userEdit);
                await updateDoc(userRef, {
                    name,
                    surname,
                    email,
                    phone,
                });
                Alert.alert('User updated successfully');
            } else {
                await addDoc(collection(db, 'users'), {
                    name,
                    surname,
                    email,
                    phone,
                    createdAt: new Date()
                });
                Alert.alert('User added successfully');
            }
            navigation.goBack();
        } catch (error) {
            Alert.alert('Error adding user: ', error.message);
        };
    }

    useEffect(() => {
        if (userEdit) {
            setName(userEdit.name)
            setSurname(userEdit.surname)
            setEmail(userEdit.email)
            setPhone(userEdit.phone)
            navigation.setOptions({ title: 'Edit User' });
        } else {
            navigation.setOptions({ title: 'Add User' });
        }
    }, [userEdit, navigation]);

    return (
        <View style={styles.container}>
            <TextInput
                placeholder="Name"
                keyboardType="default"
                style={styles.input}
                value={name}
                onChangeText={setName} />
            <TextInput
                placeholder="Surname"
                keyboardType="default"
                style={styles.input}
                value={surname}
                onChangeText={setSurname} />
            <TextInput
                placeholder="Email"
                keyboardType="email-address"
                style={styles.input}
                value={email}
                onChangeText={setEmail} />
            <TextInput
                placeholder="Phone"
                keyboardType="phone-pad"
                style={styles.input}
                value={phone}
                onChangeText={setPhone} />
            <Button
                style={styles.button}
                title="Save User"
                onPress={handleSave}
            />
        </View>
    )
}

const styles = StyleSheet.create({
    container: {
        flex: 1, // This is crucial to make the view visible
        justifyContent: 'center',
        alignItems: 'center',
        backgroundColor: '#fff',
    },
    input: {
        height: 40,
        borderColor: 'gray',
        borderWidth: 1,
        borderRadius: 24,
        marginBottom: 10,
        paddingHorizontal: 10,
        width: '60%',
    },
    button: {
        backgroundColor: '#007AFF',
        padding: 15,
        borderRadius: 24,
    }
});

export default AddEditUser