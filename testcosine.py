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



sc = SparkContext(appName="Example1")


tf_idf=SparseVector(10000, {15: 0.2668, 67: 3.0431, 69: 3.6234, 93: 2.6627, 315: 7.5103, 415: 3.9424, 419: 4.5356, 493: 2.399, 788: 0.2727, 858: 0.3938, 895: 4.1358, 945: 1.7267, 957: 1.3669, 1011: 2.2394, 1023: 3.8091, 1073: 2.3907, 1083: 0.3262, 1094: 11.0179, 1097: 0.4381, 1139: 2.6822, 1150: 8.2041, 1189: 0.5638, 1256: 17.5543, 1263: 8.5782, 1281: 8.8954, 1310: 9.1987, 1526: 4.8518, 1582: 7.1831, 1583: 2.3611, 1602: 4.7686, 1604: 6.4506, 1877: 2.3439, 2084: 7.3841, 2133: 7.3699, 2294: 18.0579, 2330: 3.8281, 2335: 3.8597, 2398: 6.3038, 2509: 8.6915, 2523: 1.7322, 2596: 1.2136, 2807: 7.3231, 3155: 2.3272, 3183: 3.782, 3297: 2.1537, 3365: 2.5824, 3484: 2.6546, 3526: 1.0074, 3646: 2.708, 3718: 0.6741, 3770: 31.9623, 3792: 2.0484, 3849: 1.842, 3911: 6.8935, 3992: 3.4249, 4003: 1.0705, 4020: 3.8975, 4034: 6.8808, 4047: 18.1611, 4148: 0.2706, 4231: 3.0663, 4408: 7.5091, 4411: 16.9447, 4432: 1.8989, 4489: 1.1187, 4511: 5.4633, 4668: 6.2155, 4715: 6.236, 4726: 4.3626, 4744: 1.0334, 4847: 12.6289, 4905: 0.2692, 4909: 0.7787, 4919: 0.2698, 4988: 5.2805, 5034: 1.7437, 5159: 7.1352, 5294: 8.62, 5301: 2.4576, 5446: 7.9557, 5500: 4.7885, 5539: 2.0997, 5699: 6.4525, 5711: 2.686, 5838: 14.7359, 5984: 1.031, 6069: 0.6785, 6123: 2.2412, 6128: 7.6292, 6163: 4.7575, 6584: 6.3844, 6710: 16.6678, 6799: 2.1487, 6906: 3.1233, 6919: 5.2938, 7045: 10.5716, 7083: 2.8896, 7145: 6.9881, 7150: 0.2717, 7218: 4.8956, 7258: 2.812, 7350: 2.5186, 7464: 10.767, 7515: 6.5252, 7541: 5.1214, 7570: 3.7488, 7650: 13.5545, 7779: 7.5831, 7797: 1.3067, 7893: 6.1629, 7989: 1.2344, 8048: 5.7617, 8077: 5.2591, 8192: 3.3871, 8273: 3.8915, 8554: 2.1467, 8626: 6.048, 8728: 2.6205, 8813: 0.6714, 8941: 1.8943, 8996: 4.038, 9113: 0.2588, 9144: 3.0634, 9224: 9.4319, 9347: 3.3344, 9438: 6.9695, 9511: 2.7681, 9825: 1.7403, 9959: 34.0648}), search_token=[u'door', u'bell'], tf=SparseVector(10000, {15: 1.0, 67: 1.0, 69: 1.0, 93: 1.0, 315: 2.0, 415: 1.0, 419: 2.0, 493: 1.0, 788: 1.0, 858: 1.0, 895: 2.0, 945: 1.0, 957: 1.0, 1011: 2.0, 1023: 1.0, 1073: 1.0, 1083: 1.0, 1094: 2.0, 1097: 1.0, 1139: 1.0, 1150: 2.0, 1189: 1.0, 1256: 3.0, 1263: 2.0, 1281: 2.0, 1310: 2.0, 1526: 4.0, 1582: 2.0, 1583: 2.0, 1602: 1.0, 1604: 1.0, 1877: 1.0, 2084: 1.0, 2133: 2.0, 2294: 4.0, 2330: 1.0, 2335: 1.0, 2398: 2.0, 2509: 3.0, 2523: 1.0, 2596: 2.0, 2807: 2.0, 3155: 1.0, 3183: 1.0, 3297: 1.0, 3365: 3.0, 3484: 1.0, 3526: 3.0, 3646: 1.0, 3718: 1.0, 3770: 5.0, 3792: 1.0, 3849: 1.0, 3911: 2.0, 3992: 1.0, 4003: 1.0, 4020: 1.0, 4034: 2.0, 4047: 3.0, 4148: 1.0, 4231: 2.0, 4408: 2.0, 4411: 3.0, 4432: 1.0, 4489: 2.0, 4511: 1.0, 4668: 1.0, 4715: 1.0, 4726: 1.0, 4744: 1.0, 4847: 7.0, 4905: 1.0, 4909: 1.0, 4919: 1.0, 4988: 1.0, 5034: 1.0, 5159: 1.0, 5294: 2.0, 5301: 1.0, 5446: 3.0, 5500: 2.0, 5539: 1.0, 5699: 2.0, 5711: 1.0, 5838: 3.0, 5984: 4.0, 6069: 1.0, 6123: 1.0, 6128: 1.0, 6163: 1.0, 6584: 1.0, 6710: 4.0, 6799: 1.0, 6906: 1.0, 6919: 1.0, 7045: 2.0, 7083: 1.0, 7145: 2.0, 7150: 1.0, 7218: 1.0, 7258: 2.0, 7350: 1.0, 7464: 4.0, 7515: 2.0, 7541: 1.0, 7570: 1.0, 7650: 3.0, 7779: 2.0, 7797: 1.0, 7893: 1.0, 7989: 1.0, 8048: 1.0, 8077: 2.0, 8192: 1.0, 8273: 2.0, 8554: 1.0, 8626: 1.0, 8728: 2.0, 8813: 1.0, 8941: 2.0, 8996: 1.0, 9113: 1.0, 9144: 1.0, 9224: 2.0, 9347: 2.0, 9438: 2.0, 9511: 1.0, 9825: 1.0, 9959: 8.0})
tf_idfs=SparseVector(10000, {4847: 3.0224, 9959: 6.4765})
cos = tf_idf.dot(tf_idfs) / (sf.sqrt(tf_idf.dot(tf_idf) * tf_idfs.dot(tf_idfs) ))
print cos