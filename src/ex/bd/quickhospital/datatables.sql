create table Persona (
    id serial primary key,
    nome Stringa not null,
    cognome Stringa not null,
    nascita date not null
);



create table Medico (
    -- associazione 1:1 con Persona
    persona integer primary key,

    foreign key (persona) 
        references Persona(id)
);

create table SpecializzazioneSecondaria (
    nome Stringa primary key
);

create table MedicoSpecializzazione (
    medico integer not null,
    specializzazione Stringa not null,

    primary key (medico, specializzazione),

    foreign key (medico)
        references Medico(persona),
    foreign key (specializzazione)
        references SpecializzazioneSecondaria(nome)
);

create table Paziente (
    email Email not null,
    indirizzo Indirizzo not null,

    -- associazione 1:1 con Persona
    persona integer primary key,

    foreign key (persona) 
        references Persona(id),

    unique (email, indirizzo)
);

create table Telefono (
    numero Telefono primary key
);

-- associazione N:M tra Paziente e Telefono 1..*
create table TelefonoPaziente (
    paziente integer not null,
    numero Telefono not null,

    primary key (paziente, numero),
    foreign key (paziente)
        references Paziente(persona),
    foreign key (numero)
        references Telefono(numero)
);

create table Stanza (
    id serial primary key,
    piano integer not null,
    settore integer not null
);

create table Letto (
    numero int1_8 not null,
    stanza integer not null,

    primary key (numero, stanza),

    foreign key (stanza)
        references Stanza(id)
);


create table Ricovero (
    id serial primary key,
    inizio timestamp not null,
    dimissione timestamp,
    paziente integer not null,
    medico integer not null,
    numero_letto int1_8 not null,
    stanza integer not null,

    check (dimissione is null or dimissione > inizio),

    foreign key (paziente)
        references Paziente(persona),
    foreign key (medico)
        references Medico(persona),
    foreign key (numero_letto, stanza)
        references Letto(numero, stanza),

    -- Impdedisce di avere due ricoveri contemporanei nello stesso letto
    -- unique (numero_letto, stanza, inizio)
);

create table PazienteEsterno (
    paziente integer primary key,
  
    foreign key (paziente)
        references Paziente(persona)
);

create table PrestazioneEsterna (
    id serial primary key,
    datarichiesta timestamp not null,
    descrizione Stringa not null,

    -- associazione 1:1 con Medico
    medico integer not null,

    -- associazione 1:1 con PazienteEsterno
    pazienteesterno integer not null,

    foreign key (pazienteesterno)
        references PazienteEsterno(paziente),
    foreign key (medico)
        references Medico(persona),

    unique (medico, pazienteesterno)
);

