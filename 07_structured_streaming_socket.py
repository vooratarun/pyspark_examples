from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("SocketStreaming").getOrCreate()

stream_df = spark.readStream     .format("socket")     .option("host", "localhost")     .option("port", 9999)     .load()

query = stream_df.writeStream     .format("console")     .outputMode("append")     .start()

query.awaitTermination()
