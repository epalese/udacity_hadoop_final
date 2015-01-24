# Intro to Hadoop and MapReduce - Final Project


This repository contains all the python scripts developed for the Udacity course Intro to Hadoop and MapReduce.

In the following part of the document a brief description of the exercises will be provided and the corresponding python scripts used to implement the solution to the excercise. 

All the exercises are based on the data that can be found in data/forum_data.tar.gz

## Students and Posting Time on Forums
Find for each student what is the hour during which the student has posted the most posts.
- mapper: student_times_mapper.py
- reducer: student_times_reducer.py

## Post and Answer Length
Write a mapreduce program that would process the forum_node data and output the length of the post and the average answer (just answer, not comment) length for each post.
- mapper: average_length_mapper.py
- reducer: average_length_reducer.py

## Top Tags
Write a mapreduce program that would output Top 10 tags, ordered by the number of questions they appear in.
- mapper: popular_tags_mapper.py
- reducer: popular_tags_reducer.py

As an extra challenge a Top 10 tags list will be produced using the where the count of tag is weighted by ratio of users that used that with respect to all the considered user base (that is all the users that used a tag):

    T = (tag count) * (number of users that used the tag) / (number of all users that used a tag)

For example, if the output of the mapper will be:
  tag1  user1
  tag1  user2
  tag1  user2
  tag2  user1
  tag2  user2
  tag2  user3
  
The value of T will be:
  T(tag1) = 3 * (2 / 3) = 2
  T(tag2) = 3 * (3 / 3) = 3
  
- mapper: [optional]popular_tags_extra_mapper.py
- reducer: [optional]popular_tags_extra_reducer.py
