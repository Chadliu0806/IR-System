

class Node:
  def __init__(self, word=None, doc=None, row=None, next=None): 
    # store data
    self.word = word
    self.subject = {}
    self.subject[doc] = [row]
    # store the reference (next item)
    self.next = next
    return

 
class LinkedList:
    def __init__(self): 
        self.head = None
        self.tail = None
        return

    def add(self, word, doc, row):
        if (self.head == None):
            return self.append(word, doc, row)
        else:
            current_node = self.head
            while current_node != None:
                if (word == current_node.word):
                    if (doc in current_node.subject):
                        if row not in current_node.subject[doc]:
                            current_node.subject[doc].append(row)
                    else:
                        current_node.subject[doc] = [row]
                    return current_node
                else:
                    current_node = current_node.next
            # Not Found then create new node
            return self.append(word, doc, row)

    def Count(self):
        return len(self)

    def append(self, word, doc, row):
        new_node = Node(word, doc, row)

        if self.head == None:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node
            self.tail = self.tail.next
        return new_node

    def getNodedata(self, word):
        if len(self) == 0 or word =='':
            return -1
        else:
            current_node = self.head
            while current_node != None:
                if (current_node.word == word):
                    return current_node.subject
                else:
                    current_node = current_node.next
            return -1

    def deleteAll(self):
        current_node = self.head
        previuos_node = current_node
        while current_node != None:
            current_node = current_node.next
            previuos_node = None
        self.head = None
        self.tail = None

    def __len__(self):
        length = 0
        current_node = self.head
        while current_node != None:
            length += 1
            current_node = current_node.next
        return length
    