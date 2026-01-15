create table Specie (
    n_scientifico Stringa not null,
    n_comune Stringa not null,

    primary key (n_scientifico)
);

create table AreaVerde (
    id serial not null,
    latitudine Latitudine not null,
    longitudine Longitudine not null,
    is_fruibile boolean not null,
    is_sensibile boolean,

    primary key (id),
    check (is_sensibile = false or is_fruibile = true)
);

create table SoggettoVerde (
    id serial not null,
    data_pianta date not null,
    specie Stringa not null, -- associazione a Specie
    area_verde integer not null, -- associazione a AreaVerde

    primary key (id),
    foreign key (specie)
        references Specie(n_scientifico),
    foreign key (area_verde)
        references AreaVerde(id)
);

create table Intervento (
    id serial not null,
    inizio timestamp not null,
    durata_prev IntGZ not null,
    priorità Priorità not null,
    area_verde integer not null,

    primary key (id),
    foreign key (area_verde)
        references AreaVerde(id)
);

create table InterventoAssegnato (
    intervento integer,
    fine timestamp,

    primary key (intervento),
    foreign key (intervento)
        references Intervento(id)

    -- (intervento) occorre in assegna (interventoass)
);

create table OperatoreVerde (
    cf CF not null,
    nome Stringa not null,
    cognome Stringa not null,
    inizio date not null,
    fine date,

    primary key (cf)
);

create table assegna (
    operatore CF not null,
    interventoass integer not null,
    istante timestamp not null,
1
    primary key (operatore, interventoass),
    foreign key (operatore)
        references OperatoreVerde(cf),
    foreign key (interventoass)
        references InterventoAssegnato(intervento)
);