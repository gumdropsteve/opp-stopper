

class Stack:

    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            print("Mag is empty!")
            return None
        else:
            self.stack.pop()
            print("Pop!")
        
    def is_empty(self):
        return len(self.stack) == 0
    
    def size(self):
        return print("Mag Size: ", len(self.stack))
    
    def display(self):
        if self.is_empty():
            print("Empty Mag")
        else:
            print("Mag: ", self.stack)



if __name__=="__main__":
    clip = Stack()

    for i in range(1, 18):
        clip.push(i)

    clip.size()
    clip.display()
    print("Spray that Mug!!!!!")

    for i in range(3):
        clip.pop()

    clip.size()
    clip.display()
