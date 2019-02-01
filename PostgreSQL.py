#Connect to Postgres
from pyspark import SparkContext,SparkConf
sparkClassPath = '/usr/local/spark/jars'

conf = SparkConf()
conf.setAppName('appname')
conf.set('spark.jars', 'file:%s' % sparkClassPath)
conf.set('spark.executor.extraClassPath', sparkClassPath)
conf.set('spark.driver.extraClassPath', sparkClassPath)
conf.set('spark.master', 'spark://localhost:7077')

url = "jdbc:postgresql://34.222.230.25:5432/test"
props = {"user": "test_user", "password": "insight", "driver": "org.postgresql.Driver"}


#Write DataFrame to PostgreSQL

def writeToDatabase(self, df, table, mode):
    from pyspark.sql import *

    my_writer = DataFrameWriter(df)
    my_writer.jdbc(url, table, mode, props)

#save users profile to database
self.writeToDatabase(users, 'user', 'overwrite')
#save business information to database
bu_attri = businessWithIntID.select('attributes.*', 'bid')
self.writeToDatabase(bu_attri, 'bu_attri', 'overwrite')

bu_hr = businessWithIntID.select('hours.*', 'bid')
self.writeToDatabase(bu_hr, 'bu_hr', 'overwrite')

bu = businessWithIntID.drop('attributes').drop('hours')
self.writeToDatabase(bu, 'bu', 'overwrite')

#Read DataFrame to PostgreSQL
#df = sqlContext.read.jdbc(url=url, table="ratingsML", properties=props)


#Convert RDD to dateframe
from pyspark.sql.types import Row

#here you are going to create a function
def f(x):
    d = {}
    for i in range(len(x)):
        d[str(i)] = x[i]
    return d

#save predictions to database
pre = predictions.map(lambda x: Row(**f(x))).toDF()
pre.select('0.*', '1')
self.writeToDatabase(pre, 'pre', 'overwrite')
