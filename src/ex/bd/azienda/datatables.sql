create table Impiegato (
    id serial not null primary key,
    nome Stringa not null,
    cognome Stringa not null,
    nascita date not null,
    stipendio RealGZ not null,
    dipartimento_aff integer,
    data_aff date not null,

    -- foreign key (dipartimento_aff) 
        -- references Dipartimento(id), posticipato

    check (
        (dipartimento_aff is null) =
        (data_aff is null)
        )
    
);

create table Dipartimento (
    id serial not null primary key,
    nome Stringa not null,
    indirizzo indirizzo
    -- v. incl (id)
    -- appare in dip_tel(dipartimento) 1..*
    direttore integer not null,
    foreign key (direttore) 
        references Impiegato(id)

);

create table Afferenza (
    impiegato integer not null,
    dipartimento integer not null,
    data_aff date not null,

    primary key (impiegato), -- questo è per ..1

    foreign key (impiegato) 
        references Impiegato(id),
    foreign key (dipartimento)
        references Dipartimento(id)
);

create table direzione (
    impiegato integer not null,
    dipartimento integer not null,

    primary key (dipartimento), -- questo è per ..1

    foreign key (impiegato) 
        references Impiegato(id),
    foreign key (dipartimento)
        references Dipartimento(id)

    -- v. incl (dipartimento, impiegato) 1..1
    -- appare in direzione(dipartimento)
);


create table Telefono (
    telefono Telefono primary key
    -- v. incl (telefono)
    -- appare in dip_tel(telefono) 1..*
);

create table dip_tel (
    dipartimento integer not null,
    telefono stringa not null,
    primary key (dipartimento, telefono),
    foreign key (dipartimento) 
        references Dipartimento(id),
    foreign key (telefono) 
        references Telefono(telefono)
);

create table Progetto (
    id serial primary key,
    nome Stringa not null,
    budget RealGEZ not null
);

create table coinvolto (
    impiegato integer not null,
    progetto integer not null,

    primary key (impiegato, progetto),
    
    foreign key (impiegato) 
        references Impiegato(id),
    foreign key (progetto) 
        references Progetto(id)
)

alter table impiegato
    add foreign key (dipartimento_aff) 
        references Dipartimento(id);