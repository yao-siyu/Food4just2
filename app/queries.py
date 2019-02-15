from sqlalchemy.engine.interfaces import Dialect
from sqlalchemy import create_engine
import yaml

config = yaml.load(open('../config.yaml'))

engine = create_engine(config['postgresql'])
conn = engine.connect()


#get result for input users and location
def get_result(user1, user2, la, lo):
	
	#Get sum of ratings of two users for each restaurant
	sql_string = """
		DROP TABLE IF EXISTS ratings, distance, twousers, result, rateandpre;

		CREATE TABLE rateandpre AS(SELECT * FROM
		(SELECT * FROM pre WHERE uid IN (%s, %s)) two_pre
		RIGHT JOIN(SELECT * FROM review WHERE uid IN (%s, %s)) two_review
		ON two_pre.userID = two_review.uid AND two_pre.buID = two_review.bid);

		CREATE TABLE twousers AS(
		SELECT bid, SUM(ratings) AS sumRatings
		FROM (SELECT COALESCE(stars, pre) AS ratings, bid, uid
		FROM rateandpre) AS ratings
		WHERE uid IN (%s, %s)
		GROUP BY bid);
		"""

	conn.execute(sql_string, (user1, user2))
		

	#Get the top 20 near the input location
	sql_string = """
		CREATE TABLE distance AS(
		SELECT *, (SELECT(point(latitude, longitude) <@> point(%s, %s)) AS distance) FROM business);

		CREATE TABLE result AS(
		SELECT name, address, latitude, longitude
		FROM distance
		JOIN twousers ON twousers.bid = distance.bid
		WHERE distance.distance < 20
		ORDER BY sumRatings LIMIT 10);


		"""
		
	conn.execute(sql_string, (la, lo))


CREATE TABLE rateandpre AS(SELECT * FROM
		(SELECT * FROM pre WHERE uid IN (1000, 2000)) two_pre
		RIGHT JOIN(SELECT * FROM review WHERE uid IN (1000, 2000)) two_review
		ON two_pre.userID = two_review.uid AND two_pre.buID = two_review.bid);



