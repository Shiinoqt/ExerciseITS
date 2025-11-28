const rootDiv = document.getElementById("root");
const root = ReactDOM.createRoot(rootDiv);
// function App() {
//   const h1 = React.createElement(
//     "h1",
//     {
//       key: "h1",
//       style: { color: "green" },
//       onClick: (e) => console.log(e),
//     },
//     "Ciao sono un H1"
//   );

//   const ul = React.createElement("ul", { key: "ul" }, [
//     React.createElement("li", { key: "php" }, "PHP"),
//     React.createElement("li", { key: "js" }, "JS"),
//     React.createElement("li", { key: "html" }, "HTML"),
//   ]);

//   const main = React.createElement(1
//     "main",
//     { className: "main" },
//     [h1, ul]
//   );

//   return main;
// }

const App = (props) => {
  return (
    <>
      {props.children}
    </>
  );
}

function List() {
  return (
    <ul>
      <li>PHP</li>
      <li>JS</li>
      <li>HTML</li>
    </ul>
  );
}

root.render(
  <>
    <App>
      <List></List>
    </App>
  </>
);