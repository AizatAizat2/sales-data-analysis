import psycopg2
import pandas as pd
import matplotlib.pyplot as plt

DB_NAME = "db_sales"
DB_USER = "school21"
DB_PASSWORD = "postgres"
DB_HOST = "localhost"
DB_PORT = 5432

def get_connection():
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT,
    )
    return conn

def main():
    conn = get_connection()

    query_all = """
        SELECT
            id,
            product,
            category,
            sale_date,
            quantity,
            price,
            quantity * price AS total_sum
        FROM sales;
    """
    df = pd.read_sql(query_all, conn)

    print("Первые строки:\n", df.head())
    print("\nБазовая статистика по сумме продаж:\n", df["total_sum"].describe())

    query_by_category = """
        SELECT
            category,
            SUM(quantity * price) AS revenue,
            SUM(quantity)         AS total_qty
        FROM sales
        GROUP BY category
        ORDER BY revenue DESC;
    """
    df_cat = pd.read_sql(query_by_category, conn)
    print("\nВыручка по категориям:\n", df_cat)

    query_by_date = """
        SELECT
            sale_date,
            SUM(quantity * price) AS revenue
        FROM sales
        GROUP BY sale_date
        ORDER BY sale_date;
    """
    df_date = pd.read_sql(query_by_date, conn)
    print("\nВыручка по дням:\n", df_date)

    conn.close()

    plt.figure(figsize=(8, 4))
    plt.plot(df_date["sale_date"], df_date["revenue"], marker="o")
    plt.title("Выручка по дням")
    plt.xlabel("Дата")
    plt.ylabel("Выручка")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("revenue_by_date.png")
    print("\n График сохранён в revenue_by_date.png")

    plt.figure(figsize=(6, 4))
    plt.bar(df_cat["category"], df_cat["revenue"])
    plt.title("Выручка по категориям")
    plt.xlabel("Категория")
    plt.ylabel("Выручка")
    plt.tight_layout()
    plt.savefig("revenue_by_category.png")
    print("График сохранён в revenue_by_category.png")

if __name__ == "__main__":
    main()
