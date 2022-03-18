#!/usr/bin/env python
# coding: utf-8

# # Screencast Code
# 
# The follow code is the same used in the "Numeric Features" screencast. Run each code cell to see how 

# In[ ]:


from pyspark.sql import SparkSession
from pyspark.ml.feature import RegexTokenizer, VectorAssembler, Normalizer, StandardScaler
from pyspark.sql.functions import udf
from pyspark.sql.types import IntegerType

import re


# In[ ]:


# create a SparkSession: note this step was left out of the screencast
spark = SparkSession.builder     .master("local")     .appName("Word Count")     .getOrCreate()


# # Read in the Data Set

# In[ ]:


stack_overflow_data = 'Train_onetag_small.json'


# In[ ]:


df = spark.read.json(stack_overflow_data)


# In[ ]:


df.head()


# # Tokenization
# 
# Tokenization splits strings into separate words. Spark has a [Tokenizer](https://spark.apache.org/docs/latest/ml-features.html#tokenizer) class as well as RegexTokenizer, which allows for more control over the tokenization process.

# In[ ]:


# split the body text into separate words

regexTokenizer = RegexTokenizer(inputCol="Body", outputCol="words", pattern="\\W")
df = regexTokenizer.transform(df)
df.head()


# In[ ]:


# count the number of words in each body tag

body_length = udf(lambda x: len(x), IntegerType())
df = df.withColumn("BodyLength", body_length(df.words))


# In[ ]:


# count the number of paragraphs and links in each body tag

number_of_paragraphs = udf(lambda x: len(re.findall("</p>", x)), IntegerType())
number_of_links = udf(lambda x: len(re.findall("</a>", x)), IntegerType())


# In[ ]:


df = df.withColumn("NumParagraphs", number_of_paragraphs(df.Body))
df = df.withColumn("NumLinks", number_of_links(df.Body))


# In[ ]:


df.head(2)


# # VectorAssembler
# 
# Combine the body length, number of paragraphs, and number of links columns into a vector

# In[ ]:


assembler = VectorAssembler(inputCols=["BodyLength", "NumParagraphs", "NumLinks"], outputCol="NumFeatures")
df = assembler.transform(df)


# In[ ]:


df.head()


# # Normalize the Vectors

# In[ ]:


scaler = Normalizer(inputCol="NumFeatures", outputCol="ScaledNumFeatures")
df = scaler.transform(df)


# In[ ]:


df.head(2)


# # Scale the Vectors

# In[ ]:


scaler2 = StandardScaler(inputCol="NumFeatures", outputCol="ScaledNumFeatures2", withStd=True)
scalerModel = scaler2.fit(df)
df = scalerModel.transform(df)


# In[ ]:


df.head(2)

