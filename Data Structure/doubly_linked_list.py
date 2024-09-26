class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_start(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = new_node
        new_node.prev = itr

    def insert_value(self, data_list):
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        itr = self.head
        count = 1
        while itr.next:
            itr = itr.next
            count += 1
        return count

    def index_at(self, index, data):
        if index < 0 and index >= self.get_length():
            raise Exception("Invalid list")
        if index == 0:
            self.insert_at_start(data)
        else:
            itr = self.head
            count = 0
            while itr:
                if count == index - 1:
                    new_node = Node(data, itr, itr.next)
                    itr.next = new_node
                    break
                itr = itr.next
                count += 1

    def remove_index(self, index):
        if index < 0 and index >= self.get_length():
            raise Exception("Invalid list")
        if index == 0:
            self.head = self.head.next
        else:
            itr = self.head
            count = 0
            while itr:
                if count == index - 1:
                    itr.next = itr.next.next
                    itr.next.prev = itr
                    break
                itr = itr.next
                count += 1

    def print_list(self):
        if self.head is None:
            print("List is empty")
        itr = self.head
        ll = ''
        while itr:
            ll += str(itr.data) + '-->'
            itr = itr.next
        print(ll)


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_value([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    ll.print_list()
    ll.insert_at_start(99)
    ll.insert_at_end(100)
    print("Length of the list : ", ll.get_length())
    ll.print_list()
    ll.index_at(2, 11)
    ll.remove_index(5)
    ll.print_list()