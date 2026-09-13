from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("ParquetPartitioning").getOrCreate()

data = [
    (1, "Alice", "Hyderabad"),
    (2, "Bob", "Bangalore"),
    (3, "Charlie", "Hyderabad"),
    (4, "David", "Mumbai"),
]

df = spark.createDataFrame(data, ["id", "name", "city"])

# Write partitioned Parquet
df.write.mode("overwrite")     .partitionBy("city")     .parquet("output/users")

# Read it back
loaded = spark.read.parquet("output/users")
loaded.show()

spark.stop()
