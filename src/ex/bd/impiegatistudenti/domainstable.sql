create domain stringa as varchar;

create domain codicefiscale as char(16)
    check (value ~ '^[A-Z]{6}\d{2}[A-Z]\d{2}[A-Z]\d{3}[A-Z]$');

create domain realgez as real
    check (value >= 0);

create domain intgez as integer
    check (value >= 0);

create domain intgz as integer
    check (value > 0);

create type genere as 
    enum ('M', 'F');

create type ruolo as 
    enum ('Segretario','Direttore', 'Progettista');