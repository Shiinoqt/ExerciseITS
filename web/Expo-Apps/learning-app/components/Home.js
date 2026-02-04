import { useNavigation } from "@react-navigation/native";
import React, { useState, useEffect } from "react";
import {
    FlatList,
    StyleSheet,
    Text,
    TouchableOpacity,
    View,
    StatusBar,
    Alert
} from "react-native";

// Ensure the URL ends without a slash, we'll add it in the calls
const DB_URL = "https://learning-app-48aef-default-rtdb.europe-west1.firebasedatabase.app";

const Home = () => {
    const navigation = useNavigation();
    const [books, setBooks] = useState([]);
    const [loading, setLoading] = useState(true);

    // 1. Fetch Logic
    const fetchBooks = async () => {
        setLoading(true);
        try {
            // Added /books.json to the endpoint
            const response = await fetch(`${DB_URL}/books.json`);
            const json = await response.json();

            if (json) {
                const transformedBooks = Object.keys(json).map((key) => ({
                    id: key,
                    ...json[key],
                }));
                setBooks(transformedBooks);
            } else {
                setBooks([]);
            }
        } catch (error) {
            Alert.alert("Error fetching books", error.message);
        } finally {
            setLoading(false);
        }
    };

    // 2. Delete Logic
    const handleDelete = async (id) => {
        try {
            const url = `${DB_URL}/books/${id}.json`;
            const response = await fetch(url, { method: 'DELETE' });

            if (response.ok) {
                Alert.alert("Deleted!");
                fetchBooks(); // Now we can call this because it's in scope
            }
        } catch (error) {
            Alert.alert("Error", error.message);
        }
    };

    const confirmDelete = (id) => {
        Alert.alert("Delete Book", "Are you sure?", [
            { text: "Cancel", style: "cancel" },
            { text: "Delete", style: "destructive", onPress: () => handleDelete(id) }
        ]);
    };

    useEffect(() => {
        fetchBooks();
        const unsubscribe = navigation.addListener('focus', () => {
            fetchBooks();
        });
        return unsubscribe;
    }, [navigation]);

    // 3. Render Item (Moved inside Home or passed navigation/functions)
    const renderItem = ({ item }) => (
        <View style={styles.card}>
            <View style={styles.cardContent}>
                <Text style={styles.titleText}>{item.title}</Text>
                <Text style={styles.authorText}>by {item.author}</Text>

                <View style={styles.tag}>
                    <Text style={styles.tagText}>🏷️ {item.genre}</Text>
                </View>

                <View style={styles.actionRow}>
                    <TouchableOpacity
                        onPress={() => navigation.navigate("EditBook", { book: item })}
                        style={[styles.smallButton, { backgroundColor: '#5067FF' }]}>
                        <Text style={styles.btnText}>Edit</Text>
                    </TouchableOpacity>

                    <TouchableOpacity
                        onPress={() => confirmDelete(item.id)}
                        style={[styles.smallButton, { backgroundColor: '#ff5252' }]}>
                        <Text style={styles.btnText}>Delete</Text>
                    </TouchableOpacity>
                </View>
            </View>
        </View>
    );

    return (
        <View style={styles.container}>
            <FlatList
                data={books}
                keyExtractor={(item) => item.id}
                renderItem={renderItem}
                onRefresh={fetchBooks}
                refreshing={loading}
                ListEmptyComponent={
                    <Text style={styles.emptyText}>Nessun libro trovato</Text>
                }
            />
            <TouchableOpacity
                style={styles.fab}
                onPress={() => navigation.navigate("AddBook")}>
                <Text style={styles.fabText}>+</Text>
            </TouchableOpacity>
            <StatusBar barStyle="dark-content" backgroundColor="transparent" translucent={true} />
        </View>
    );
};

export default Home;

const styles = StyleSheet.create({
    container: { flex: 1, backgroundColor: "#f8f9fa" },
    card: {
        backgroundColor: "white",
        padding: 20,
        marginVertical: 10,
        marginHorizontal: 20,
        borderRadius: 20,
        elevation: 3,
        borderWidth: 1,
        borderColor: "#f0f0f0",
    },
    cardContent: { flexDirection: "column" },
    titleText: { fontSize: 18, fontWeight: "700", color: "#1a1a1a" },
    authorText: { fontSize: 14, color: "#6c757d", marginBottom: 12, fontStyle: "italic" },
    actionRow: { flexDirection: 'row', justifyContent: 'flex-end', gap: 10 },
    smallButton: { paddingHorizontal: 15, paddingVertical: 8, borderRadius: 10 },
    btnText: { color: 'white', fontWeight: 'bold', fontSize: 12 },
    emptyText: { textAlign: 'center', marginTop: 50, color: '#999' },
    fab: {
        position: "absolute",
        width: 60, height: 60,
        bottom: 30, right: 30,
        backgroundColor: "#5067FF",
        borderRadius: 30,
        justifyContent: "center",
        alignItems: "center",
        elevation: 8,
    },
    fabText: { color: "white", fontSize: 30 },
});