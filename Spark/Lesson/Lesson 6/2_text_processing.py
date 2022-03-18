#!/usr/bin/env python
# coding: utf-8

# # Screencast Code
# 
# The follow code is the same used in the "Text Processing" screencast. Run each code cell to see how 

# In[ ]:


from pyspark.sql import SparkSession
from pyspark.ml.feature import RegexTokenizer, CountVectorizer,     IDF, StringIndexer
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


# # CountVectorizer

# In[ ]:


# find the term frequencies of the words
cv = CountVectorizer(inputCol="words", outputCol="TF", vocabSize=1000)
cvmodel = cv.fit(df)
df = cvmodel.transform(df)
df.take(1)


# In[ ]:


# show the vocabulary in order of 
cvmodel.vocabulary


# In[ ]:


# show the last 10 terms in the vocabulary
cvmodel.vocabulary[-10:]


# # Inter-document Frequency

# In[ ]:


idf = IDF(inputCol="TF", outputCol="TFIDF")
idfModel = idf.fit(df)
df = idfModel.transform(df)
df.head()


# # StringIndexer

# In[ ]:


indexer = StringIndexer(inputCol="oneTag", outputCol="label")
df = indexer.fit(df).transform(df)


# In[ ]:


df.head()

