# Paging-Techniques
Demonstrates the 3 main Paging Techniques used in Operating Systems: Optimal, LRU and FIFO

A web-application using Streamlit which demonstrates the Optimal, LRU and FIFO Paging Techniques. 
Based on the requests made by the user, it shows step-by-step when page-fault occurs and how it is resolved.

The OS keeps record of all pages in the memory in a queue, when the maximum limit of length of queue is reached:
1)FIFO - The oldest page is replaced
2)LRU - The least recently used page is replaced
3)Optimal - The page that is going to be re-demanded after the longest time duration is replaced

Ideally, Optimal is the best Algorithm with the least number of page-faults but it is not possible to predict the future requests of the CPU and so remains only a theoritical concept

Currently, LRU is the most efficient, practically-possible algorithm
