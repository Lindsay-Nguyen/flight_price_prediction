-- 1. Average price by airline (economy)
SELECT DISTINCT airline, AVG(price) AS avg_price
FROM flights_economy
GROUP BY airline
ORDER BY avg_price DESC;