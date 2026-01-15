-- 1. Gli operatori devono
-- poter calcolare l’insieme delle aree verdi fruibili che hanno almeno un soggetto verde
-- della specie 'Pinus pinea' e piantata almeno 5 anni fa.

select distinct a.id
from AreaVerde a, SoggettoVerde s
where a.is_fruibile = true
  and s.specie = 'Pinus pinea'
  and s.data_pianta <= current_date - interval '5 years'
  and s.area_verde = a.id;


-- 2. Il management deve poter calcolare, l’insieme delle aree verdi sensibili che non sono state 
-- oggetto di alcun intervento
-- nel periodo '2023-10-9' - '2023-10-13'

SELECT *
FROM AreaVerde a
WHERE a.is_sensibile = true
  AND NOT EXISTS (
      SELECT 1
      FROM Intervento i
      WHERE i.area_verde = a.id
        AND i.inizio >= TIMESTAMP '2023-10-09'
        AND i.inizio <  TIMESTAMP '2023-10-13'
  );


-- 3. I dipendenti
-- comunali devono poter ottenere dal sistema gli operatori ai quali è stato assegnato il
-- minor numero di interventi con priorità maggiore o uguale a 5 nell'anno 2023.

-- SOLUZIONE QUERY 3

WITH
n_int_per_oper AS (
    select o.cf, o.nome, o.cognome, count(*) num_interv
    from operatore o, intervento i, assegna a
    where
        a.operatore = o.cf
        and a.interventoassegnato = i.id
        and i.priorita >= 5
        and extract(year from a.istante) = 2023
    group by o.cf),
n_min_interv as (
    select min(num_interv) as n_min
    from n_int_per_oper
)
select *
from n_int_per_oper t1, n_min_interv t2
where t1.num_interv = t2.n_min;

-- 4. restituire tutte le aree verdi con almeno 10 soggetti verdi
select *
from AreaVerde a
where (
    select count(*)
    from SoggettoVerde s
    where s.area_verde = a.id
) >= 10;


-- 5. il numero di operatori che sono stati assegnati almeno una volta ad interventi con priorità < 4
select count(distinct a.operatore) as num_operatori
from assegna a, intervento i
where a.interventoass = i.id
  and i.priorità < 4;

-- 6. la durata prevista media e la durata effettiva media degli interventi completati.
select avg(i.durata_prev) as durata_prev_media,
       avg(extract(epoch from (ia.fine - i.inizio)) / 60) as durata_eff_media
from intervento i, interventoassegnato ia
where i.id = ia.intervento
  and ia.fine is not null;

-- 7. gli operatori assegnati all'intervento più lungo
select o.cf, o.nome, o.cognome
from operatoreverde o, assegna a, intervento i
where a.operatore = o.cf
  and a.interventoass = i.id
  and i.durata_prev = (
      select max(durata_prev)
      from intervento
  );

-- 8. il numero degli interventi non terminati assegnati ad aree verdi non sensibili
select count(*) as num_interventi
from intervento i, interventoassegnato ia, areaverde a
where i.id = ia.intervento
  and i.area_verde = a.id
  and ia.fine is null
  and a.is_sensibile = false;

-- 9. le aree verdi senza nessun soggetto verde.
select *
from areaverde a
where not exists (
    select 1
    from soggettoverde s
    where s.area_verde = a.id
);