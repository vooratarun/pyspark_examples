from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_json
from pyspark.sql.types import (
    StructType, StructField, IntegerType, StringType, DoubleType
)

spark = SparkSession.builder.appName("KafkaStreaming").getOrCreate()

schema = StructType([
    StructField("user_id", IntegerType()),
    StructField("event", StringType()),
    StructField("amount", DoubleType()),
])

events = spark.readStream     .format("kafka")     .option("kafka.bootstrap.servers", "localhost:9092")     .option("subscribe", "events")     .option("startingOffsets", "latest")     .load()

parsed = events.select(
    col("timestamp"),
    from_json(col("value").cast("string"), schema).alias("data")
).select("timestamp", "data.*")

purchases = parsed.filter(col("event") == "purchase")

query = purchases.writeStream     .format("console")     .outputMode("append")     .option("checkpointLocation", "checkpoint/purchases")     .start()

query.awaitTermination()
