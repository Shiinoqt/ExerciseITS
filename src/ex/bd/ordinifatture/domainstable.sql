create domain Stringa as varchar;

create domain IntGZ as integer
    check (value>0);

create domain IntGEZ as integer
    check (value >=0);

create domain RealGEZ as real
    check (value >= 0);

create domain Aliquota as real
    check (value >= 0.0 and value <= 1.0);

create domain CAP as char(5)
    check (value ~ '^[0-9]{5}$');

create type Indirizzo as (
    via Stringa,
    civico IntGZ,
    cap CAP
);

create domain CodiceFiscale as char(16)
    check (value ~ '^[A-Z]{6}[0-9]{2}[A-Z][0-9]{2}[A-Z][0-9]{3}[A-Z]$');

create domain PartitaIVA as char(11)
    check (value ~ '^[0-9]{11}$');

create domain Email as varchar(255)
    check (value ~ '^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$');

create domain Telefono as varchar(15);

create type StatoOrdine as
    enum ('In preparazione', 'Inviato', 'Da saldare', 'Saldato');