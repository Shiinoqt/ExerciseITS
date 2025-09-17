create table posizionemilitare (
    nome stringa primary key
);

create table persona (
    cf codicefiscale primary key,
    nome stringa not null,
    cognome stringa not null,
    nascita date not null,
    maternita intgez,
    genere genere not null,
    pos_mil stringa,

    foreign key (pos_mil) 
        references posizionemilitare(nome),

    --  Per ogni p: Persona
    --      p.genere = 'Uomo' se e solo se esiste un link pos_mil che coinvolge p
    --      p.genere = 'Donna' se e solo se p.maternità ha valore

    check (
        (genere = 'M' ) = (pos_mil is not null)
    ),
    check (
        (genere = 'F' ) = (maternita is not null)
    )
);

create table studente (
    persona codicefiscale primary key,
    foreign key (persona) 
        references persona(cf),
    matricola intgz not null,
    unique (matricola)
);

create table impiegato (
    persona codicefiscale primary key,
    foreign key (persona) 
        references persona(cf),
    stipendio realgez not null,
    ruolo ruolo not null
);

create table responsabile (
    impiegato codicefiscale primary key,
    foreign key (impiegato) 
        references impiegato(persona)
);

create table progetto (
    id serial primary key,
    nome stringa not null
);

create table resp_prog (
    responsabile codicefiscale not null,
    progetto integer not null,
    
    primary key (responsabile, progetto),
    foreign key (responsabile) 
        references responsabile(impiegato),
    foreign key (progetto) 
        references progetto(id)
);


-- Vincoli non implementabili direttamente nello schema relazionale

-- [V.Impiegato.responsabile]
-- Per ogni i: Impiegato
-- se i partecipa a un link resp_isa_prog allora i.ruolo = 'Progettista'

insert into posizionemilitare(nome) values
('Non tenuto'),
('Obbiettore di coscienza'),
('Assolto'),
('Non assolto');

insert into persona(cf, nome, cognome, nascita, genere, pos_mil) values
('RSSMRA85M01H501U', 'Mario', 'Rossi', '1985-01-01', 'M', 'Assolto'),
('VRDLGI90C05F205X', 'Luigi', 'Verdi', '1990-03-05', 'M', 'Non tenuto');

insert into persona(cf, nome, cognome, nascita, genere, maternita) values
('BNCFNC92D41H501Y', 'Francesca', 'Bianchi', '1992-04-01', 'F', 4),
('NCRLDA95E41H501W', 'Lara', 'Neri', '1995-05-01', 'F', 0);

insert into studente(persona, matricola) values
('VRDLGI90C05F205X', 1),
('NCRLDA95E41H501W', 2);

insert into impiegato(persona, stipendio, ruolo) values
('RSSMRA85M01H501U', 45000, 'Direttore'),
('BNCFNC92D41H501Y', 33000, 'Progettista');

insert into responsabile(impiegato) values
('BNCFNC92D41H501Y');

insert into progetto(nome) values
('Phoenix'),
('Pegasus'),
('Manhattan'),
('ITiEsse');

insert into resp_prog(responsabile, progetto) values
('BNCFNC92D41H501Y', 3),
('BNCFNC92D41H501Y', 4);