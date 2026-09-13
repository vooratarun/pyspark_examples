from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("SparkSQL").getOrCreate()

data = [
    (1, "Alice", 25, "Hyderabad"),
    (2, "Bob", 30, "Bangalore"),
    (3, "Charlie", 35, "Hyderabad"),
    (4, "David", 28, "Mumbai"),
]

df = spark.createDataFrame(data, ["id", "name", "age", "city"])
df.createOrReplaceTempView("users")

result = spark.sql("""
    SELECT city,
           COUNT(*) AS users,
           AVG(age) AS average_age
    FROM users
    GROUP BY city
    ORDER BY users DESC
""")

result.show()
spark.stop()
