create type Strutturato as
    enum ('Ricercatore','Professore Associato','Professore Ordinario');

create type LavoroProgetto as 
    enum ('Ricerca e Sviluppo','Dimostrazione','Management','Altro');

create type LavoroNonProgettuale as 
    enum ('Didattica','Ricerca','Missione','Incontro Dipartimentale','Incontro Accademico','Altro');

create type CausaAssenza as 
    enum ('Chiusura Universitaria','Maternita','Malattia');

create domain PosInteger as integer 
    default 0 
    check (value >= 0);2

create domain StringaM as varchar(100);

create domain NumeroOre as integer
    default 0
    check (value >= 0 and value <= 8);

create domain Denaro as real
    default 0.0
    check (value >= 0.0);

create table Persona (
    id PosInteger not null,
    nome StringaM not null,
    cognome StringaM not null,
    posizione Strutturato not null,
    stipendio Denaro not null,
    primary key (id)
);

create table Progetto (
    id PosInteger not null,
    nome StringaM not null,
    ore NumeroOre not null,
    inizio date not null,
    fine date not null,
    budget Denaro not null,
    primary key (id),
    unique (nome),
    check (fine >= inizio)
);

create table WP (
    progetto PosInteger not null,
    id PosInteger not null,
    nome StringaM not null,
    inizio date not null,
    fine date not null,
    primary key (progetto, id),
    foreign key (progetto) references Progetto(id),
    unique (progetto, nome),
    check (fine >= inizio)
);

create table AttivitaProgetto (
    id PosInteger not null,
    persona PosInteger not null,
    progetto PosInteger not null,
    wp PosInteger not null,
    giorno date not null,
    tipo LavoroProgetto not null,
    oreDurata NumeroOre not null,
    primary key (id),
    foreign key (persona) references Persona(id),
    foreign key (progetto, wp) references WP(progetto, id)
);

create table AttivitaNonProgettuale (
    id PosInteger not null,
    persona PosInteger not null,
    tipo LavoroNonProgettuale not null,
    giorno date not null,
    oreDurata NumeroOre not null,
    primary key (id),
    foreign key (persona) references Persona(id)
);

create table Assenza (
    id PosInteger not null,
    persona PosInteger not null,
    tipo CausaAssenza not null,
    giorno date not null,
    primary key (id),
    foreign key (persona) references Persona(id),
    unique (persona, giorno)
);