-- 1
select nome
from persona p, impiegato i
where p.cf = i.persona and p.nascita >= '1965-01-01';

-- 2
select nome
from progetto;

-- 3
select stipendio
from impiegato i
where ruolo = 'Direttore';

-- 4 
select count(*)
from impiegato i
where ruolo = 'Progettista';

-- 5
select count(*)
from responsabile;

-- 6
select count(*)
from impiegato i
where i.ruolo = 'Progettista' 
    and i.persona not in (select impiegato from responsabile);

-- 7
select avg(stipendio)
from impiegato
where ruolo = 'Segretario';

-- 8
select max(extract(year from age(p.nascita))) as eta_massima
from studente s, persona p
where s.persona = p.cf;

select max(date_part('year', age(current_date, p.nascita))) as eta
from studente s, persona p
where s.persona = p.cf;

-- 9
select count(*)
from persona p, impiegato i
where p.cf = i.persona and p.pos_mil = 'Assolto' and i.ruolo = 'Direttore';

-- 10
select count(*)
from resp_prog rp, responsabile r, impiegato i, persona p
where rp.responsabile = r.impiegato
    and r.impiegato = i.persona
    and i.persona = p.cf
    and p.genere = 'F'
    and p.maternita >= 2;