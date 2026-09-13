from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when

spark = SparkSession.builder.appName("DataFrameBasics").getOrCreate()

data = [
    (1, "Alice", 25, "Hyderabad"),
    (2, "Bob", 30, "Bangalore"),
    (3, "Charlie", 35, "Hyderabad"),
    (4, "David", 28, "Mumbai"),
]

df = spark.createDataFrame(data, ["id", "name", "age", "city"])

df.show()
df.select("name", "age").show()
df.filter(col("age") > 28).show()

df2 = df.withColumn(
    "category",
    when(col("age") >= 30, "Senior").otherwise("Junior")
)
df2.show()

spark.stop()
