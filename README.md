# flight_price_prediction
My Linear Regression model achieves R² = 0.90, explaining 90% of flight price variation. Ticket class (~92%) and duration (~6%) are the main drivers, while airline, stops, and departure time contribute less than 2%.
✈️ Flight Price Analysis & Prediction
This project demonstrates data wrangling, exploratory data analysis (EDA), and predictive modeling using real-world flight price data. It highlights both storytelling with visuals and building interpretable machine learning models.
________________________________________
📊EDA & Data Analysis
📌 Data Preparation
Used PostgreSQL to clean and preprocess raw flight data.
Applied SELECT and JOIN queries to combine tables and compute features such as average flight price by airline, class, and stops before feeding the data into Python for EDA and modeling.
🔧 Data Cleaning
•	Fixed inconsistent formats in dates, times, and prices (SQL preprocessing).
•	Handled missing / noisy values (e.g., strings like "1-stop\n").
📈 Exploratory Analysis & Visualizations (Python: pandas, matplotlib, seaborn)
•	Average flight price by airline → bar chart.
•	Price distribution across dataset → histogram.
•	Effect of number of stops on price → boxplot.
•	Cheapest vs. most expensive routes → grouped bar chart.
👉 This stage focused on EDA + storytelling with visuals, similar to projects like:
•	Movie Ratings Dashboard
•	COVID-19 Dashboard
•	Stock Price Analyzer
________________________________________
🤖Machine Learning
Goal: Predictive modeling with cleaned flight dataset
✈️ Flight Price Prediction (Regression)
•	Target: Flight ticket price
•	Features: Airline, class, stops, duration, days left until flight, departure time
•	Algorithm Used: Linear Regression
📊 Results
•	R² Score: 0.90
•	Mean Absolute Error (MAE): 4,904.72
•	Root Mean Squared Error (RMSE): 7,122.51
✅ A good fit for a relatively simple model, capturing 90% of variance in flight prices.

