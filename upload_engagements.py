import time
import pandas as pd
from sqlalchemy import create_engine, Integer ,Date
import psycopg2
from datetime import datetime


dateparse = lambda x: datetime.strptime(x, '%Y-%m-%d')



#INPUT YOUR OWN CONNECTION STRING HERE
conn_string = 'postgresql://pstguser:pstg123@127.0.0.1/contrataciones'

#Import .csv file

dfcontra = pd.read_csv('Contratos2021_231112011934_short.csv', 
                       parse_dates=['Fecha de inicio del contrato','Fecha de fin del contrato'], 
                       date_parser=dateparse)



#perform to_sql test and print result
db = create_engine(conn_string)
conn = db.connect()

start_time = time.time()
dfcontra.to_sql('contract_test', con=conn, if_exists='replace', index=False)
print("contract_test: {} seconds".format(time.time() - start_time))



#perform COPY test and print result
sql = '''
COPY contract
FROM '/Contratos2021_231112011934.csv' --input full file path here. see line 46
DELIMITER ',' CSV HEADER;
'''

table_create_sql = '''
CREATE TABLE IF NOT EXISTS contract  (
    "Orden de gobierno" text,
    "Siglas de la Institución" text,
    "Institución" text,
    "Clave de la UC" text,
    "Código del expediente" text,
    "Clave CUCOP" text,
    "Plantilla del expediente" text,
    "Fundamento legal" text,
    "Número del procedimiento" text,
    "Carácter del procedimiento" text,
    "Tipo de contratación" text,
    "Tipo de procedimiento" text,
    "Forma de participación" text,
    "Código del contrato" text,
    "Título del contrato" text,
    "Fecha de inicio del contrato" timestamp without time zone,
    "Fecha de fin del contrato" timestamp without time zone,
    "Importe del contrato" double precision,
    "Moneda del contrato" text,
    "Estatus del contrato" text,
    "Convenio modificatorio" bigint,
    "Fecha de firma del contrato" text,
    "Contrato marco" text,
    "Compra consolidada" bigint,
    "Contrato plurianual" bigint,
    "Clave de cartera SHCP" text,
    "Folio en el RUPC" double precision,
    "RFC" text,
    "Proveedor o contratista" text,
    "Estratificación de la empresa" text,
    "Clave del país de la empresa" text,
    "RFC verificado en el SAT" bigint
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