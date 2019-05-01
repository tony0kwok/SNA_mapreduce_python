# SNA_mapreduce_python
Welcome!This is social network analysis with mapreduce written in python.
Before you study this project, please make sure you have downloaded [Python](https://www.python.org/downloads/ "悬停显示") in your machine.

Please do install MRJob package by pip first
```Bash
pip install mrjob
```

Then you should clone the project. You can do it by typing following in your shell
```Bash
git clone https://github.com/tony0kwok/SNA_mapreduce_python.git
```

File Purpose
---------
Here is the function of file in this project.

File name | type | purpose
---------|---------|--------
faker.py|python executable|Generate random graph
dc_mapreduce.py|python executable|MRJob program implemented mapper and reducer that output the analysis result. Main program file we focus on.
sample_input.txt|text|Input file for testing the analysis function
random_graph|folder|Contains input data and analysis output. There are 4 pre-generatd random graphs G(n, p) which has 10000 nodes (n=10000). The graphs have p=0.1, p=0.5, p=0.75, p=1 respectively.
Marvel (the comic)|folder|Contains Marvel character dataset and its analysis output
GOT|folder|Contains Game of Thrones character dataset and its analysis output

Faker
-----------
The faker.py take 3 argument: the number of the output graph, the p and the name of the output file.
```Bash
python faker.py [NODES_NUMBER] [P] [OUTPUT_FILE_NAME:optional]
```
OUTPUT_FILE_NAME is optional. If you leave it blank, the program will save the output as "edge_list.txt"

Besides, P shows that the output graph will have (number of nodes)*(number of nodes-1)/2*P

For example, the following generate a random edge list saved as "output_graph.txt". The generated graph has 100 nodes and 100*(100-1)/2*0.1 = 495 edges.
```Bash
python faker.py 10000 0.1
```

MRJob
----------
Try the following command.
```Bash
python dc_mapreduce.py sample_input.txt
```
If your MRJob work fine, you shall see something like this:
```
No configs found; falling back on auto-configuration
No configs specified for inline runner
Creating temp directory /tmp/dc_mapreduce.csci3150.20190501.030849.157280
Running step 1 of 1...
job output is in /tmp/dc_mapreduce.csci3150.20190501.031555.251975/output
Streaming final output from /tmp/dc_mapreduce.csci3150.20190501.031555.251975/output...
0 49
1 49
.
.
.
.
```
If you see this, it means your MRJob is working. Congratulation:)

The output here showed every nodes in "sample_input.txt" has the degree centrality 49. The first one is the node id, start with 0. 
The second one is the degree centrality of that node. Since "sample_input.txt" saved a complete graph with 50 nodes, so every node has 49 degree centrality.

Now Try this
```Bash
python dc_mapreduce.py random_graph/10000_p0.10
```
This step will take a while, around 2 minutes. It depends on the machine.

That will output the analysis of a G(10000,0.1) graph.

If every thing is fine with you now, good, we are about to do the analysis on cloud!

MRjob allow you to do mapreduce in Goodle Cloud Dataproc
```Bash
python dc_mapreduce.py -r dataproc sample_input.txt
```
The code above does not work because we haven't set up the dataproc environment.

Please following the intruction below to do the set up. If you have any problem, seek answer in [this site](https://pythonhosted.org/mrjob/guides/dataproc-quickstart.html)

* Configuring your GCP credentials allows mrjob to run your jobs on Dataproc and use GCS.

- [Create a Google Cloud Platform account](https://cloud.google.com/), see top-right

* [Learn about Google Cloud Platform “projects”](https://cloud.google.com/docs/overview/#projects)

- [Select or create a Cloud Platform Console project](https://console.cloud.google.com/cloud-resource-manager)

* [Enable billing for your project](https://console.cloud.google.com/billing)--there are free money quota when you firstly sign up for Google Cloud, as I recall

- Go to the [API Manager](https://console.cloud.google.com/apis) and search for / enable the following APIs...

  * Google Cloud Storage
  - Google Cloud Storage JSON API
  * Google Cloud Dataproc API

* Under Credentials, Create Credentials and select Service account key. Then, select New service account, enter a Name and select Key type JSON.
Install the Google Cloud SDK

***[IMPORTANT]*** After you have download a credential, you have to declare it every time you start a new shell to process!!!!
you can always do this by typing:
```Bash
export GOOGLE_APPLICATION_CREDENTIALS="[CREDENTIAL_PATH]"
```

Now you should able to use dataproc to increase the computing speed
```Bash
python dc_mapreduce.py -r dataproc random_graph/10000_p1.00
```
If you want to be faster, you can type the following to include more machines in your cluster
```Bash
python dc_mapreduce.py -r dataproc –num-task-instances 4 random_graph/10000_p1.00
```

You can see more options in [MRJob Documentation](https://pythonhosted.org/mrjob/guides/configs-reference.html#additional-options-for-dataprocjobrunner), have fun.
