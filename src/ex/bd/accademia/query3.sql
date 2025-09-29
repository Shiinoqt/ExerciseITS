--1 
select posizione, count(*)
from persona
group by posizione;

--2
select count(*)
from persona
where stipendio >= 40000

--3
select count(*)
from progetto
where budget > 50000
	and fine <= 'current_date'; 

--4 
select avg(oredurata) as media, max(oredurata) as massimo, min(oredurata) as minimo
from progetto p, attivitaprogetto ap
where ap.progetto = p.id 
	and p.nome = 'Pegasus';

--5
select p.id, p.nome, avg(oredurata) as media, max(oredurata) as massimo, min(oredurata) as minimo
from persona p, progetto pr, attivitaprogetto ap
where ap.progetto = pr.id
	and p.id = ap.persona
	and pr.nome = 'Pegasus'
group by p.id;

--6
select p.id, p.nome, p.cognome, sum(oredurata) as totale
from attivitanonprogettuale anp, persona p
where anp.persona = p.id
	and anp.tipo = 'Didattica'
group by p.id;

--7
select avg(stipendio) as media, max(stipendio) as massimo, min(stipendio) as minimo
from persona p
where p.posizione = 'Ricercatore';
 
--8
select posizione, avg(stipendio) as media, max(stipendio) as massimo, min(stipendio) as minimo
from persona p
where p.posizione = 'Ricercatore'
    or p.posizione = 'Professore Associato'
    or p.posizione = 'Professore Ordinario'
group by posizione;

--9
select pr.id, pr.nome, sum(oredurata) as oretotali
from persona p, attivitaprogetto ap, progetto pr
where p.id = ap.persona
    and pr.id = ap.progetto
	and p.nome = 'Ginevra'
	and p.cognome = 'Riva'
group by pr.id, pr.nome;

-- 10
select pr.nome as progetto
from progetto pr, attivitaprogetto ap
where pr.id = ap.progetto
group by pr.nome
having count(distinct ap.persona) >= 2;

--11
select p.id, p.nome, p.cognome 
from persona p, attivitaprogetto ap
where p.id = ap.persona
	and p.posizione = 'Professore Associato'
group by p.id, p.nome, p.cognome
having count(distinct ap.progetto) > 1;