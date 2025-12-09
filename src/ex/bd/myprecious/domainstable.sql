create domain stringa as varchar;

create domain realgez as real
    check (value >= 0);

create domain intgz as integer
    check (value > 0);