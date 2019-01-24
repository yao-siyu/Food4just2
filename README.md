# Restaurant-Picker
Restaurant recommendation for a group of two people


## Business Value
Which restaurant we should go? It has been a difficult decision to make for two people, especially you're visiting another city or you're planning for important date, and don't want the experience in the restaurant ruin your vacation or big date.


## Engineering Challenge
1. Recommendation system based on multiple users
2. find results inside a radius of certain location


## Tech Stack
Kafka --> S3 --> Spark --> PostgreSQL --> Flask


## Data
Using stimulated data based on yelp open dataset (~5GB, over 6.68M reviews)


## MVP
1. build up Spark collaborative filter model
2. PostgreSQL to deal with location component
