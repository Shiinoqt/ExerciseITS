create type Strutturato as
    enum ('Ricercatore','Professore Associato','Professore Ordinario');

create type LavoroProgetto as 
    enum ('Ricerca e Sviluppo','Dimostrazione','Management','Altro');

create type LavoroNonProgettuale as 
    enum ('Didattica','Ricerca','Missione','Incontro Dipartimentale','Incontro Accademico','Altro');

create type CausaAssenza as 
    enum ('Chiusura Universitaria','Maternita','Malattia');

create domain PosInteger as integer 
    default 0 
    check (value >= 0);2

create domain StringaM as varchar(100);

create domain NumeroOre as integer
    default 0
    check (value >= 0 and value <= 8);

create domain Denaro as real
    default 0.0
    check (value >= 0.0);