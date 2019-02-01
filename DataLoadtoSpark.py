#Get data from S3 to Spark
#S3 bucket "s3n://restaurant-picker-data"
from pyspark.sql import SQLContext
sqlContext = SQLContext(sc)

#Preprocess data for ML
reviews = sqlContext.read.json("s3n://restaurant-picker-data/review.json")
ratings = reviews.drop('cool').drop('funny').drop('text').drop('useful')
ratingsRDD = ratings.rdd

users = sqlContext.read.json("s3n://restaurant-picker-data/user.json")
businesses = sqlContext.read.json("s3n://restaurant-picker-data/business.json")

#Add uid -- int id for users
uID = users.rdd.map(lambda u: u.user_id).distinct().zipWithIndex()
usersDf = sqlContext.createDataFrame(uID, ['user', 'uid'])
usersWithIntID = users.join(usersDf, users.user_id == usersDf.user).drop('user')

#Add bid -- int id for business
bID = businesses.rdd.map(lambda b: b.business_id).distinct().zipWithIndex()
businessDf = sqlContext.createDataFrame(bID, ['business', 'bid'])
businessWithIntID = businesses.join(businessDf, businesses.business_id == businessDf.business).drop('business')

newratings = ratings.join(usersDf, ratings.user_id == usersDf.user).join(businessDf, ratings.business_id == businessDf.business)
