-- -- 1) Quante partite sono state giocate in ogni città?
--      citta     |  regione   |   nazione    | numero_partite 
-- ---------------+------------+--------------+----------------
--  Roma          | Lazio      | Italia       |              5
--  Milano        | Lombardia  | Italia       |              4
--  Tokyo         | Tokyo      | Giappone     |              3
--  Seoul         | Seoul      | Corea del Sud|              2
--  Venezia       | Veneto     | Italia       |              1

select c.nome, count(p.id) as numero_partite
from citta c, partita p
where c.id = p.citta
group by c.nome;


-- -- 2) Quanti giocatori hanno un rank maggiore o uguale a 5?
--  numero_giocatori 
-- ------------------
--                 8
select count(*) as player
from giocatore g
having g.rank >= 5;


-- -- 3) Quante partite sono state giocate con ogni insieme di regole?
--    regole    | numero_partite 
-- -------------+----------------
--  Giapponesi  |             10
--  Cinesi      |              2
--  Coreane     |              2
--  AGA         |              1

select p.regole, count(*) as numero_partite
from partita p
group by p.regole;

-- -- 4) Qual è la media, il massimo e il minimo dei punteggi del bianco?
--    media_bianco    | minimo_bianco | massimo_bianco 
-- -------------------+---------------+----------------
--  91.916666666666667|            65 |            120

select round(avg(punteggio_bianco)) as media_bianco, min(punteggio_bianco) as minimo_bianco, max(punteggio_bianco) as massimo_bianco
from partitaconpunteggio;

-- -- 5) Quali sono le medie, i massimi e i minimi dei punteggi per ogni giocatore?
--    nickname    |  nome   | cognome | media_punteggio | minimo_punteggio | massimo_punteggio 
-- ---------------+---------+---------+-----------------+------------------+-------------------
--  SamuraiGo     | Takeshi | Yamamoto|           110.0 |               88 |               120
--  CloudPlayer   | Wei     | Chen    |           106.0 |               98 |               110
--  WhitePhoenix  | Marco   | Ricci   |            88.5 |               82 |                95
--  ZenMaster     | Kenji   | Tanaka  |            88.0 |               75 |               100
--  MoonStone     | Jin     | Park    |            87.5 |               85 |                90
--  DragonKing    | Mario   | Rossi   |            85.0 |               76 |                92
--  GoNinja       | Giulia  | Verdi   |            81.5 |               75 |                88
--  StoneMaster   | Luca    | Bianchi |            81.5 |               78 |                85
--  RiverFlow     | Sara    | Colombo |            80.0 |               70 |                90
--  OceanWave     | Lisa    | Romano  |            70.0 |               70 |                70

SELECT 
    giocatore,
    ROUND(AVG(punteggio), 2) AS media_punti,
    MAX(punteggio) AS punteggio_massimo,
    MIN(punteggio) AS punteggio_minimo,
    COUNT(*) AS partite_giocate
FROM (
    -- Prendo i punteggi di quando il giocatore era Bianco
    SELECT p.bianco AS giocatore, pp.punteggio_bianco AS punteggio
    FROM partita p, partitaconpunteggio pp
    WHERE p.id = pp.partita
    
    UNION ALL
    
    -- Unisco i punteggi di quando il giocatore era Nero
    SELECT p.nero AS giocatore, pp.punteggio_nero AS punteggio
    FROM partita p, partitaconpunteggio pp
    WHERE p.id = pp.partita
) AS totale_punti
GROUP BY giocatore
ORDER BY media_punti DESC;

SELECT 
    g.nickname, 
    g.nome, 
    g.cognome,
    ROUND(AVG(tp.punteggio), 2) AS media_punti,
    MAX(tp.punteggio) AS punteggio_massimo,
    MIN(tp.punteggio) AS punteggio_minimo
FROM giocatore g
JOIN (
    -- Questa è la tua sottoquery che unifica i dati
    SELECT p.bianco AS giocatore_nk, pp.punteggio_bianco AS punteggio
    FROM partita p, partitaconpunteggio pp
    WHERE p.id = pp.partita
    
    UNION ALL
    
    SELECT p.nero AS giocatore_nk, pp.punteggio_nero AS punteggio
    FROM partita p, partitaconpunteggio pp
    WHERE p.id = pp.partita
) AS tp ON g.nickname = tp.giocatore_nk
GROUP BY g.nickname, g.nome, g.cognome
ORDER BY media_punti DESC;

WITH Statistiche AS (
    SELECT 
        giocatore_nk,
        ROUND(AVG(punteggio), 2) AS media_punti,
        MAX(punteggio) AS punteggio_massimo,
        MIN(punteggio) AS punteggio_minimo
    FROM (
        SELECT p.bianco AS giocatore_nk, pp.punteggio_bianco AS punteggio
        FROM partita p, partitaconpunteggio pp
        WHERE p.id = pp.partita
        UNION ALL
        SELECT p.nero AS giocatore_nk, pp.punteggio_nero AS punteggio
        FROM partita p, partitaconpunteggio pp
        WHERE p.id = pp.partita
    ) AS totale_punti
    GROUP BY giocatore_nk
)
SELECT 
    g.nickname, 
    g.nome, 
    g.cognome, 
    s.media_punti, 
    s.punteggio_massimo, 
    s.punteggio_minimo
