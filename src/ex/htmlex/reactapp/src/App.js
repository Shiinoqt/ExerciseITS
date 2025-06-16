import './App.css';
import Componente1 from './Componente1';


function getDate() {
  return new Date().toLocaleDateString() + " " + new Date().toLocaleTimeString();
}

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <Componente1/>
        <img src="https://media.licdn.com/dms/image/v2/D4D03AQFQ73Lcq0DEBQ/profile-displayphoto-shrink_800_800/B4DZXKdTPAG4Ac-/0/1742858435677?e=1755129600&v=beta&t=v4E2ZGu13iZ-zCjDXKhDF-hBGaBdZzQ5AEsPvWHSqY8" className="App-logo" alt="logo" />
        <h2>
          {
            getDate()
          }
        </h2>
        <p>learn how to sybau!</p>
      </header>
    </div>
  );
}

export default App;
