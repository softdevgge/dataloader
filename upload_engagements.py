import time
import pandas as pd
from sqlalchemy import create_engine, Integer ,Date
import psycopg2
from datetime import datetime

dateparse = lambda x: datetime.strptime(x, '%Y-%m-%d')

#INPUT YOUR OWN CONNECTION STRING HERE
conn_string = 'postgresql://pstguser:pstg123@127.0.0.1/contrataciones'

#Import .csv file           this way is not commendable
#dfcontra = pd.read_csv('Contratos2021_231112011934_short.csv', 
#                       parse_dates=['Fecha de inicio del contrato','Fecha de fin del contrato'], 
                       #date_parser=dateparse)

#perform to_sql test and print result
db = create_engine(conn_string)
conn = db.connect()

start_time = time.time()
#dfcontra.to_sql('contract_test', con=conn, if_exists='replace', index=False)
#print("contract_test: {} seconds".format(time.time() - start_time))

#perform COPY test and print result
sql = '''
COPY contract
FROM '/Contratos2021_231112011934.csv' --input full file path here
DELIMITER ',' CSV HEADER;
'''

table_create_sql = '''
CREATE TABLE IF NOT EXISTS contract  (
    "Siglas de la Institución" text,    
    "Plantilla del expediente" text,
    "Código del contrato" text,
    "Título del contrato" text,
    "Fecha de inicio del contrato" timestamp without time zone,
    "Fecha de fin del contrato" timestamp without time zone,
    "Importe del contrato" double precision,    
    "Estatus del contrato" text,    
    "RFC" text,
    "Proveedor o contratista" text  
)
'''

pg_conn = psycopg2.connect(conn_string)
cur = pg_conn.cursor()
cur.execute(table_create_sql)
cur.execute('TRUNCATE TABLE contract') #Truncate the table in case you've already run the script before

start_time = time.time()
#dfcontra.to_csv('Contratos2021_231112011934_short_copy.csv', index=False, header=False) #Name the .csv file reference in line 29 here
cur.execute(sql)
pg_conn.commit()
cur.close()
print("COPY duration: {} seconds".format(time.time() - start_time))
#close connection
conn.close()