-- 1
select nome
from progetto p
where p.fine > '2023-12-31';

-- 2
select posizione, count(*) as persone
from persona
group by posizione;

-- 3
select distinct p.id, p.nome
from persona p, assenza a
where p.id = a.persona and a.tipo = 'Malattia';

-- 4
select tipo, count(*)
from assenza
group by tipo;

-- 5
select max(stipendio)
from persona p
where p.posizione = 'Professore Ordinario';

-- 6
select ap.id, ap.tipo, ap.oredurata
from persona p, attivitaprogetto ap
where p.id = ap.persona and p.id = 1 and ap.progetto = 4
order by ap.oredurata desc;

-- 7
SELECT p.nome, p.cognome, a.tipo, count(*) as giorni_totali
from persona p, assenza a
where p.id = a.persona
group by p.nome, p.cognome, a.tipo;

-- 8
select p.id, p.nome, p.cognome
from persona p
where p.posizione = 'Professore Ordinario' and p.stipendio = (
    select max(stipendio) 
    from Persona 
    where posizione = 'Professore Ordinario'
);

-- 9
select sum(ap.oredurata) as ore_totali
from attivitaprogetto ap
where ap.persona = 3 and ap.oredurata <= 3;

-- 10
select p.id, p.nome
from persona p
where p.id not in (
    select a.persona
    from assenza a
    where a.tipo = 'Chiusura Universitaria'
); 