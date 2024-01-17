from pyspark.sql import SparkSession
from pyspark.sql.functions import avg

# Создаем сессию Spark
spark = SparkSession.builder.appName("HousePrices").getOrCreate()

# Загружаем данные из PostgreSQL
df = spark.read \
    .format("jdbc") \
    .option("url", "jdbc:postgresql://postgres:5432/db_house") \
    .option("dbtable", "table_name") \
    .option("user", "postgres") \
    .option("password", "postgres") \
    .option("driver", "org.postgresql.Driver") \
    .load()

# Вычисляем средние стоимости квартир и домов в зависимости от города, района и количества комнат (спален)
avg_prices = df.groupBy("city", "location",  "bedrooms").agg(avg("price").alias("avg_price"))

# Выводим результат
avg_prices.show()
