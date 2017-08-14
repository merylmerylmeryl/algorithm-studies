class PriorityQueue (object) :

    def __init__(self, size=0, queue=[]):
        self.size = size
        self.queue = queue
        self.min = None
        self.findMin()


    def insert(self, value):
        ''' Check the value in question
            If this value is smaller than the min,
            make it the new min.
            Otherwise stick it at the end.
        '''
        if len(self.queue) > 0:
            if value < self.min:
                self.queue.append(self.min)
                self.queue[0] = value
                self.min = value
            else:
                self.queue.append(value)
        else:
            self.queue.append(value)
            self.min = value

    def delete(self, value):
        for i in self.queue:
            if i == value:
                self.queue.remove(value)
        self.findMin()

    def findMin(self):
        if len(self.queue) == 0:
            return None
        else:
            i = 0
            while i < len(self.queue):
                if self.queue[i] < self.queue[0]:
                    moveMe = self.queue[0]
                    self.queue[0] = self.queue[i]
                    self.queue[i] = moveMe
                i += 1
            self.min = self.queue[0]
                    
        

    def __str__(self):
        return str(self.queue)


    
myQueue = PriorityQueue(10, [40,5,3,4,7,18,3,30,90,22])
print('myQueue: ' + str(myQueue))
print('min: ' + str(myQueue.min))
myQueue.insert(1)
print('After inserting 1: ' + str(myQueue))


print('\n')

insQueue = PriorityQueue()
print('insQueue: ' + str(insQueue))
insQueue.insert(54)
print('After inserting 12: ' + str(insQueue))
print('The smallest value in insQueue is: ' + str(insQueue.min))
insQueue.insert(2)
print('After inserting 2: ' + str(insQueue))
print('The smallest value in insQueue is: ' + str(insQueue.min))
insQueue.insert(12)
print('After inserting 12: ' + str(insQueue))
print('The smallest value in insQueue is: ' + str(insQueue.min))
insQueue.delete(2)
print('After deleting 2: ' + str(insQueue))
print('The smallest value in insQueue is: ' + str(insQueue.min))
print('insQueue: ' + str(insQueue))
print('The smallest value in insQueue is: ' + str(insQueue.min))
insQueue.insert(90)
print('insQueue: ' + str(insQueue))
insQueue.insert(1)
print('insQueue: ' + str(insQueue))
insQueue.insert(15)
print('insQueue: ' + str(insQueue))
print('The smallest value in insQueue is: ' + str(insQueue.min))
