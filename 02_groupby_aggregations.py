from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, count, max, min, sum

spark = SparkSession.builder.appName("Aggregations").getOrCreate()

data = [
    (1, "Hyderabad", 500),
    (2, "Hyderabad", 700),
    (3, "Bangalore", 300),
    (4, "Mumbai", 900),
]

df = spark.createDataFrame(data, ["user_id", "city", "amount"])

result = df.groupBy("city").agg(
    count("*").alias("orders"),
    sum("amount").alias("revenue"),
    avg("amount").alias("avg_order"),
    max("amount").alias("max_order"),
    min("amount").alias("min_order"),
)

result.orderBy("revenue", ascending=False).show()
spark.stop()
