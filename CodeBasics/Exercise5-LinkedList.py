# Implement doubly linked list. The only difference with regular linked list is that double linked 
# has prev node reference as well. That way you can iterate in forward and backward direction. 
# Your node class will look this this,

class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


# Add following new methods,
# def print_forward(self):
#     This method prints list in forward direction. Use node.next

# def print_backward(self):
#     Print linked list in reverse direction. Use node.prev for this.

# Implement all other methods in regular linked list class and make necessary changes for 
# doubly linked list (you need to populate node.prev in all those methods)

class DoubleLikedList:
    def __init__(self):
        self.head = None

    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next
        return itr

    def get_length(self):
        itr = self.head
        count = 0
        while itr:
            itr = itr.next
            count += 1

        return count

    def print_forward(self):
        if self.head == None:
            print("List is empty")

        itr = self.head
        lstr = ''
        while itr:
            lstr += str(itr.data) + '-->'
            itr = itr.next
        print("Linked list in forward:", lstr)

    def print_backward(self):
        if self.head == None:
            print("List is empty")

        itr = self.get_last_node()
        lstr = ''
        while itr:
            lstr += str(itr.data) + '-->'
            itr = itr.prev
        print("Linked list in backward:", lstr)

    def insert_at_begining(self, data):
        if self.head == None:
            node = Node(data, self.head, None)
            self.head = node
        else:
            node = Node(data, self.head, None)
            self.head.prev = node
            self.head = node

    def insert_at_end(self, data):
        if self.head == None:
            self.head = Node(data, None, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None, itr)

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            print("Invalid Index")

        if index == 0:
            self.insert_at_begining(data)

        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                node = Node(data, itr.next, itr)
                if node.next:
                    node.next.prev = node
                itr.next = node
                break

            itr = itr.next
            count += 1

    def remove_at(self, index):
        if index < 0 or index > self.get_length():
            print("Invalid index")

        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.prev.next = itr.next
                if itr.next:
                    itr.next.prev = itr.prev
                break

            itr = itr.next
            count += 1

    def insert_values(self, data_list):
        for item in data_list:
            self.insert_at_end(item)

dl = DoubleLikedList()
dl.insert_at_begining(5)
dl.insert_at_begining(50)
dl.insert_at_end(11)
dl.insert_at(1, 45)
dl.insert_at(0, 75)
dl.print_forward()
dl.print_backward()

dl.remove_at(2)
dl.insert_values(['hello', 58, 'jack'])
dl.print_forward()
dl.print_backward()