from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self._val = val
        self._left = left
        self._right = right
    
    def __str__(self,depth=0) -> str:
        if not self:
            return ""
        else:
            res = " "*depth + f"{self._val}\n"
            res += TreeNode.__str__(self._left,depth+1)
            res += TreeNode.__str__(self._right,depth+1)
            return res
    
    @property
    def height(self):
        def dfs(node):
            if not node: return 0
            left_ht = dfs(node._left)
            right_ht = dfs(node._right)
            return 1 + max(left_ht,right_ht)
        return dfs(self)

    @property
    def diameter(self):
        dia = 0
        def dfs(node):
            nonlocal dia
            if not node: return 0
            left_ht = dfs(node._left)
            right_ht = dfs(node._right)
            dia = max(dia,left_ht + right_ht)
            return 1 + max(left_ht, right_ht)
        dfs(self)
        return dia
    
if __name__=='__main__':
    # t = TreeNode(
    #         1,
    #         TreeNode(2),
    #         TreeNode(3)
    # )
    t = TreeNode(
        1,
        TreeNode(
            2,
            TreeNode(3),
            TreeNode(4)
            ),
        TreeNode(
            5,
            TreeNode(6),
            TreeNode(7)
        )
    )
    print(t)
    print(t.height)
    print(t.diameter)