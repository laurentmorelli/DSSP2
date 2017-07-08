from pyspark import SparkContext
import pyspark
from pyspark.conf import SparkConf
from pyspark.sql import SQLContext
from pyspark.sql.types import StringType
from pyspark.sql.functions import udf
from pyspark.sql import HiveContext
from pyspark.sql import functions as sf
from pyspark.sql import SparkSession
from pyspark.ml.feature import HashingTF, IDF, Tokenizer
from pyspark.mllib.linalg import SparseVector
from pyspark.ml.linalg import DenseVector
from pyspark.sql import Row
from functools import partial
from pyspark.ml.regression import LinearRegression
import string
import nltk
from nltk.stem.porter import *
from nltk.corpus import stopwords



#sc = SparkContext(appName="Example1")

a = SparseVector(10000, {4847: 3.0224, 9959: 6.4765})
print a.dot(a)

#print a.dot(array([1., 2., 3., 4.]))

b = SparseVector(10000, {15: 0.2668, 67: 3.0431, 69: 3.6234, 93: 2.6627, 315: 7.5103, 415: 3.9424, 419: 4.5356, 493: 2.399, 788: 0.2727, 858: 0.3938, 895: 4.1358, 945: 1.7267, 957: 1.3669, 1011: 2.2394, 1023: 3.8091, 1073: 2.3907, 1083: 0.3262, 1094: 11.0179, 1097: 0.4381, 1139: 2.6822, 1150: 8.2041, 1189: 0.5638, 1256: 17.5543, 1263: 8.5782, 1281: 8.8954, 1310: 9.1987, 1526: 4.8518, 1582: 7.1831, 1583: 2.3611, 1602: 4.7686, 1604: 6.4506, 1877: 2.3439, 2084: 7.3841, 2133: 7.3699, 2294: 18.0579, 2330: 3.8281, 2335: 3.8597, 2398: 6.3038, 2509: 8.6915, 2523: 1.7322, 2596: 1.2136, 2807: 7.3231, 3155: 2.3272, 3183: 3.782, 3297: 2.1537, 3365: 2.5824, 3484: 2.6546, 3526: 1.0074, 3646: 2.708, 3718: 0.6741, 3770: 31.9623, 3792: 2.0484, 3849: 1.842, 3911: 6.8935, 3992: 3.4249, 4003: 1.0705, 4020: 3.8975, 4034: 6.8808, 4047: 18.1611, 4148: 0.2706, 4231: 3.0663, 4408: 7.5091, 4411: 16.9447, 4432: 1.8989, 4489: 1.1187, 4511: 5.4633, 4668: 6.2155, 4715: 6.236, 4726: 4.3626, 4744: 1.0334, 4847: 12.6289, 4905: 0.2692, 4909: 0.7787, 4919: 0.2698, 4988: 5.2805, 5034: 1.7437, 5159: 7.1352, 5294: 8.62, 5301: 2.4576, 5446: 7.9557, 5500: 4.7885, 5539: 2.0997, 5699: 6.4525, 5711: 2.686, 5838: 14.7359, 5984: 1.031, 6069: 0.6785, 6123: 2.2412, 6128: 7.6292, 6163: 4.7575, 6584: 6.3844, 6710: 16.6678, 6799: 2.1487, 6906: 3.1233, 6919: 5.2938, 7045: 10.5716, 7083: 2.8896, 7145: 6.9881, 7150: 0.2717, 7218: 4.8956, 7258: 2.812, 7350: 2.5186, 7464: 10.767, 7515: 6.5252, 7541: 5.1214, 7570: 3.7488, 7650: 13.5545, 7779: 7.5831, 7797: 1.3067, 7893: 6.1629, 7989: 1.2344, 8048: 5.7617, 8077: 5.2591, 8192: 3.3871, 8273: 3.8915, 8554: 2.1467, 8626: 6.048, 8728: 2.6205, 8813: 0.6714, 8941: 1.8943, 8996: 4.038, 9113: 0.2588, 9144: 3.0634, 9224: 9.4319, 9347: 3.3344, 9438: 6.9695, 9511: 2.7681, 9825: 1.7403, 9959: 34.0648})

print a.dot(b)

print sf.sqrt(a.dot(a) * b.dot(b) )

#rint a.dot(array([[1, 1], [2, 2], [3, 3], [4, 4]]))

#print cos