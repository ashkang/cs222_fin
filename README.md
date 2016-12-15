# Testing

`cat example.in | ./mapper.py | ./reducer.py`

# Testing with Apache Hadoop

`hadoop jar /lib/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar -file mapper.py -mapper mapper.py -file reducer.py -reducer reducer.py -input example.in -output example.out`

**NOTE** 
The path to hadoop-streaming jar file might be different on your system.
