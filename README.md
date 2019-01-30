## Restaurant For Just 2
Restaurant recommendation for a group of two people


## Business Value
Two people may have different level of similarity on tastes in food. Sometimes they are not on the same boat at all. This project is to develop a data platform to recommend restaurants "just for two", a.k.a. "Solo per Due". It is intended to solve the potential issues listed in below with the singular characteristic of two people, i.e., couples, colleagues, friends, dating parters, etc.

1). To discover what they have and don't have in common in terms of food.
2). To help make decision by using historical data when struggling with various options.
3). To reduce the potential dis-agreement, argument, or even fightings over the decision of where to eat or what to eat.
4). To recommend fun exotic recipes for a cooked meal.


## Engineering Challenge
1. Recommendation system for multiple users
2. find results inside a radius of certain location


## Tech Stack
Kafka --> S3 --> Spark --> PostgreSQL --> Flask


## Data
Using stimulated data based on yelp open dataset (~5GB, over 6.68M reviews)


## MVP
1. build up Spark collaborative filter model
2. PostgreSQL to deal with location component
