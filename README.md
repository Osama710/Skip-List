							#<<< SKIP LIST >>>

##Description:
	The skip list is a probabilisitc data structure that is built upon the general idea of a linked list. The skip list uses probability to build subsequent layers of linked lists upon an original linked list. Each additional layer of links contains fewer elements, but no new elements.

##For Example: 
You can think about the skip list like a subway system.
There's one train that stops at every single stop. However, there is also an express train. This train doesn't visit any unique stops, but it will stop at fewer stops. 
This makes the express train an attractive option if you know where it stops.

##Functions:
Skip List has the following Functions:

a) Insert(value) :
This function inserts the node of the given value in the List.

b) Delete(value) :
This function deletes nodeof the given value from the List.

c) Search(value) :
This function searches the node of the given value in the List and return if the element is present in the list or not.
	
d) PrintList() :
This functions displays a sorted Skip list with random levels of every node. 

##Time Complexity:

The complexity of a skip list is complicated due to its probabilistic nature. 
The Worst Case time complexity of different opertions are:

Average Case:
Indexing - O(log(n)),
Insertion - O(log(n)),
Search   - O(log(n)),
Deletion - O(log(n))

Worst case:
Indexing - O(n),
Insertion - O(n),
Search   - O(n),
Deletion - O(n)


##How To Run The Program:

Make an object of the SkipList class. For Example: list = SkipList().

It Will be an empty list at first.

Insert a node in the List using the Insert() Function by giving the value. For Example: lst.Insert(value), here value = 1,2,3...

Display the List using the PrintList() Function.

Delete a node from the List using the Delete() Function.

For Example: lst.Delete(value), here value = 1,2,3...


To search a node in the List, use the Search() Function.

For Example: lst.Search(value), here value = 1,2,3...

If the node is present in the list the function will return True.

If the node is not present in the list the function will return False.

##Group Members:

	Muhammad Arsal		18B-115-CS(A)
	Muhammad Osama		18B-003-CS(A)
	
