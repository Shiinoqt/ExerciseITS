-- 1
select distinct cognome
from persona;

-- 2
select id, nome, cognome
from persona
where posizione = 'Ricercatore';

-- 3
select id, nome, cognome
from persona p
where posizione = 'Professore Associato' and cognome like 'V%';

-- 4
select id, nome, cognome
from persona 
where (posizione = 'Professore Associato' 
	or posizione = 'Professore Ordinario')
	and cognome like 'V%';

-- 5
select id, nome, inizio, fine, budget
from progetto 
where fine >= inizio

-- 6
select id, nome
from progetto 
order by inizio asc;

-- 7
select id, nome 
from wp 
order by nome asc;

-- 8
select distinct tipo
from assenza;

-- 9
select distinct tipo
from attivitaprogetto;

-- 10
select distinct giorno
from attivitanonprogettuale
where tipo = 'Didattica'
order by giorno asc;