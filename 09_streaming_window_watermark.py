from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum, window

spark = SparkSession.builder.appName("StreamingWindows").getOrCreate()

# Expects a streaming DataFrame with:
# timestamp, user_id, event, amount

events = spark.readStream     .format("socket")     .option("host", "localhost")     .option("port", 9999)     .load()

# This example is intentionally simplified for learning.
# For real event-time processing, parse an event timestamp from JSON.

# Example pattern:
# sales = events.withWatermark("timestamp", "10 minutes") #     .groupBy(window("timestamp", "5 minutes"), "user_id") #     .agg(sum("amount").alias("total_sales"))

print("Learn the production pattern:")
print("""
sales = purchases.withWatermark("timestamp", "10 minutes") \
    .groupBy(window("timestamp", "5 minutes"), "user_id") \
    .agg(sum("amount").alias("total_sales"))
""")

spark.stop()
