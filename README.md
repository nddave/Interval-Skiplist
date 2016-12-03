# Interval Skiplist

![alt tag](https://raw.githubusercontent.com/nddave/Interval-Skiplist/master/Interval%20Skiplist.png)

Implementation of Integer-Set-With-Next-Excluded ADT that uses a skiplist with an integer range per node in the skiplist.

## Adding data
A skiplist usually includes one set of data per node, here the skiplist includes a range of data per node. Therefore, for this skiplist implementation, imagine adding integer "1" to the skiplist, it will create a new node. Then adding integer "3" to the skiplist will create a new node. However, now, adding the integer "2" to the skiplist, will merge the two nodes into one node, with data "(1, 3)" which represents the range of values in the skiplist. Here, adding "4" will change the current node's data to "(1, 4)". And then adding "9", will create a totally new node. Below is a basic representation of how add-merging works in this program.

```python
# Adding 1
{(1)}
# Adding 3
{(1), (3)}
# Adding 2
{(1, 3)}
# Adding 4
{(1, 4)}
# Adding 9
{(1, 4), (9)}
```

## Deleting data
And the same goes for the delete function. Deleting "9", will have no impact on any other nodes. And deleting "1", will change the respective node's range from "(1, 4)" to "(2, 4)". However, if there exists a node K, such that the data in node K is "(1, 7)", then deleting "4", will split node K into two parts. Node K1, with data "(1, 3)" and Node K2 with data "(5, 7)". Below is a basic representation of how delete-splitting works in this program.

```python
skiplist = {(1, 4), (9)}
# Removing 9 from skiplist
{(1, 4)}
# Removing 1 from sliplist
{(2, 4)}

skiplist_nodeK = {(1, 7)}
# Removing 4 from skiplist_nodeK
{(1, 3), (5, 7)}
```

# Use case

Next excluded function. This function, given a number gives the next number in a skiplist that is missing. Therefore, imagine a conventional skiplist with three nodes as follows:
```python
conv_skiplist = {(1), (2), (3), (4), (5)}
```
And if we run the next excluded function on the conventional skiplist, node (1). Then, the function will first find the node 1 *(in O(log(n)) time)* and then calculate the next immediate number after "1", which is "2" and check if "2" exists in the conv_skiplist. If it doesn't, it will simply return the value. However, if the number "2" does exist in the conv_skiplist, it will increment the value by 1 *(which here, is "3")* and will check again. Until it reaches to incremented value of "6", and finds that "6" does not exist in the conv_skiplist, and returns "6". This process can end up taking O(n) time in worst case. 

Therefore, this implementation of Integer-Set-With-Next-Excluded ADT is created.
```python
new_skiplist = {(1, 5)}
```
Since, the nodes are merged, the next excluded function works in O(1) time, instead of O(n). When we run next excluded function on "1", it will first find the respective node *(in O(log(n)) time)* and then will simply look at the end value of that node and return a value which is one more than the end value. Therefore, an execution of next excluded function on "1", will find the node "(1, 5)" and return node.end+1 which here is "6". 

# Getting started

[Interval Skiplist](https://github.com/nddave/Interval-Skiplist/blob/master/skiplist.py) is quick and easy to setup. You do not need any additional libraries than the ones built into Python3. So, download the Interval-Skiplist.zip file, change directory to the Interval Skiplist folder and run it with the following command:

```python
python3 skiplist.py
```

It will automatically add values, defined in the main method, to the skiplist. Feel free to edit the main method. And it will also give an output with next excluded at each step. Below is an example of the output for adding values to the skiplist.

Input
```python
ints = [2, 1, 4, 6, 8, 3, 9, 10, 5, 7]
```

Output
```python
===ADDING 2 ===
<2; 2; 2>
<2; 2; 2>
next_excluded(0) = 0
next_excluded(1) = 1
next_excluded(2) = 3
next_excluded(3) = 3
next_excluded(4) = 4
next_excluded(5) = 5
next_excluded(6) = 6
next_excluded(7) = 7
next_excluded(8) = 8
next_excluded(9) = 9
next_excluded(10) = 10
next_excluded(11) = 11
===ADDING 1 ===
<1; 2; 2>
<1; 2; 2>
next_excluded(0) = 0
next_excluded(1) = 3
next_excluded(2) = 3
next_excluded(3) = 3
next_excluded(4) = 4
next_excluded(5) = 5
next_excluded(6) = 6
next_excluded(7) = 7
next_excluded(8) = 8
next_excluded(9) = 9
next_excluded(10) = 10
next_excluded(11) = 11
===ADDING 4 ===
<1; 2; 2>
<1; 2; 2><4; 4; 1>
<1; 2; 2><4; 4; 1>
next_excluded(0) = 0
next_excluded(1) = 3
next_excluded(2) = 3
next_excluded(3) = 3
next_excluded(4) = 5
next_excluded(5) = 5
next_excluded(6) = 6
next_excluded(7) = 7
next_excluded(8) = 8
next_excluded(9) = 9
next_excluded(10) = 10
next_excluded(11) = 11
===ADDING 6 ===
<1; 2; 2>
<1; 2; 2><4; 4; 1>
<1; 2; 2><4; 4; 1><6; 6; 1>
<1; 2; 2><4; 4; 1><6; 6; 1>
next_excluded(0) = 0
next_excluded(1) = 3
next_excluded(2) = 3
next_excluded(3) = 3
next_excluded(4) = 5
next_excluded(5) = 5
next_excluded(6) = 7
next_excluded(7) = 7
next_excluded(8) = 8
next_excluded(9) = 9
next_excluded(10) = 10
next_excluded(11) = 11
===ADDING 8 ===
<1; 2; 2>
<1; 2; 2><4; 4; 1>
<1; 2; 2><4; 4; 1><6; 6; 1>
<1; 2; 2><4; 4; 1><6; 6; 1><8; 8; 1>
<1; 2; 2><4; 4; 1><6; 6; 1><8; 8; 1>
next_excluded(0) = 0
next_excluded(1) = 3
next_excluded(2) = 3
next_excluded(3) = 3
next_excluded(4) = 5
next_excluded(5) = 5
next_excluded(6) = 7
next_excluded(7) = 7
next_excluded(8) = 9
next_excluded(9) = 9
next_excluded(10) = 10
next_excluded(11) = 11
===ADDING 3 ===
<1; 4; 2>
<1; 4; 2><6; 6; 1>
<1; 4; 2><6; 6; 1><8; 8; 1>
<1; 4; 2><6; 6; 1><8; 8; 1>
next_excluded(0) = 0
next_excluded(1) = 5
next_excluded(2) = 5
next_excluded(3) = 5
next_excluded(4) = 5
next_excluded(5) = 5
next_excluded(6) = 7
next_excluded(7) = 7
next_excluded(8) = 9
next_excluded(9) = 9
next_excluded(10) = 10
next_excluded(11) = 11
===ADDING 9 ===
<1; 4; 2>
<1; 4; 2><6; 6; 1>
<1; 4; 2><6; 6; 1><8; 9; 1>
<1; 4; 2><6; 6; 1><8; 9; 1>
next_excluded(0) = 0
next_excluded(1) = 5
next_excluded(2) = 5
next_excluded(3) = 5
next_excluded(4) = 5
next_excluded(5) = 5
next_excluded(6) = 7
next_excluded(7) = 7
next_excluded(8) = 10
next_excluded(9) = 10
next_excluded(10) = 10
next_excluded(11) = 11
===ADDING 10 ===
<1; 4; 2>
<1; 4; 2><6; 6; 1>
<1; 4; 2><6; 6; 1><8; 10; 1>
<1; 4; 2><6; 6; 1><8; 10; 1>
next_excluded(0) = 0
next_excluded(1) = 5
next_excluded(2) = 5
next_excluded(3) = 5
next_excluded(4) = 5
next_excluded(5) = 5
next_excluded(6) = 7
next_excluded(7) = 7
next_excluded(8) = 11
next_excluded(9) = 11
next_excluded(10) = 11
next_excluded(11) = 11
===ADDING 5 ===
<1; 6; 2>
<1; 6; 2><8; 10; 1>
<1; 6; 2><8; 10; 1>
next_excluded(0) = 0
next_excluded(1) = 7
next_excluded(2) = 7
next_excluded(3) = 7
next_excluded(4) = 7
next_excluded(5) = 7
next_excluded(6) = 7
next_excluded(7) = 7
next_excluded(8) = 11
next_excluded(9) = 11
next_excluded(10) = 11
next_excluded(11) = 11
===ADDING 7 ===
<1; 10; 2>
<1; 10; 2>
next_excluded(0) = 0
next_excluded(1) = 11
next_excluded(2) = 11
next_excluded(3) = 11
next_excluded(4) = 11
next_excluded(5) = 11
next_excluded(6) = 11
next_excluded(7) = 11
next_excluded(8) = 11
next_excluded(9) = 11
next_excluded(10) = 11
next_excluded(11) = 11
```

# License information ![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)

This work is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/). 

Program is created by [Nirman Dave](http://www.nirmandave.com) as a form of assignment for *Data Structures and Algorithms 2 COSC301* course at *Amherst College, Amherst MA* under *Professor James Glenn*.
