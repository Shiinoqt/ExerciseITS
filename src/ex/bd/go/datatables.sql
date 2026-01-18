create type Stringa as varchar(100);

create type indirizzo as (
    via varchar,
    civico integer
);

create domain IntGEZ as integer
    check (value >= 0);

create domain IntGZ as integer
    check (value > 0);

create domain Reale_0_10 as real
    check (value >= 0 and value <= 10);

create type Colore as enum (
    'Bianco','Nero'
);

create table nazione (
    nome varchar primary key
);

create table regione (
    nome varchar not null,
    -- Accorpo la nazione alla regione
    nazione varchar not null,
    foreign key (nazione) 
        references nazione(nome),
    primary key (nome, nazione)
);

create table citta (
    id integer primary key,
    nome varchar not null,
    regione varchar not null,
    nazione varchar not null,

    foreign key (regione, nazione) 
        references regione(nome, nazione),
    unique (nome, regione, nazione)
);

create table giocatore (
    nickname varchar primary key,
    nome varchar not null,
    cognome varchar not null,
    indirizzo indirizzo not null,
    rank IntGZ not null,

    -- Accorpo la citta al giocatore
    citta integer not null,
    foreign key (citta) 
        references citta(id)
);

create table regole (
    nome varchar primary key
);

create table torneo (
    id integer primary key,
    nome varchar not null,
    descrizione varchar not null,
    edizione integer not null
);

create table partita (
    id integer primary key,
    data date not null,
    indirizzo indirizzo not null,
    komi Reale_0_10 not null,

    -- Accorpo citta
    citta integer not null,
    foreign key (citta)
        references citta(id),

    -- Accorpo segue
    regole varchar not null,
    foreign key (regole) 
        references regole(nome),

    -- Accorpo part torneo
    torneo integer not null,
    foreign key (torneo) 
        references torneo(id),

    -- Accorpo bianco 
    bianco varchar not null,
    foreign key (bianco) 
        references giocatore(nickname),

    nero varchar not null,
    foreign key (nero)
        references giocatore(nickname),

    check (bianco <> nero)
);

create table partitaconrinuncia (
    partita integer primary key,
    rinunciatario Colore not null,

    foreign key (partita)
        references partita(id)
);

create table partitaconpunteggio (
    partita integer primary key,
    punteggio_bianco IntGEZ not null,
    punteggio_nero IntGEZ not null,

    foreign key (partita)
        references partita(id)
);