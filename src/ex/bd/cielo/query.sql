-- 1
select v.codice codice_volo, c.nome compagnia
from compagnia c, volo v
where c.nome = v.comp
    and v.durataminuti >= 180;

-- 2
select distinct c.nome compagnia
from compagnia c, volo v
where c.nome = v.comp
    and v.durataminuti > 180;

-- 3
select v.codice codice_volo, v.comp compagnia
from volo v, arrpart ap
where v.codice = ap.codice 
    and v.comp = ap.comp
    and ap.partenza = 'CIA';

-- 4
select distinct c.nome compagnia
from compagnia c, arrpart ap
where c.nome = ap.comp
    and ap.arrivo = 'FCO';

-- 5 
select v.codice codice_volo, v.comp compagnia
from volo v, arrpart ap
where v.codice = ap.codice 
	and v.comp = ap.comp
	and ap.partenza = 'FCO'
  	and ap.arrivo = 'JFK';

-- 6
select distinct c.nome compagnia
from compagnia c, arrpart ap
where c.nome = ap.comp
	and ap.partenza = 'FCO'
	and ap.arrivo = 'JFK';

-- 7
select distinct c.nome compagnia
from compagnia c, arrpart ap, luogoaeroporto la, luogoaeroporto lp
where ap.comp = c.nome
	and lp.aeroporto = ap.partenza
	and la.aeroporto = ap.arrivo
	and lp.citta = 'Roma'
	and la.citta = 'New York';

-- 8 
select a.codice codiceiata, a.nome, la.citta
from aeroporto a, luogoaeroporto la, arrpart ap
where a.codice = la.aeroporto 
	and a.codice = ap.partenza
	and ap.comp = 'MagicFly'

-- 9
select ap.codice codice_volo, ap.comp compagnia, ap.partenza, ap.arrivo
from arrpart ap, luogoaeroporto lp, luogoaeroporto la
where ap.partenza = lp.aeroporto 
	and ap.arrivo = la.aeroporto
	and lp.citta = 'Roma'
	and la.citta = 'New York'

-- 10
select ap1.comp compagnia, ap1.codice codice_volo_1, ap1.partenza partenza, ap1.arrivo scalo, ap2.codice codice_volo_2, ap2.arrivo arrivo
from arrpart ap1, arrpart ap2, luogoaeroporto lp, luogoaeroporto la
where ap1.comp = ap2.comp
    and ap1.arrivo = ap2.partenza
    and ap1.partenza = lp.aeroporto
    and ap2.arrivo = la.aeroporto
    and lp.citta = 'Roma'
    and la.citta = 'New York';

-- 11
select c.nome
from compagnia c, arrpart ap
where c.nome = ap.comp
	and ap.partenza = 'FCO'
	and ap.arrivo = 'JFK'
	and c.annofondaz is not null;
	
