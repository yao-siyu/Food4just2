#Get data from S3 to Spark
from pyspark.sql import SQLContext
from pyspark import SparkContext
import yaml

sc =SparkContext()

sqlContext = SQLContext(sc)
config = yaml.load(open('../config.yaml'))

reviews = sqlContext.read.json(config['S3_review'])
ratings = reviews.drop('cool').drop('funny').drop('text').drop('useful')
ratingsRDD = ratings.rdd

users = sqlContext.read.json(config['S3_user'])
businesses = sqlContext.read.json(config['S3_business'])


#Add uid -- int id for users
uID = users.rdd.map(lambda u: u.user_id).distinct().zipWithIndex()
usersDf = sqlContext.createDataFrame(uID, ['user', 'uid'])
usersWithIntID = users.join(usersDf, users.user_id == usersDf.user).drop('user')

#Add bid -- int id for business
bID = businesses.rdd.map(lambda b: b.business_id).distinct().zipWithIndex()
businessDf = sqlContext.createDataFrame(bID, ['business', 'bid'])
businessWithIntID = businesses.join(businessDf, businesses.business_id == businessDf.business).drop('business')

newratings = ratings.join(usersDf, ratings.user_id == usersDf.user).join(businessDf, ratings.business_id == businessDf.business)

#filter restaurant only
bu_att = businessWithIntID.select('attributes.*', 'bid')
restaurant = bu_att.filter(bu_att.RestaurantsAttire.isNotNull()).withColumnRenamed('bid', 'rid') #48639

res_ratings = newratings.join(restaurant, newratings.bid == restaurant.rid).drop('rid')

uid = res_ratings.select('uid').distinct()
bid = res_ratings.select('bid').distinct()

user_res = uid.crossJoin(bid)