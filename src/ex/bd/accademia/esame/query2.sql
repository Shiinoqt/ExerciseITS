-- 1
select nome, cognome, stipendio
from persona p
where p.stipendio <= 40000;

-- 2
select distinct nome, cognome, stipendio
from persona p, attivitaprogetto ap
where p.id = ap.persona and p.stipendio <= 40000 and p.posizione = 'Ricercatore';

-- 3
select sum(budget) as budget_totale
from progetto;

-- 4 ??
select p.nome, p.cognome, SUM(pr.budget) AS budget_totale
from persona p, progetto pr, (select distinct persona, progetto from attivitaprogetto) ap
where p.id = ap.persona and ap.progetto = pr.id
group by p.id, p.nome, p.cognome;

-- 5
select p.nome, p.cognome, count(distinct AP.progetto) as NumeroProgetti
from persona p, attivitaprogetto ap
where p.id = ap.persona and p.posizione = 'Professore Ordinario'
group by p.id, p.nome, p.cognome;

-- 6
select p.nome, p.cognome, count(*) as NumeroAssenze 
from persona p, assenza a 
where p.id = a.persona and p.posizione = 'Professore Associato' and a.tipo = 'Malattia' 
group by p.id, p.nome, p.cognome;

-- 7 
select p.nome, p.cognome, sum(ap.oreDurata) as TotaleOre 
from persona p, attivitaprogetto ap 
where p.id = ap.persona and ap.progetto = 5 
group by p.id, p.nome, p.cognome;

-- 8 
select p.nome, p.cognome, avg(ap.oreDurata) as MediaOre 
from persona p, attivitaprogetto ap 
where p.id = ap.persona 
group by p.id, p.nome, p.cognome;

-- 9 
select p.nome, p.cognome, sum(anp.oreDurata) as TotaleOreDidattica 
from persona p, attivitanonprogettuale anp 
where p.id = anp.persona and anp.tipo = 'Didattica' 
group by p.id, p.nome, p.cognome;

-- 10 
select p.nome, p.cognome, sum(ap.oreDurata) as TotaleOreWP 
from persona p, attivitaprogetto ap 
where p.id = ap.persona and ap.progetto = 3 and ap.wp = 5 
group by p.id, p.nome, p.cognome;