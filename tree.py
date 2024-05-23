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
                str_so_far += child.__str__(depth+1)
            return str_so_far
    
    def __len__(self):
        if self.is_empty():
            return 0
        elif len(self._children)==0:
            return 1
        else:
            size_so_far = 1
            for child in self._children:
                size_so_far += child.__len__()
            return size_so_far

    @property  
    def length(self):
        return self.__len__()


if __name__=='__main__':
    t1 = TreeNode(1, [])
    t2 = TreeNode(2, [])
    t3 = TreeNode(3, [])
    t4 = TreeNode(4, [t1, t2, t3])
    t5 = TreeNode(5, [])
    t6 = TreeNode(6, [t4, t5])
    print(t6)
    print(len(t6), t6.length)