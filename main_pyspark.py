import os

from pyspark.sql import SparkSession
from pyspark.sql import DataFrame
from pyspark.sql.functions import col

# это было для локального теста
os.environ["JAVA_HOME"] = r"S:\CODE\GIT_repo\jdk-11"
# спасибо компании Oracle за то, что усложняет жизнь людям

spark = SparkSession.builder.appName("Example").getOrCreate()

def get_products_with_categories(products_df: DataFrame, 
                               categories_df: DataFrame, 
                               product_category_links_df: DataFrame) -> DataFrame:
    """
    Возвращает датафрейм со всеми парами "Имя продукта – Имя категории" 
    """
    # Соединяем продукты с их категориями
    products_with_categories = (
        products_df.join(
            product_category_links_df, 
            on="product_id", 
            how="left"
        )
        .join(
            categories_df, 
            on="category_id", 
            how="left"
        )
        .select(
            col("product_name"), 
            col("category_name")
        )
    )
    
    return products_with_categories

# Пример данных
products_data = [(1, "Продукт 1"), (2, "Продукт 2"), (3, "Продукт 3"), (4, "Продукт 4")]
categories_data = [(1, "Категория A"), (2, "Категория B"), (3, "Категория C"), (4, "Категория D")]
links_data = [(1, 1), (1, 2), (2, 1), (3, 1), (3, 2), (3, 4), (2, 4)]

try:
    # Создание датафреймов
    products_df = spark.createDataFrame(products_data, ["product_id", "product_name"])
    categories_df = spark.createDataFrame(categories_data, ["category_id", "category_name"])
    links_df = spark.createDataFrame(links_data, ["product_id", "category_id"])

    # Вызов функции
    result = get_products_with_categories(products_df, categories_df, links_df)
    result.orderBy("product_name", "category_name").show()
finally:
    spark.stop()