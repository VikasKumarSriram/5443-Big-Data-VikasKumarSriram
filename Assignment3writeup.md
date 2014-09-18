
![](http://107.170.187.103/BigData/Assignment3.png)

Q1. How do you add nodes to your Hadoop cluster? 

Answer:

To startup a Namenode, Datanode, Jobtracker and a Tasktracker on your machine. Run the following command.

```hduser@ubuntu:~$ /usr/local/hadoop/bin/start-all.sh

To check whether the Hadoop is running use the jps command 

```root@ubuntu:/usr/local/hadoop$ jps

```2287 TaskTracker

```2149 JobTracker

```1938 DataNode

```2085 SecondaryNameNode

```2349 Jps

```1788 NameNode

You can examine the log file to check for the errors in /logs/ directory.

reference: http://www.michael-noll.com/tutorials/running-hadoop-on-ubuntu-linux-single-node-cluster/


Q2. Can everyone simultaneously run thier own Hadoop cluster, AND be a slave (worker) in another Hadoop cluster?

Answer:

Yes, everyone can simultaneously run their own hadoop cluster and be a slave in another hadoop cluster. That can be done by running the commands shown in the following link.

http://www.michael-noll.com/tutorials/running-hadoop-on-ubuntu-linux-multi-node-cluster/