FROM giocatore g
JOIN Statistiche s ON g.nickname = s.giocatore_nk
ORDER BY s.media_punti DESC;

-- -- 6) Qual è il numero totale di partite giocate da ogni giocatore?
--    nickname    |  nome   | cognome  | totale_partite 
-- ---------------+---------+----------+----------------
--  DragonKing    | Mario   | Rossi    |              4
--  WhitePhoenix  | Marco   | Ricci    |              3
--  SamuraiGo     | Takeshi | Yamamoto |              3
--  CloudPlayer   | Wei     | Chen     |              3
--  ZenMaster     | Kenji   | Tanaka   |              2
--  GoNinja       | Giulia  | Verdi    |              3
--  RiverFlow     | Sara    | Colombo  |              2
--  StoneMaster   | Luca    | Bianchi  |              2
--  MoonStone     | Jin     | Park     |              2
--  BlackTiger    | Anna    | Ferrari  |              2
--  MountainPeak  | Paolo   | Greco    |              3
--  OceanWave     | Lisa    | Romano   |              1

select g.nickname, g.nome, g.cognome, count(p.id) as partite_giocate
from giocatore g, partita p
where (g.nickname = p.bianco or g.nickname = p.nero)
group by g.nickname, g.nome, g.cognome

-- -- 7) Qual è la media, il massimo e il minimo dei rank dei giocatori italiani?
--    media_rank   | minimo_rank | massimo_rank 
-- ----------------+-------------+--------------
--  4.666666666667 |           2 |            7

select round(avg(g.rank), 2) as media_rank, min(g.rank) as minimo_rank, max(g.rank) as massimo_rank
from giocatore g, citta c
where g.citta = c.id and c.nazione = 'Italia';

-- -- 8) Quali sono le medie, i massimi e i minimi dei rank per ogni nazione?
--    nazione    |   media_rank   | minimo_rank | massimo_rank 
-- --------------+----------------+-------------+--------------
--  Giappone     | 8.500000000000 |           8 |            9
--  Cina         | 7.000000000000 |           7 |            7
--  Corea del Sud| 6.000000000000 |           6 |            6
--  Italia       | 4.666666666667 |           2 |            7

select c.nazione, round(avg(g.rank), 2) as media_rank, min(g.rank) as minimo_rank, max(g.rank) as massimo_rank
from giocatore g, citta c
where g.citta = c.id
group by c.nazione;

-- -- 9) Quante partite ha giocato 'Mario Rossi' in ogni torneo?
--        torneo        | edizione | numero_partite 
-- ---------------------+----------+----------------
--  Campionato Italiano | 2024     |              3

select t.nome, t.edizione, count(p.id) as numero_partite
from torneo t, partita p, giocatore g
where g.nome = 'Mario' 
    and g.cognome = 'Rossi'
    and (g.nickname = p.bianco or g.nickname = p.nero)
    and t.id = p.torneo
group by t.nome, t.edizione;


-- -- 10) Quali sono i tornei in cui hanno giocato più di 2 partite?
--  id_torneo |       torneo        | numero_partite 
-- -----------+---------------------+----------------
--          1 | Campionato Italiano |              4
--          5 | Milano Open         |              3
--          3 | Asian Masters       |              3

select t.id, t.nome, count(p.id) as numero_partite
from torneo t, partita p
where t.id = p.torneo
group by t.id, t.nome
having count(p.id) > 2;


-- -- 11) Quali sono i giocatori con rank >= 5 che hanno giocato in più di un torneo?
--   nickname   |  nome   | cognome  | rank | numero_tornei 
-- -------------+---------+----------+------+---------------
--  CloudPlayer | Wei     | Chen     |    7 |             2
--  SamuraiGo   | Takeshi | Yamamoto |    9 |             2

select g.nickname, g.nome, g.cognome, g.rank, count(distinct t.id) as numero_tornei
from giocatore g, partita p, torneo t
where t.id = p.torneo
    and (g.nickname = p.bianco or g.nickname = p.nero)
    and g.rank > 5
group by g.nickname, g.nome, g.cognome, g.rank;


-- -- 12) Qual è il numero di vittorie per rinuncia di ogni giocatore?
--    nickname   | nome  | cognome | vittorie_per_rinuncia 
-- --------------+-------+---------+-----------------------
--  DragonKing   | Mario | Rossi   |                     1
--  RiverFlow    | Sara  | Colombo |                     1
--  MountainPeak | Paolo | Greco   |                     1

select g.nickname, g.nome, g.cognome, count(*)
from partitaconrinuncia pcr, partita p, giocatore giocate
where pcr.partita = p.id
    and ((g.nickname = p.bianco and pcr.rinunciatario = 'Nero') or (g.nickname = p.nero and pcr.rinunciatario = 'Bianco'))
group by g.nickname, g.nome, g.cognome;