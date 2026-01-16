import { Button } from '@react-navigation/elements';
import { View, Text } from 'react-native';

export default function HomeScreen({ navigation }) {
    return (
        <View>
            <Text>Home Screen</Text>
            <Button title ="Go to Details" onPress={() => navigation.navigate('Details')} />
        </View>
    )
}