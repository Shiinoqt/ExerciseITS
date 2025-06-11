const rootElement=document.querySelector("#root");

const root=ReactDOM.createRoot(rootElement);

const App=(props)=>{
    return (
        <main className="main">
            <h1>Primo componente</h1>
            {props.children}
        </main>
    )
}

const List=()=>{
    return (
        <ul>
            <li>Elemento 1</li>
            <li>Elemento 2</li>
            <li>Elemento 3</li>
            <li>Elemento 4</li>
            <li>Elemento 5</li>
        </ul>
    )
}


root.render(
    <>
        <App>
            <h2>Lista di elementi</h2>
            <List></List>            
        </App>
    </>
)