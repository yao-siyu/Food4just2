## Food4just2

A Restaurant Recommendation Engine that suits two people 

Screencast: https://youtu.be/YC0G9e8o9CI



## Business Value

As per 2018 Dining Trend Survey, Americans typically dine out 5.9 times per work. And according to OpenTable, most of its restaurant reservations are made for two or more people. However, two people may have different level of similarity on tastes in food.

This project is to develop a data platform to recommend restaurants "just for two", a.k.a. "Solo per Due". It is intended to solve the potential issues listed in below with the singular characteristic of two people, i.e., couples, colleagues, friends, dating parters, etc.

This recommendation system not only can improve customers' satisfaction, but also be able to help business increase revenue, as statistics showing 35% of Amazon total revenues come from the positive effects of recommendation system. This project has the potential to be easily converted to other applications that involve more than one party, e.g., movies and hotels recommendations.



## Engineering Challenge

1. Collaborative filtering model - Cold Start
In production, for new users or items that have no rating history and on which the model has not been trained, this is the “cold start problem”.
Solution -- according to new users’ attributes like age, gender etc., find old users’ sharing the same attributes, get the average ratings as the prediction for new users

2. Location Query
The model predicts the ratings a user may give to all the restaurants in the datasets, but a user’s query usually from the same city, there is no need to waste time and resources to scan all the ratings
Solution -- save the predictions for the restaurants that are in the same city as the user’s last query into a seperate table, query it first and if cannot find the ratings, then go to the table with all data


## Tech Stack

1. Store raw data in Amazon S3
2. Load data into a Spark batch job; train ALS collaborative filtering model, save the model to Amazon S3
3. Transfer predictions based on the model to a PostgreSQL database
4. In a Flask application, use Google Maps API to show the results of queries

![alt text](https://github.com/yao-siyu/Food4just2/blob/master/Data%20Pipeline.png)
      

## Data

Yelp open dataset (~5GB, over 6.68M reviews)
https://www.yelp.com/dataset

