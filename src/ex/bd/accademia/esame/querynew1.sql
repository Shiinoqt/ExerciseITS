-- Quanti Work Package (WP) sono stati definiti per ogni progetto? (Si richiede il nome del progetto e il numero di WP).
select p.nome, count(*)
from progetto p, wp
where p.id = wp.progetto
group by p.nome;

-- Qual è lo stipendio medio dei Professori Ordinari?.
select round(avg(stipendio)) as media
from persona p
where p.posizione = 'Professore Ordinario';

-- Qual è il budget totale di tutti i progetti che sono iniziati dopo il 1° gennaio 2020?.
select sum(budget) as budget_totale
from progetto p
where p.inizio >= '2020-01-01';

-- Quante ore totali di attività non progettuale di tipo 'Ricerca' ha svolto ogni singola persona? (Si richiede id, nome, cognome e somma delle ore).
select p.id, p.nome, p.cognome, sum(oredurata) as ore_totali
from persona p, attivitanonprogettuale anp
where p.id = anp.persona and anp.tipo = 'Ricerca'
group by p.id, p.nome, p.cognome;

-- Quali sono i nomi dei progetti che hanno un budget complessivo superiore a 100.000?.
select pr.nome
from progetto pr
where pr.budget > 100000;

-- Qual è il numero totale di ore dedicate ad attività di progetto da ogni Ricercatore? (Si richiede id, nome, cognome e totale ore).
select p.id, p.nome, p.cognome, sum(oredurata) as ore_totali
from persona p, attivitaprogetto ap
where p.id = ap.progetto
group by p.id, p.nome, p.cognome;

-- Quante assenze per 'Malattia' ha effettuato ogni dipendente? (Si richiede nome, cognome e numero di assenze).
select p.nome, p.cognome, count(*) as assenze
from persona p, assenza a
where p.id = a.persona and a.tipo = 'Malattia'
group by p.nome, p.cognome;

-- Qual è la durata media, massima e minima delle singole attività di progetto svolte nel Work Package 'Management' del progetto 'Pegasus'?.
select avg(oredurata), max(oredurata), min(oredurata)
from attivitaprogetto ap, wp, progetto p
where p.nome = 'Pegasus'
    and wp.nome = 'Management'
    and wp.id = ap.wp
    and ap.progetto = p.id
    and ap.progetto = wp.progetto;

-- Quali sono i dipendenti (id, nome, cognome) che hanno lavorato su più di tre Work Package (WP) distinti?. ???
SELECT p.id, p.nome, p.cognome
FROM Persona p, AttivitaProgetto ap
WHERE p.id = ap.persona
GROUP BY p.id, p.nome, p.cognome
HAVING COUNT(DISTINCT (ap.progetto, ap.wp)) > 3;

-- Per ogni posizione (Ricercatore, Associato, Ordinario), qual è lo stipendio massimo e minimo percepito?.
select distinct(p.posizione), max(stipendio), min(stipendio)
from persona p
group by p.posizione;

-- Quali sono i nomi dei progetti che coinvolgono più di cinque persone diverse?.
SELECT pr.nome
FROM Progetto pr, AttivitaProgetto ap
WHERE pr.id = ap.progetto
GROUP BY pr.id, pr.nome
HAVING COUNT(DISTINCT ap.persona) > 5;

-- Qual è il numero totale di ore di 'Didattica' svolte dai Professori Associati che hanno uno stipendio superiore a 35.000?.
select sum(anp.oredurata) as ore_totali
from attivitanonprogettuale anp, persona p
where p.id = anp.persona 
    and p.posizione = 'Professore Associato' 
    and anp.tipo = 'Didattica'
    and p.stipendio > 350000;
