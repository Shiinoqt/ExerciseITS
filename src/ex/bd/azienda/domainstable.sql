create domain Stringa as varchar;

create domain Telefono as varchar(15);

create domain IntGEZ as integer
    check (value >= 0);

create domain IntGZ as integer
    check (value > 0);

create domain RealGEZ as real
    check (value >= 0);

create domain CAP as char(5)
    check (value ~ '^[0-9]{5}$');

create type Indirizzo as (
    via Stringa,
    cap CAP,
    civico IntGZ2
);