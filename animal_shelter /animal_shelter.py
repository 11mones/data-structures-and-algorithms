class Queue:
    def __init__(self,front=None,back=None):
        self.front = front # first node in th queue
        self.back=back    # last node in queue    




    def enqueue(self, value):
        node = Node(value)
        if self.front is None:
            self.front = node
            self.back = node
        else:
            self.back.next = node
            self.back = node

    def dequeue(self):
        """
    Adds an element to the back of the queue.
    Argsument is the value to be added to the queue.
        """
        if self.front is None:
            raise Exception("The queue is empty, you cannot dequeue from it")
        else:
            temp = self.front
            self.front = temp.next
            if self.front is None:
                self.back = None
            temp.next = None
            return temp.data


    def peek(self):
        """
    Returns the value of the element at the front of the queue without removing it.
    Raises an Exception: If the queue is empty.
    Returns The value of the element at the front of the queue.

        """
        if self.front == None: 
            raise Exception("The queue is empty you can not peek from it")
        else : 
            return self.front.data
        

    def is_empty(self):
        if self.front == None: 
            return  "queue is empty"

    
    def __str__(self):
        current=self.front
        string=""
        while current:
            string+=f"{current.value}"
            string+=" -> "
            current=current.next
        return string+"None"  
    

class AnimalShelter:
    def __init__(self , species, name):
        self.species = species
        self.name = name
        self.shelter = Queue()

    def enqueue(self, animal):
        self.shelter.enqueue(animal)

    def dequeue(self, pref):
        temp_queue = Queue()
        if pref == "dog" or pref == "cat":
        
            while not self.shelter.is_empty():
                temp_queue.enqueue(self.shelter.dequeue())
                if temp_queue.back.species == pref:
                    return temp_queue.back.data
                

        # to restore the original queue
            while not temp_queue.is_empty():
                item = temp_queue.dequeue()
                self.shelter.enqueue(item)

        return None