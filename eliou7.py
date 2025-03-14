from collections import deque

class creature_node:
    def __init__(self, name):
        self.name = name 
        self.left = None # left child
        self.right = None #right child
        # will get overridden later

class creature_tree:
    def __init__(self):
        self.root = None #tree root 

    def add_root(self, name):
        if self.root is None: # if no root exists yet...
            self.root = creature_node(name)
            print(f"Root creature '{name}' has been added!")
        else:
            print("Root creature already exists.")

    def add_creature(self, parent_name, side, name):
        parent_node = self.search_node(self.root, parent_name)
        if parent_node:
            if side.lower() == 'l': #left child
                if parent_node.left is None:
                    parent_node.left = creature_node(name)
                    print(f"Left child '{name}' has been added to '{parent_name}'.")
                else:
                    print(f"'{parent_name}' already has a left child!")

            elif side.lower() == 'r': #right child
                if parent_node.right is None:
                    parent_node.right = creature_node(name)
                    print(f"Right child '{name}' has been added to '{parent_name}'.")
                else:
                    print(f"'{parent_name}' already has a right child!")

            else:
                print("Invalid side! Choose 'L' for left or 'R' for right.")

        else:
            print(f"Parent '{parent_name}' not found.")

    def search_node(self, node, name):
        if node is None:
            return None
        if node.name == name:
            return node
        left_search = self.search_node(node.left, name)
        if left_search:
            return left_search 
        return self.search_node(node.right, name)
    
    def find_ancestor(self, name):
        ancestors = []
        if self.help_find_ancestor(self.root, name, ancestors):
            print(f"The {name} descends from {'-->'.join(ancestors[::-1])}.")
        else:
            print(f"'{name}' not found.")

    def help_find_ancestor(self, node, name, ancestors):
        if node is None:
            return False
        if node.name == name:
            return True 
        if (self.help_find_ancestors(node.left, name, ancestors) or self.help_find_ancestors(node.right, name, ancestors)):
            ancestors.append(node.name)
            return True
        return False 
    
    def print_tree(self, node, level=0):
        if node:
            print("    " * level + node.name)
            if node.left or node.right:
                print("    " * (level + 1) + "/ " if node.left else "    " * (level + 1) + "  ")
                self.print_tree(node.left, level + 1)
                print("    " * (level + 1) + "\\ " if node.right else "    " * (level + 1) + "  ")
                self.print_tree(node.right, level + 1)


def menu():
    tree = creature_tree()
    while True:
        print("\n-----------Menu-----------")
        print("1: Add Creature")
        print("2: Print All")
        print("3: Print Specific Ancestors")
        print("4: Exit")
        print("---------------------------")

        choice = input("Please enter menu option: ")

        if choice == "1":
            if not tree.root:
                name = input("Please input creature name: ")
                tree.add_root(name)
            else:
                parent_name = input("Please enter Node name: ")
                side = input("Please enter left or right child (input L or R respectively.): ")
                name = input("Please enter name: ")
                tree.add_creature(parent_name, side, name)

        elif choice == "2":
            if tree.root: 
                print("\n-----Creatures-----")
                tree.print_tree(tree.root)
            else:
                print("The tree is empty!")

        elif choice == "3":
            name = input("Input Node ancestor name: ")
            tree.find_ancestor(name)

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid option! Please enter a choice from the menu above.")

if __name__ == '__main__':
    menu()