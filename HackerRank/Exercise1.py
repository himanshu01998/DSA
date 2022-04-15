class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(head):
    st = ''
    while head:
        st += str(head.data) + '-->' if head.next else str(head.data)
        head = head.next
    print(st)

def removeDuplicates(llist):
    # Write your code here
    while llist:
        if llist.next is None:
            break

        if llist.data == llist.next.data:
            llist.next = llist.next.next
        llist = llist.next
    return llist

if __name__ == '__main__':

    llist_count = int(input())
    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    removeDuplicates(llist.head)
