from typing import List

class TreeNode:
    def __init__(self,val,children=[]) -> None:
        self.val = val
        self.children = children
    
    def __str__(self,depth=0) -> str:
        res = ''
        if self:
            res = ' '*depth + f'{self.val}\n'
            for child in self.children:
                res += child.__str__(depth+1)
        return res

if __name__=='__main__':
    t1 = TreeNode(1, [])
    t2 = TreeNode(2, [])
    t3 = TreeNode(3, [])
    t4 = TreeNode(4, [t1, t2, t3])
    t5 = TreeNode(5, [])
    t6 = TreeNode(6, [t4, t5])
    print(t6)