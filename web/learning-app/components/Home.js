import { useNavigation } from "@react-navigation/native";
import { collection, onSnapshot } from "firebase/firestore";
import React, { useState, useEffect } from "react";
import {
    FlatList,
    StyleSheet,
    Text,
    TouchableOpacity,
    View,
    StatusBar
} from "react-native";
import { db } from "../firebaseConfig";

const renderItem = ({ item }) => (
    <View style={styles.card}>
        <View style={styles.cardContent}>
            <Text style={styles.titleText}>{item.title}</Text>
            <Text style={styles.authorText}>by {item.author}</Text>

            <View style={styles.tag}>
                <Text style={styles.tagText}>🏷️ {item.genre}</Text>
            </View>
        </View>
    </View>
);

const Home = () => {
    const navigation = useNavigation();
    const [books, setBooks] = useState([]);

    useEffect(() => {
        const unsubscribe = onSnapshot(collection(db, "books"), (snapshot) => {
            const books = snapshot.docs.map((doc) => ({
                id: doc.id,
                ...doc.data(),
            }));
            setBooks(books);
        });

        return () => unsubscribe();
    }, []);

    return (
        <View style={styles.container}>
            <FlatList
                data={books}
                keyExtractor={(item) => item.id}
                renderItem={renderItem}
                ListEmptyComponent={
                    <Text style={styles.emptyText}> Nessun libro trovato</Text>
                } />
            <TouchableOpacity
                style={styles.fab}
                onPress={() => navigation.navigate("AddBook")}>
                <Text style={styles.fabText}>+</Text>
            </TouchableOpacity>
            <StatusBar
                barStyle="dark-content" // Options: 'light-content', 'dark-content', 'default'
                backgroundColor="transparent"
                translucent={true}
            />
        </View>
    )
}

export default Home

const styles = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: "#f8f9fa" // Soft off-white background makes white cards pop
    },
    card: {
        top: 10,
        backgroundColor: "white",
        padding: 20,
        marginVertical: 10,
        marginHorizontal: 20,
        borderRadius: 20,
        // Softer, more modern shadow
        shadowColor: "#000",
        shadowOffset: { width: 0, height: 4 },
        shadowOpacity: 0.05,
        shadowRadius: 10,
        elevation: 3,
        borderWidth: 1,
        borderColor: "#f0f0f0", // Subtle border for definition
    },
    cardContent: {
        flexDirection: "column",
    },
    titleText: {
        fontSize: 18,
        fontWeight: "700",
        color: "#1a1a1a",
        marginBottom: 4,
    },
    authorText: {
        fontSize: 14,
        color: "#6c757d",
        marginBottom: 12,
        fontStyle: "italic",
    },
    tag: {
        backgroundColor: "#e9ecef",
        paddingHorizontal: 10,
        paddingVertical: 4,
        borderRadius: 8,
        alignSelf: "flex-start", // Keeps the background tight around text
    },
    tagText: {
        fontSize: 12,
        fontWeight: "600",
        color: "#495057",
        textTransform: "uppercase",
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
    fabText: { color: "white", fontSize: 30 },
});