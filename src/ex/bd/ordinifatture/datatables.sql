create table Nazione (
    nome Stringa primary key not null
);

create table Regione (
    nome Stringa not null,
    nazione Stringa not null,

    primary key (nome, nazione),
    foreign key (nazione)
        references Nazione(nome)
);

create table Citta (
    id serial not null,
    nome Stringa not null,
    regione Stringa not null,
    nazione Stringa not null,
    
    primary key (id),
    foreign key (regione, nazione) 
        references Regione(nome, nazione),
    unique (nome, regione, nazione)
);

create table Direttore (
    cf CodiceFiscale not null,
    nome Stringa not null,
    cognome Stringa not null,
    data_nascita date not null,
    anni_servizio IntGEZ not null,

    -- Accorpo la citta al direttore
    citta integer not null,

    primary key (cf),
    foreign key (citta) 
        references Citta(id)
);

create table Dipartimento (
    nome Stringa not null,
    indirizzo Indirizzo not null,
    direttore CodiceFiscale not null,

    -- Accorpo la citta al dipartimento
    citta integer not null,

    primary key (nome),
    foreign key (direttore) 
        references Direttore(cf),
    foreign key (citta) 
        references Citta(id)
);

create table Fornitore (
    id serial not null,
    ragione_sociale Stringa not null,
    partita_iva PartitaIVA not null,
    indirizzo Indirizzo not null,
    telefono Telefono not null,
    email Email not null,

    -- Accorpo la citta al fornitore
    citta integer not null,

    primary key (id),
    foreign key (citta) 
        references Citta(id)
);

create table Ordine (
    id serial not null,
    data_stipula date not null,
    imponibile RealGEZ not null,
    aliquota_iva Aliquota not null,
    stato StatoOrdine not null,

    -- Accorpo il fornitore all'ordine
    fornitore integer not null,
    
    -- Accorpo il dipartimento all'ordine
    dipartimento Stringa not null,

    primary key (id),
    foreign key (fornitore) 
        references Fornitore(id),
    foreign key (dipartimento)  
        references Dipartimento(nome)
);