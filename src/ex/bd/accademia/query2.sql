-- 1
select wp.id, wp.nome, wp.inizio, wp.fine
from wp, progetto p
where p.id = wp.progetto 
    and p.nome = 'Pegasus';

-- 2
select distinct p.id, p.nome, p.cognome, p.posizione
from persona p, attivitaprogetto ap, progetto pr
where p.id = ap.persona
    and ap.progetto = pr.id
    and pr.nome = 'Pegasus'
order by p.cognome desc;

-- 3
select p.id, p.nome, p.cognome, p.posizione
from persona p, attivitaprogetto ap, progetto pr
where p.id = ap.persona
    and ap.progetto = pr.id
    and pr.nome = 'Pegasus'
group by p.id, p.nome, p.cognome, p.posizione
having count(*) > 1;

-- 4
select p.id, p.nome, p.cognome
from persona p, assenza a
where p.id = a.persona
    and p.posizione = 'Professore Ordinario'
    and a.tipo = 'Malattia'
group by p.id, p.nome, p.cognome
having count(*) > 1;

-- 5
select p.id, p.nome, p.cognome
from persona p, assenza a
where p.id = a.persona
    and a.tipo = 'Malattia'
group by p.id, p.nome, p.cognome
having count(*) > 1;

-- 6
select distinct p.id, p.nome, p.cognome
from persona p, attivitanonprogettuale anp
where p.id = anp.persona
	and p.posizione = 'Ricercatore'
    and anp.tipo = 'Didattica';

-- 7
select p.id, p.nome, p.cognome
from persona p, attivitanonprogettuale anp
where p.id = anp.persona
	and p.posizione = 'Ricercatore'
    and anp.tipo = 'Didattica'
group by p.id, p.nome, p.cognome
having count(*)>1;

-- 8
select p.id, p.nome, p.cognome
from persona p, attivitaprogetto ap, attivitanonprogettuale anp
where p.id = ap.persona
    and p.id = anp.persona
    and ap.giorno = anp.giorno;

-- 9 
select p.id, p.nome, p.cognome, ap.giorno, 
from persona p, attivitaprogetto ap, attivitanonprogettuale anp, progetto pr
where p.id = ap.persona
    and p.id = anp.persona
    and ap.giorno = anp.giorno;