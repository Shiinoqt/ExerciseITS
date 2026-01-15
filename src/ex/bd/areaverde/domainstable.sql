create domain CF as varchar(16)
    check(value ~ '^[A-Z0-9]{16}$');

create domain Stringa as varchar;

create domain IntGZ as integer
    check (value>0);

create domain Latitudine as real
    check (value >= -90.0 and value <= 90.0);

create domain Longitudine as real
    check (value >= -180.0 and value <= 180.0);

create domain Priorità as integer
    check (value >= 1 and value <= 10);