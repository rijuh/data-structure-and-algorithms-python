class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_start(self, data):
        new_node = Node(data, self.head)
        self.head = new_node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def insert_at(self, index, data):
        if index < 0 and index >= self.get_length():
            raise Exception("Invalid index")

        if index == 0:
            self.insert_at_start(data)

        else:
            itr = self.head
            count = 0
            while itr:
                if count == index - 1:
                    new_node = Node(data, itr.next)
                    itr.next = new_node
                    break
                itr = itr.next
                count += 1

    def remove_index(self, index):
        if index < 0 and index >= self.get_length():
            raise Exception("Invalid index")

        if index == 0:
            self.head = self.head.next

        else:
            count = 0
            itr = self.head
            while itr:
                if count == index - 1:
                    itr.next = itr.next.next
                    break
                itr = itr.next
                count += 1

    def get_length(self):
        itr = self.head
        count = 0
        while itr:
            itr = itr.next
            count += 1
        return count

    def print_list(self):
        if self.head is None:
            print("Linked List is empty")
            return

        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next

        print(llstr)


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    ll.print_list()
    ll.remove_index(4)
    ll.print_list()
    ll.insert_at(2, 99)
    ll.print_list()