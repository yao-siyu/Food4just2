# Build the recommendation model using Alternating Least Squares
from pyspark.mllib.recommendation import ALS, MatrixFactorizationModel, Rating

newratingsRDD = newratings.rdd
ratingsML = newratingsRDD.map(lambda l: Rating(int(l[6]), int(l[8]), float(l[3])))

rank = 10
numIterations = 10
model = ALS.train(ratingsML, rank, numIterations)

# Evaluate the model on training data

testdata = ratingsML.map(lambda p: (p[0], p[1]))
predictions = model.predictAll(testdata).map(lambda r: ((r[0], r[1]), r[2]))
ratesAndPreds = ratingsML.map(lambda r: ((r[0], r[1]), r[2])).join(predictions)
MSE = ratesAndPreds.map(lambda r: (r[1][0] - r[1][1])**2).mean()
print("Mean Squared Error = " + str(MSE))

#0.327520844251 -- rank = 10, numIterations = 10


# Save and load model
model.save(sc, "s3n://restaurant-picker-data/model")
sameModel = MatrixFactorizationModel.load(sc, "s3n://restaurant-picker-data/model")
