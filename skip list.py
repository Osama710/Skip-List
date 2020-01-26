print(u"\u25A0"*70)
print("\nData Structures and Algorithm\nSemester III\nProject Title:\t\tSKIP LIST\n")
print(u"\u25A0"*70)
print("\nGroup Members:\nMuhammad Arsal\t18B-115-CS(A)\nMuhammad Osama\t18B-003-CS-(A)\n")

import random

# A Node class to create a node with a given value

class SkipNode:
    def __init__(self,value, level):
        self.value = value
        self.next = [None]*(level+1)

# A Skip List class with all the Functions.

class SkipList:
    def __init__(self):
        self.max_lvl = 99
        self.head = SkipNode(-99,self.max_lvl)
        self.level = 0

    # This RandomLevel Function creates Random Levels
    # using random number and a given probability
    
    def __RandomLevel(self):
        level = 0
        probability = 1
        while random.uniform(0,2) >= probability:
            level += 1
        return level


    # The Insert function inserts a node with a given value
    
    def Insert(self,value):
        update = self.__Update(value)
        head = self.head
        head = head.next[0]
        if head == None or head.value != value:
            random_level = self.__RandomLevel() 
            if random_level > self.level: 
                for z in range(self.level+1, random_level+1): 
                    update[z] = self.head
                self.level = random_level 
            node = SkipNode(value, random_level)
            for z in range(random_level+1): 
                node.next[z] = update[z].next[z] 
                update[z].next[z] = node
                
    def __Update(self,value):
        update = [None]*(self.max_lvl+1)
        head = self.head
        for x in reversed(range(len(update))):
            while head.next[x] and head.next[x].value < value:
                head = head.next[x]
            update[x] = head
        return update

    # The Delete function deletes a node with the given value
    
    def Delete(self,value):
        update = [None]*(self.max_lvl+1)
        head = self.head
        for x in reversed(range(len(update))):
            while head.next[x] and head.next[x].value < value:
                head = head.next[x]
            update[x] = head
        head = head.next[0]
        if head != None or head.value == value:
            for z in range(self.level+1):
                if update[z].next[z] != head:
                    break
                update[z].next[z] = head.next[z]

            while(self.level>0 and self.head.next[self.level] == None):
                self.level -= 1

    # The Search function searches the node with the given value in the list.
    # It returns True if the node is present in the Skip List.
    # It returns False if the node is not in the List.
    
    def Search(self,value):
        update = self.__Update(value)
        head = self.head
        for z in reversed(range(len(update))):
            while head.next[z] and head.next[z].value < value:
                head = head.next[z]
        head = head.next[0]
        if head and head.value == value:
            return True
        return False

    # PrintList Funciton is used to print the Skip List in a sorted way with random levels.

    def PrintList(self):
        print((u"\u25A0")*30+"SKIP LIST" + (u"\u25A0")*30)
        for level in range(self.level+1):
            print("Level {}: ".format(level), end = " ")
            node = self.head.next[level]
            while node != None:
                print(node.value,end=" ")
                node = node.next[level]
            print("")

if __name__ == "__main__":
    
    slst = SkipList()
    slst.Insert(3)
    slst.Insert(6)
    slst.Insert(8)
    slst.Insert(9)
    slst.Insert(2)
    slst.Insert(4)
    slst.Insert(5)
    slst.PrintList()
    print(slst.Search(4))
    slst.Delete(4)
    slst.PrintList()
    print(slst.Search(4))
    
