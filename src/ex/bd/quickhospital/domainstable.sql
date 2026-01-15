create domain Stringa as varchar;

create domain Email as varchar(255)
    check (value ~ '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$');

create domain Telefono as varchar(15)
    check (value ~ '^\+?[0-9]{7,15}$');

create domain int1_8 as integer
    check (value >= 1 and value <= 8);

create domain via as Stringa
    check (value is not null);

create domain civico as Stringa
    check (value is not null);

create type Indirizzo as (
    via via,
    civico civico
);