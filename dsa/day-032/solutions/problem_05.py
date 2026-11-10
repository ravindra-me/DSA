class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode | None' = None, right: 'TreeNode | None' = None):
        self.val = val
        self.left = left
        self.right = right

def deserialize_preorder(preorder: str) -> TreeNode | None:
    """Reconstructs a binary tree from a comma-separated preorder string iteratively using a stack."""
    if not preorder or preorder == "#":
        return None
    
    tokens = preorder.split(",")
    root: TreeNode | None = None
    # Stack holds mutable lists: [node, count_of_children_filled]
    stack: list[list] = []
    
    for token in tokens:
        curr = None if token == "#" else TreeNode(int(token))
        
        if not stack:
            root = curr
        else:
            parent_frame = stack[-1]
            parent = parent_frame[0]
            if parent_frame[1] == 0:
                parent.left = curr
            else:
                parent.right = curr
            parent_frame[1] += 1
            
            if parent_frame[1] == 2:
                stack.pop()
        
        if curr is not None:
            stack.append([curr, 0])
            
    return root
