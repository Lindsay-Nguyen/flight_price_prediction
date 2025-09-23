WITH biz AS (
  SELECT flight_date, origin, destination, AVG(price) AS avg_business_price
  FROM flights_business
  GROUP BY flight_date, origin, destination
),
eco AS (
  SELECT flight_date, origin, destination, AVG(price) AS avg_economy_price
  FROM flights_economy
  GROUP BY flight_date, origin, destination
)
SELECT 
  b.flight_date,
  b.origin,
  b.destination,
  b.avg_business_price,
  e.avg_economy_price
FROM biz b
JOIN eco e
  ON b.flight_date = e.flight_date
 AND b.origin = e.origin
 AND b.destination = e.destination;
