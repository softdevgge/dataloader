# Dataloader for procurement public data
## Problem :
Generates a dataloader for procurement public data to consume from a procurement government dashboard.

## Solution Approach:
- CREATE THE CONTAINER

    docker run -p 5432:5432 --name postgres -e POSTGRES_PASSWORD=pstg123 -e POSTGRES_USER=pstguser -e POSTGRES_DB=contrataciones -d postgres

- EXTRACT THE FILE .TAR.GZ AND COPY THE CONTENT TO THE CONTAINER

    docker cp ./Contratos2021_231112011934.csv postgres:/Contratos2021_231112011934.csv

## Explanation
- EXECUTE 
    here you can use pipenv or just pip

    pip install -r requirements.txt  

    upload_engagements.py


## UTILITIES

    docker exec -it postgres bash

    --dont use localhost, use the name of the hostname.
    psql -h localhost -d contrataciones -U pstguser

    when ask for pass:  pstg123
    \c contrataciones

    to extract  dump
    docker exec postgres pg_dump -U pstguser -F t contrataciones > mydb.tar



    some querys

    SELECT count(*),contract."Plantilla del expediente" FROM contract group by contract."Plantilla del expediente" order by 1 desc;


