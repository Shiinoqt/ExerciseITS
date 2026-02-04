import { URL_BASE } from "./config.js";
import { Libro } from "./models/Libro.js";
import { listObject } from "./utils.js";

const URL_LIBRI = URL_BASE + "libri/";
async function leggiLibri() {
  const response = await fetch(URL_LIBRI + ".json");
  const dati = await response.json();
  const libri = listaOggetti(dati);
}

export async function aggiungiLibro(libro) {
  const response = await fetch(URL_LIBRI + ".json", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(libro),
  });
  const newLibro = await response.json();
  return newLibro;
  //const libri=listaOggetti(dati);
}
const form = document.querySelector("form");
form.addEventListener("submit", (e) => {
  e.preventDefault();
  const titolo = document.querySelector("input[name='titolo']");
  const autore = document.querySelector("#autore");
  const categoria = document.querySelector("#categoria");
  const newLibro = new Libro({
    titolo: titolo.value,
    autore: autore.value,
    categoria: categoria.value,
  });
  aggiungiLibro(newLibro).then(ris=>{
    console.log(ris)
    document.getElementById("result").innerHTML="Libro inserito correttamente "+ris.name
});
  titolo.value=""
  autore.value=""
  categoria.value=""
});