# COEN498 PP (Cloud Computing) Assignment 2
## Assignment 2: Hadoop MapReduce on Large Data Set

### Running the application
This application is intended to be run using the Hadoop Streaming functionality that enables applications to interact with the Hadoop MapReduce framework through STDIN/STDOUT.
To test the scripts, simply run the "test.sh" script. This mimicks what Hadoop does at a smaller scale, using standard stream pipes.
To run the application on a Hadoop cluster, refer to the "test.csh" script. To ensure it works, "hadoop" should be in your $PATH or aliased to the actual hadoop distribution binary. Similarly, "HADOOP_DIR" must be defined in your environment (this should be the folder where the hadoop installation is)