 **Sorting Algorithms Implemented**\
 Insertion sort shifts each element from the unsorted portion of the array to the sorted
 portion. Merge sort takes advantage of the divide and conquer paradigm to merge sorted left
 and right portions of the array. Shell sort 1, 2, 3, and 4 is similar to insertion sort in that it shifts
 each element towards their correct position. However, shell sort adds a decreasing gap
 parameter that determines the distance of these shifts. Each version has a different gap
 sequence. Hybrid sort 1, 2, and 3 is a combination of merge sort and insertion sort. When the
 array reaches a small threshold size, insertion sort is instead used. Each progressive version
 increases this threshold.
 
 **Input Data and its Distributions**\
 The primary set of growing input sizes utilized in this running-time experiment are 512,
 1024, 2048, 4096, 8192, 16384, and 32768. Furthermore, the three input distributions are
 uniform distributions, almost-sorted distributions, and reverse-sorted distributions. The uniform
distribution is computed using the Fisher-Yates shuffle. Subsequently, the almost-sorted
 distribution is computed by starting with a sorted input and randomly choosing 2*log n pairs to
 swap. Lastly, the reverse-sorted distribution is computed using the reverse function
