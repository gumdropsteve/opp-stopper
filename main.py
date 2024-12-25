class Stack:
    """
    Load and fire a magazine using LIFO

    Tutorial: https://www.instagram.com/reel/DD0U5opvSDX/
    """

    def __init__(self):
        self.stack = []

    def push(self, item):
        """
        Push a round into the mag
        """
        self.stack.append(item)

    def pop(self):
        """
        Unload a round from the magazine
        """
        if self.is_empty():
            print("Mag is empty!")
            return None
        else:
            self.stack.pop()
            print("Pop!")
        
    def is_empty(self):
        """
        Check if the magazine is empty

        Returns True if magazine is empty
        """
        return len(self.stack) == 0
    
    def size(self):
        """
        Print out how many rounds are in the magazine
        """
        return print("Mag Size: ", len(self.stack))
    
    def display(self):
        """
        Print out the magazine
        """
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
