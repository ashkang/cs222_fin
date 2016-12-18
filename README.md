# Generate a test-case

`./generate 1.in 10 10 2`
Generates two matrices 10x10 and 10x2

# Vanilla multiplier

`cat example.in | ./matrix.py`

# Testing

`cat example.in | ./mapper.py | sort | ./reducer.py`

# How it works
Consider we want to multiply two matrices, M(m*n) and N(n*p). This results in a matrix like P(m*p).
Matrix P has m*p elements, therefore we have m*p reducers. Each element from matrix M participates exactly p times in key-value generation.
Each element from matrix N participates exactly m times in key-value generation.

Each time we visit an element from matrix M or N, we generate all key-value pairs necessary for reducers.

# Performance Considerations
Our mapping algorithm can be optimized to facilitate reading inputs that have array index already instead of calculating one at run-time. This
gives us the benefit of gaining the ability to run multiple mappers which drastically increases our load time in case of very large inputs.
However, the trade-off is, our input files will become larger in size. We can optimize that out by leaving off elements that our zero since
most of the matrices in real-life are sparce matrices.

# Testing with Apache Hadoop

`hadoop jar /lib/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar -file mapper.py -mapper mapper.py -file reducer.py -reducer reducer.py -input example.in -output example.out`

**NOTE**
The path to hadoop-streaming jar file might be different on your system.
