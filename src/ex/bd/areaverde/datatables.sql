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
    check (not is_fruibile or is_sensibile is not null)
);

create table SoggettoVerde (
    id serial not null,
    data_pianta date not null,
    specie Stringa not null,
    area_verde integer not null,

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

