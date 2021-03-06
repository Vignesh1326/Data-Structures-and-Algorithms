#Queue is also and Linear Abstract Data Type used to store objects.
#Items added using enqueue and removed using dequeue.
#Objects inserted from one end and removed from another end.
#Visualized as Horizontal Collection.
#Uses two pointers (front, rear) which refers to the two ends.
#Follows First In First Out(FIFO) or Last In Last Out(LILO).
#Can be implemented using Arrays and Lists.

class Queue():
    def __init__(self,capacity):
        #max_q_size is the maximum or total capacity of the queue.
        self.q = []
        self.max_q_size = capacity
        for i in range(self.max_q_size):
            self.q.append(None)
        self.sz = 0
        #front gives the next index to be dequeued.
        self.f = 0
        #rear gives the index where the element is to be added.
        self.r = -1

    # Time Complexity: O(1)
    def enqueue(self,val):
        if(self.sz == self.max_q_size):
            print("The Queue is Full")
        else:
            self.r = (self.r + 1) % self.max_q_size
            self.q[self.r] = val
            self.sz += 1
        return

    # Time Complexity: O(1)
    def dequeue(self):
        if(self.sz == 0):
            print("Queue is Empty")
        else:
            self.q[self.f] = None
            self.f = (self.f + 1) % self.max_q_size
            self.sz -= 1
        return

    # Time Complexity: O(1)
    def size(self):
        return self.sz

    def front(self):
        if(self.sz == 0):
            print("Queue is Empty")
        else:
            return self.q[self.f]

    # Time Complexity: O(1)
    def isEmpty(self):
        if(self.sz == 0):
            print("True")
        else:
            print("False")

    # Time Complexity: O(max_q_size)
    def printqueue(self):
        if(self.sz == 0):
            print("Queue is Empty")
        else:
            for i in range(self.max_q_size):
                print(self.q[i],end=" ")
            

def testqueue():
    print("Enter the capacity of the Circular queue")
    cap = int(input())
    q = Queue(cap)
    print("Enter the number commands")
    commands = int(input())
    print("Enter the commands")
    while(commands > 0):
        com = input()
        op = com.split()
        if(op[0] == "SIZE"):
            print("Size of queue is: ",q.size())
        elif(op[0] == "ENQUEUE"):
            q.enqueue(int(op[1]))
            q.printqueue()
        elif(op[0] == "DEQUEUE"):
            q.dequeue()
            q.printqueue()
        elif(op[0] == "ISEMPTY"):
            q.isEmpty()
        elif(op[0] == "FRONT"):
            print(q.front())
        elif(op[0] == "PRINT"):
            q.printqueue()
        else:
            print("Enter a proper command")
        commands = commands - 1


def main():
    testqueue()

if __name__ == "__main__":
    main()
