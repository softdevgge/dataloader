
1) CREATE THE CONTAINER

docker run -p 5432:5432 --name postgres -e POSTGRES_PASSWORD=pstg123 -e POSTGRES_USER=pstguser -d postgres

2) EXTRACT THE FILE .TAR.GZ AND COPY THE CONTENT TO THE CONTAINER

docker cp ./Contratos2021_231112011934.csv postgres:/Contratos2021_231112011934.csv


2) EXECUTE upload_engagements.py


docker exec -it postgres bash

--dont use localhost, use the name of the hostname.
psql -h localhost -U postgres

psql -h 662312e17c10 -U pstguser
when ask for pass:  pstg123
\c contrataciones



to extract  dump
docker exec postgres pg_dump -U pstguser -F t contrataciones > mydb.tar



some querys

SELECT count(*),contract."Plantilla del expediente" FROM contract group by contract."Plantilla del expediente" order by 1 desc;

SELECT sum("Importe del contrato"),contract."Plantilla del expediente" FROM contract group by contract."Plantilla del expediente" order by 1 desc;


