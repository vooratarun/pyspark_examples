# PySpark Examples

A progressive collection of PySpark examples.

## Prerequisites

- Python 3.9+
- Apache Spark / PySpark
- Java version compatible with your Spark installation

Install PySpark:

    pip install pyspark

## Examples

1. DataFrame basics
2. GroupBy and aggregations
3. Joins
4. Window functions
5. Spark SQL
6. Parquet and partitioning
7. Structured Streaming with socket
8. Structured Streaming with Kafka
9. Streaming windows and watermarks
10. Python UDF

## Run

Example:

    spark-submit 01_dataframe_basics.py

For the socket streaming example, start a terminal with:

    nc -lk 9999

Then run:

    spark-submit 07_structured_streaming_socket.py

## Suggested learning order

DataFrames
-> transformations
-> aggregations
-> joins
-> windows
-> SQL
-> Parquet
-> partitioning
-> Structured Streaming
-> Kafka
-> watermarks
-> checkpointing
-> Spark performance tuning
# pyspark_examples
