import psycopg2

def main():
    DB_HOST = "localhost"
    DB_NAME = "flight_dataset"
    DB_USER = "postgres"
    DB_PASS = "Guide@5805795"
    DB_PORT = "5432"

    conn = None
    cursor = None

    try:
        # Connect to PostgreSQL
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS,
            port=DB_PORT
        )
        cursor = conn.cursor()

        # SQL Join query
        query = """
        SELECT 
            b.flight_date,
            b.airline AS business_airline,
            b.price AS business_price,
            e.airline AS economy_airline,
            e.price AS economy_price
        FROM flights_business b
        JOIN flights_economy e
          ON b.flight_date = e.flight_date
         AND b.origin = e.origin
         AND b.destination = e.destination
         AND b.dep_time = e.dep_time;
        """
        cursor.execute(query)
        results = cursor.fetchall()

        header = "flight_date | business_airline | business_price | economy_airline | economy_price"
        separator = "-" * 80

        # Print to console
        print(header)
        print(separator)
        for row in results:
            print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]}")

        # Save results to text file
        with open("join_results.txt", "w", encoding="utf-8") as f:
            f.write(header + "\n")
            f.write(separator + "\n")
            for row in results:
                f.write(f"{row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]}\n")

        print("\n✅ Results also saved to join_results.txt")

    except Exception as e:
        print(f"❌ An error occurred: {e}")

    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()

if __name__ == "__main__":
    main()
