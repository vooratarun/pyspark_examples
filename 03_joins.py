from pyspark.sql import SparkSession
from pyspark.sql.functions import sum

spark = SparkSession.builder.appName("Joins").getOrCreate()

users = spark.createDataFrame([
    (1, "Alice"),
    (2, "Bob"),
    (3, "Charlie"),
], ["user_id", "name"])

orders = spark.createDataFrame([
    (101, 1, 500),
    (102, 1, 700),
    (103, 2, 300),
], ["order_id", "user_id", "amount"])

joined = users.join(orders, "user_id", "inner")
joined.show()

revenue = joined.groupBy("user_id", "name").agg(
    sum("amount").alias("total_revenue")
)
revenue.show()

spark.stop()
