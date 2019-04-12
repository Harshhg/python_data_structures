class Queue:
    def __init__(self):
        self.capacity = 5
        self.front=0
        self.rear = self.capacity-1
        self.size=0         #to check the number of elements in queue 0 = empty
        self.Q = [None]*(self.capacity)       #initializing list with total size of queue (5 here)

    def insert(self, item):
        if(self.size==5):
            print("Full")
            return
        self.rear = (self.rear + 1) % (self.capacity) #incrementing rear
        self.Q[self.rear]=item      #inserting element in the Q list at rear position
        self.size+=1                #incrementing the size of the queue
        print("inserted in the Queue")

    def delete(self):
        if(self.size==0):
            print("Empty")
            return
        self.front = (self.front +1 ) % (self.capacity)         #incrementing front because element is deleted
        self.size-=1                #reducing the size of the queue after deletion
        print("Deleted From Queue")

    def printqueue(self):
        self.temp =self.front;
        while(self.temp<=self.rear):
            print(self.Q[self.temp])
            self.temp+=1

queue = Queue()
queue.insert(10)
queue.insert(20)
queue.insert(30)
queue.printqueue();
queue.delete()
queue.printqueue();
