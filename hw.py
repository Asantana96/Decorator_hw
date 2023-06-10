def convert_to_binary_search_tree(func):
    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None
    
    def build_binary_search_tree(lst):
        if not lst:
            return None
        
        sorted_lst = sorted(lst)
        mid = len(sorted_lst) // 2
        root = Node(sorted_lst[mid])
        
        root.left = build_binary_search_tree(sorted_lst[:mid])
        root.right = build_binary_search_tree(sorted_lst[mid + 1:])
        
        return root
    
    def wrapper(lst):
        binary_search_tree = build_binary_search_tree(lst)
        
        result = func(binary_search_tree)
        
        return result
    
    return wrapper
