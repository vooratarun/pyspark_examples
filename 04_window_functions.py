from pyspark.sql import SparkSession
from pyspark.sql.functions import col, row_number
from pyspark.sql.window import Window

spark = SparkSession.builder.appName("WindowFunctions").getOrCreate()

data = [
    (1, "Alice", 1200),
    (2, "Bob", 300),
    (3, "Charlie", 950),
    (4, "David", 1500),
]

df = spark.createDataFrame(data, ["user_id", "name", "revenue"])

window = Window.orderBy(col("revenue").desc())

ranked = df.withColumn(
    "rank",
    row_number().over(window)
)

ranked.show()
spark.stop()
