from pathlib import Path
import shutil
from pyspark import SparkContext
import re

import os
os.environ["JAVA_HOME"] = "/Library/Java/JavaVirtualMachines/jdk-17.jdk/Contents/Home"
os.environ["SPARK_HOME"] = "/Applications/Spark"

from pyspark.sql import SparkSession
spark = SparkSession.builder \
    .appName("WordCount") \
    .getOrCreate()

sc = spark.sparkContext
# Read the input file and Calculating words count
text_file = sc.textFile("source_in.txt")

# 定義清理函數
def clean_text(text):
    text = text.lower()  # 轉小寫
    text = re.sub(r'[^\w\s]', '', text)  # 去除標點符號
    text = re.sub(r'\s+', ' ', text).strip()  # 去除多餘空白
    return text

# 清理，分詞，並計算詞頻
word_counts = (text_file
               .map(clean_text)  # 清理文本
               .flatMap(lambda line: line.split())  # 分詞
               .map(lambda word: (word, 1))  # 記錄詞頻
               .reduceByKey(lambda a, b: a + b))  # 合併相同的詞

# 保存結果
path = Path.cwd() / "pyspark_output"
if path.exists():
    for file in path.rglob('*'):
        file.unlink()
    path.rmdir()

word_counts.saveAsTextFile("pyspark_output")