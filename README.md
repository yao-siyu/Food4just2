# Restaurant-Picker
Restaurant recommendation for a group of two people


## Business Value
My insight project is to build such a data platform with a focus on solving the issues for two people using their historical review data.  The Spark collaborative filtering model and established recommendation system are going to be adapted for two (or more) users. This project has the potential to be easily converted to other applications that involve more than one party, e.g., movies and hotels recommendations.


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
