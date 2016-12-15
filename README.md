# Generate a test-case

`./generate 1.in 10 10 2`
Generates two matrices 10x10 and 10x2

# Vanilla multiplier

`cat example.in | ./matrix.py`

# Testing

`cat example.in | ./mapper.py | ./reducer.py`

# Testing with Apache Hadoop

`hadoop jar /lib/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar -file mapper.py -mapper mapper.py -file reducer.py -reducer reducer.py -input example.in -output example.out`

**NOTE** 
The path to hadoop-streaming jar file might be different on your system.
