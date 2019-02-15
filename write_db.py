from pyspark import SparkContext,SparkConf
from pyspark.sql import *
import yaml, queries

#Convert RDD to dateframe
from pyspark.sql.types import Row

#here you are going to create a function
def f(x):
    d = {}
    for i in range(len(x)):
        d[str(i)] = x[i]
    return d

config = yaml.load(open('../config.yaml'))

conf = SparkConf()
conf.setAppName('Food4just2')
conf.set('spark.jars', 'file:%s' % config['spark_path'])
conf.set('spark.executor.extraClassPath', config['spark_path'])
conf.set('spark.driver.extraClassPath', config['spark_path'])
conf.set('spark.master', 'spark://localhost:7077')

url = config['url']
props = config['props']

def writeToDatabase(df, table, mode):
	my_writer = DataFrameWriter(df)
    my_writer.jdbc(url, table, mode, props)


#save predictions to database

pre = predictions.map(lambda x: Row(**f(x))).toDF()
pre = pre.select('0.*', '1').withwithColumnRenamed('_1', 'userID').withwithColumnRenamed('_2', 'buID').withwithColumnRenamed('1', 'pre')

writeToDatabase(pre, 'pre', 'overwrite')
writeToDatabase(newratings, 'review', 'overwrite')
writeToDatabase(businessWithIntID.drop('attributes').drop('hours'), 'business', 'overwrite')
