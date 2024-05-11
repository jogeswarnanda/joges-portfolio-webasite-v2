# IMPORT THE SQALCHEMY LIBRARY's CREATE_ENGINE METHOD
from sqlalchemy import create_engine, text
import os

from sqlalchemy.sql.selectable import Values
# engine=create_engine("postgresql+psycopg2://postgres.cxntcshwyqnjqmtycmkm:postgres.cxntcshwyqnjqmtycmkm@aws-0-ap-southeast-1.pooler.supabase.com port=5432/postgres")
# with engine.connect() as conn:
# result = conn,execute(text("Hello !!"))
# print(result.all())
#from sqlalchemy import create_engine
#engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)
#engine=create_engine("postgresql+psycopg2://postgres.wpdsognshpvkjlginido:pTRoGlDpl9IUgQXh@aws-0-ap-southeast-1.pooler.supabase.com/jogeswardb",pool_pre_ping=True,connect_args={
 #                       "keepalives": 1,
 #                       "keepalives_idle": 30,
 #                       "keepalives_interval": 10,
 ##                       "keepalives_count": 5,
  #                  })
#engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)

#-----------sensitive
#from sqlalchemy import create_engine
#engine=create_engine("postgresql://neondb_owner:9lfadbx4XSCU@ep-flat-frog-a13qydk8.ap-#southeast-1.aws.neon.tech/neondb?sslmode=require")
#-----------sensitive
db_conn_string = os.environ['DB_CONNECTION_STRING']
from sqlalchemy import create_engine
engine=create_engine(db_conn_string)

#with engine.connect() as conn:
 # result = conn.execute(text("select * from jobs"))
  #res_dicts = []
  #for r in result.all():
  #  res_dicts.append(r)
  #print(res_dicts)
  #result_all = result.all()
  #print(type(result.all()))
  #print(result_all)
  #print(type(result_all[0]))
  #first_result_dict1=result_all[0]
  #first_result_dict=dict((first_result_dict1))
  #print(first_result_dict)
  #result_dict = []
  #result_dict.dict.append(dict(r)) 
  #print("final res::", result_dict)

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for r in result.all():
      jobs.append(r)
    #print ("SAALLLLA :", jobs)
    return jobs

def load_job_from_db(id):
  values = { 'code' :  id }
  with engine.connect() as conn:
    text1 = text("select * from jobs where jobs.id = :code")
    result = conn.execute(text1, values)
    rows = result.all()
    print("rows_new::", rows)
    if len(rows) == 0:
      print ("return no rows")
      return None
    else:
      return rows[0]
