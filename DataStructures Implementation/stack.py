#Stack is an Linear Abstract Data Type used to store data or a collection of objects.
#Items can be added to stack using push operation.
#Items removed from stack using pop operation.
#Objects inserted and removed from same ends.
#Visualized as Vertical Collection.
#Uses only one pointer (top)
#Follows First In Last Out(FILO) or Last In First Out(LIFO).
#Can be implemented using lists or arrays.

class Stack():
    #max_cap gives the total capacity of stack.
    def __init__(self,size):    
        self.stack = []
        self.max_cap = size
        for i in range(self.max_cap):
            self.stack.append(None)
        #top gives the index of topmost element of stack.
        self.top = -1         

    # Time Complexity: O(1)    
    def size(self):
        return self.top+1

    # Time Complexity: O(1)
    def push(self,val): 
        if(self.size() == self.max_cap):
            print("Stack is Full")
        else:
            self.top = self.top + 1
            self.stack[self.top] = val
        return
    # Time Complexity: O(1)
    def pop(self):
        if(self.size() == 0):
            print("Stack is Empty")
        else:
            self.stack[self.top] = None
            self.top = self.top - 1
        return
    # Time Complexity: O(stack_capacity)
    def printstack(self):
        if(self.size() == 0):
            print("Stack is Empty")
        else:
            for i in range(self.max_cap):
                if(self.stack[i] != None):
                    print(self.stack[i], end=" ")
        return
    # Time Complexity: O(1)
    def isEmpty(self):
        if(self.size() == 0):
            print("True")
        else:
            print("False")
        return
    
    # Time Complexity: O(1)
    def s_top(self):
        if(self.size() == 0):
            print("Stack is Empty")
            return
        else:
            return (self.stack[self.top])
    
def teststack():
    print("Enter the capacity of the stack")
    cap = int(input())
    s = Stack(cap)
    print("Enter the number of commands")
    com = int(input())
    print("Enter your commands")
    while(com > 0):
        command = input()
        op=command.split()
        if(op[0] == "SIZE"):
            print("Size of stack is: ",s.size()
        elif(op[0] == "PUSH"):
            s.push(int(op[1]))
            s.printstack()
        elif(op[0] == "POP"):
            s.pop()
            s.printstack()
        elif(op[0] == "ISEMPTY"):
            s.isEmpty()
        elif(op[0] == "TOP"):
            print(s.s_top())
        elif(op[0] == "PRINT"):
            s.printstack()
        else:
            print("Enter a proper command")
        com = com - 1


def main():
    teststack()

if __name__  == '__main__':
    main()
