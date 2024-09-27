class Tree:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_children(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + '|--' if self.parent else ''
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()


def build_tree(data):
    tree = Tree(data['name'])
    if 'children' in data:
        for child in data['children']:
            child_node = build_tree(child)
            tree.add_children(child_node)
    return tree


if __name__ == '__main__':
    tree_data = {
        'name': 'Electronics',
        'children': [
            {
                'name': 'Laptop',
                'children': [
                    {'name': 'HP'},
                    {'name': 'Dell'}
                ]
            },
            {
                'name': 'Mobile',
                'children': [
                    {'name': 'Vivo'},
                    {'name': 'Iqoo'},
                    {'name': 'HTC'}
                ]
            }
        ]
    }

    tree = build_tree(tree_data)
    tree.print_tree()
