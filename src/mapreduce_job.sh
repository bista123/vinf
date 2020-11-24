#!/bin/bash

# remove old output files
#hdfs dfs -rm -r output/labels
#hdfs dfs -rm -r output/ids
#hdfs dfs -rm -r output/categories
#hdfs dfs -rm -r output/links
#hdfs dfs -rm -r output/final
hdfs dfs -rm -r input
hdfs dfs -rm -r output

# put input files to hdfs
hdfs dfs -mkdir input
hdfs dfs -mkdir output
#hdfs dfs -put labels_sample.ttl input/labels_sample.ttl
#hdfs dfs -put page_ids_sample.ttl input/page_ids_sample.ttl
#hdfs dfs -put article_categories_sample.ttl input/article_categories_sample.ttl
#hdfs dfs -put page_links_sample.ttl input/page_links_sample.ttl
hdfs dfs -put labels_sk.ttl input/labels_sk.ttl
hdfs dfs -put page_ids_sk.ttl input/page_ids_sk.ttl
hdfs dfs -put article_categories_sk.ttl input/article_categories_sk.ttl
hdfs dfs -put page_links_sk.ttl input/page_links_sk.ttl

# run labels mapreduce job
#hadoop jar /hadoop-2.8.2/share/hadoop/tools/lib/hadoop-streaming-2.8.2.jar -file ./label_mapper.py -mapper ./label_mapper.py -file ./label_reducer.py -reducer ./label_reducer.py -input input/labels_sample.ttl -output output/labels
hadoop jar /hadoop-2.8.2/share/hadoop/tools/lib/hadoop-streaming-2.8.2.jar -file ./label_mapper.py -mapper ./label_mapper.py -file ./label_reducer.py -reducer ./label_reducer.py -input input/labels_sk.ttl -output output/labels

# run ids mapreduce job
#hadoop jar /hadoop-2.8.2/share/hadoop/tools/lib/hadoop-streaming-2.8.2.jar -file ./id_mapper.py -mapper ./id_mapper.py -file ./id_reducer.py -reducer ./id_reducer.py -input input/page_ids_sample.ttl -output output/ids
hadoop jar /hadoop-2.8.2/share/hadoop/tools/lib/hadoop-streaming-2.8.2.jar -file ./id_mapper.py -mapper ./id_mapper.py -file ./id_reducer.py -reducer ./id_reducer.py -input input/page_ids_sk.ttl -output output/ids

# run categories mapreduce job
#hadoop jar /hadoop-2.8.2/share/hadoop/tools/lib/hadoop-streaming-2.8.2.jar -file ./category_mapper.py -mapper ./category_mapper.py -file ./category_reducer.py -reducer ./category_reducer.py -input input/article_categories_sample.ttl -output output/categories
hadoop jar /hadoop-2.8.2/share/hadoop/tools/lib/hadoop-streaming-2.8.2.jar -file ./category_mapper.py -mapper ./category_mapper.py -file ./category_reducer.py -reducer ./category_reducer.py -input input/article_categories_sk.ttl -output output/categories

# run links mapreduce job
#hadoop jar /hadoop-2.8.2/share/hadoop/tools/lib/hadoop-streaming-2.8.2.jar -file ./link_mapper.py -mapper ./link_mapper.py -file ./link_reducer.py -reducer ./link_reducer.py -input input/page_links_sample.ttl -output output/links
hadoop jar /hadoop-2.8.2/share/hadoop/tools/lib/hadoop-streaming-2.8.2.jar -file ./link_mapper.py -mapper ./link_mapper.py -file ./link_reducer.py -reducer ./link_reducer.py -input input/page_links_sk.ttl -output output/links

# run final mapreduce job
hadoop jar /hadoop-2.8.2/share/hadoop/tools/lib/hadoop-streaming-2.8.2.jar -file ./final_mapper.py -mapper ./final_mapper.py -file ./final_reducer.py -reducer ./final_reducer.py -input output/labels/* output/ids/* output/categories/* output/links/* -output output/final

# display final output
#hdfs dfs -cat /output/final/part-00000

# get final output from hdfs
hdfs dfs -get /output/final/*

