export class Libro{
    #available
    constructor(id = null, titolo, autore, categoria) {
        this.id = id;
        this.titolo = titolo;
        this.autore = autore;
        this.categoria = categoria;
        this.#available = true;
    }

    toggleAvailability() {
        this.#available = !this.#available;
    }
}