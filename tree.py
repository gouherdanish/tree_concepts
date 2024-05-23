from typing import List

class TreeNode:

    def __init__(self,val,children=[]) -> None:
        self._val = val
        self._children = children

    def is_empty(self):
        return self._val is None
    
    def __str__(self,depth=0) -> str:
        if self.is_empty():
            return ""
        else:
            str_so_far = ' '*depth + f'{self._val}\n'
            for child in self._children:
                str_so_far += TreeNode.__str__(child,depth+1)
            return str_so_far
    
    def __len__(self):
        if self.is_empty():
            return 0
        elif len(self._children)==0:
            return 1
        else:
            size_so_far = 1
            for child in self._children:
                size_so_far += TreeNode.__len__(child)
            return size_so_far

    @property  
    def length(self):
        return self.__len__()
    
    @property
    def height(self):
        if self.is_empty():
            return 0
        elif len(self._children)==0:
            return 1
        else:
            max_ht_so_far = 0
            for child in self._children:
                max_ht_so_far = max(max_ht_so_far, 1 + child.height)
            return max_ht_so_far
    
    @property
    def diameter(self):
        dia = 0
        def dfs(self):
            if self.is_empty():
                return 0
            else:
                nonlocal dia
                max_ht_now, max_ht_prev = 0, 0
                for child in self._children:
                    max_ht_prev = max_ht_now
                    max_ht_now = 1 + max(max_ht_now, dfs(child))
                    dia = max_ht_prev + max_ht_now
                return max_ht_now
        dfs(self)
        return dia

if __name__=='__main__':
    # t1 = TreeNode(1, [])
    # t2 = TreeNode(2, [])
    # t3 = TreeNode(3, [])
    # t4 = TreeNode(4, [t1, t2, t3])
    # t5 = TreeNode(5, [])
    # t6 = TreeNode(6, [t4, t5])
    t1 = TreeNode(1, [])
    t2 = TreeNode(2, [])
    t3 = TreeNode(3, [t2])
    t4 = TreeNode(4, [t1, t3])
    t5 = TreeNode(5, [])
    t6 = TreeNode(6, [t5])
    t7 = TreeNode(7, [t6,t4])
    print(t7)
    print(len(t7), t7.length)
    print(t7.height)
    print(t7.diameter)