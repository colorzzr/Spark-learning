import pyspark
from pyspark import SparkContext
sc =SparkContext()

nums= sc.parallelize([1,2,3,4])
print(nums.take(1))

squared = nums.map(lambda x: x*x).collect()
print(squared)
for num in squared:
    print('%i ' % (num))

from pyspark.sql import Row
from pyspark.sql import SQLContext

sqlContext = SQLContext(sc)
list_p = [('John',19),('Smith',29),('Adam',35),('Henry',50)]
rdd = sc.parallelize(list_p)

rdd.map(lambda x: Row(name=x[0], age=int(x[1])))

# sqlContext.createDataFrame(ppl)
list_p = [('John',19),('Smith',29),('Adam',35),('Henry',50)]
rdd = sc.parallelize(list_p)
print(rdd)
ppl = rdd.map(lambda x: Row(name=x[0], age=int(x[1])))
DF_ppl = sqlContext.createDataFrame(ppl)

DF_ppl.printSchema()