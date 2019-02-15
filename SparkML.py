from pyspark.mllib.recommendation import ALS, MatrixFactorizationModel, Rating
from pyspark import StorageLevel
import yaml

config = yaml.load(open('../config.yaml'))

newratingsRDD = newratings.rdd
ratingsML = newratingsRDD.map(lambda l: Rating(int(l[6]), int(l[8]), float(l[3])))

rank = 100
numIterations = 20
model = ALS.train(ratingsML, rank, numIterations)

# Evaluate the model on training data

testdata = ratingsML.map(lambda p: (p[0], p[1]))
predictions = model.predictAll(testdata).map(lambda r: ((r[0], r[1]), r[2]))
ratesAndPreds = ratingsML.map(lambda r: ((r[0], r[1]), r[2])).join(predictions)
MSE = ratesAndPreds.map(lambda r: (r[1][0] - r[1][1])**2).mean()
print("Mean Squared Error = " + str(MSE))

#0.327520844251 -- rank = 10, numIterations = 10
#0.0835593328909 -- rank = 50, numIterations = 10

# Save and load model

model.save(sc, config['S3_model'])

model = MatrixFactorizationModel.load(sc, config['S3_model'])

userFeatures = model.userFeatures().repartition(1)
userFeatures.persist(StorageLevel.MEMORY_AND_DISK_SER)

productFeatures = model.productFeatures().repartition(1)
productFeatures.persist(StorageLevel.MEMORY_AND_DISK_SER)

predictions = model.predictAll(user_res.rdd).map(lambda r: ((r[0], r[1]), r[2]))