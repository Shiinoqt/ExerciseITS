--1
select a.codice, a.nome, count(distinct comp) 
from aeroporto a, arrpart ap
where ap.partenza = a.codice 
	or ap.arrivo = a.codice
group by a.codice;

--2
select count(*) numero_voli
from volo v, arrpart ap
where v.codice = ap.codice
	and ap.partenza = 'HTR'
	and v.durataminuti >= 100;

--3
select la.nazione, count(distinct la.aeroporto) num_aeroporti
from arrpart ap, luogoaeroporto la
where ap.comp = 'Apitalia'
	and la.aeroporto = ap.arrivo
	or la.aeroporto = ap.partenza
group by la.nazione
order by la.nazione;

--4 
select avg(v.durataminuti) media, min(v.durataminuti) minimo, max(v.durataminuti) massimo
from volo v
where v.comp = 'MagicFly';

--5
select a.codice, a.nome, max(c.annoFondaz)
from aeroporto a, compagnia c, arrpart ap
where c.nome = ap.comp
  and (a.codice = ap.arrivo OR a.codice = ap.partenza)
group by a.codice, a.nome
order by a.codice;

--6

--7
select a.codice, a.nome, avg(v.durataminuti) durata_media
from aeroporto a, arrpart ap, volo v
where a.codice = ap.partenza
  and ap.codice = v.codice 
  AND ap.comp = v.comp
group by a.codice, a.nome
order by a.codice;

--8
select c.nome, sum(v.durataminuti) durata_tot
from compagnia c, volo v
where v.comp = c.nome 
	and c.annoFondaz >= 1950
group by c.nome
order by c.nome;

--9
select a.codice, a.nome
from aeroporto a, arrpart ap
where a.codice = ap.arrivo 
   or a.codice = ap.partenza
group by a.codice, a.nome
having count(distinct ap.comp) = 2
order by a.codice;

--10
select la.citta
from luogoaeroporto la
group by la.citta
having count(*) >= 2
order by la.citta;

--11
select c.nome
from compagnia c, volo v
where c.nome = v.comp
group by c.nome
having avg(v.durataminuti) > 360
order by c.nome;

--12
select c.nome
from compagnia c, volo v
where c.nome = v.comp
group by c.nome
having min(v.durataminuti) > 100
order by c.nome;