from pyspark.sql import SparkSession
from pyspark.sql.functions import udf, col
from pyspark.sql.types import StringType

spark = SparkSession.builder.appName("UDF").getOrCreate()

data = [(1, 25), (2, 35), (3, 28)]
df = spark.createDataFrame(data, ["id", "age"])

def classify_age(age):
    return "Senior" if age >= 30 else "Junior"

classify_age_udf = udf(classify_age, StringType())

result = df.withColumn(
    "category",
    classify_age_udf(col("age"))
)

result.show()

# Prefer built-in Spark functions over Python UDFs when possible.
spark.stop()
