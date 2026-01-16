import { View, Text } from 'react-native';
import { Button } from '@react-navigation/elements';

export default function DetailScreen({ navigation }) {
    return (
        <View>
            <Text>Detail Screen</Text>
            <Button title= "Go back" onPress={() => navigation.goBack()} />
        </View>
    )
}