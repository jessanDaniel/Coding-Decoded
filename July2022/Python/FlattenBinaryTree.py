class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        
        
        def dfs(root):
            if not root:
                return None 
            
            root_leftTail=dfs(root.left)
            root_rightTail=dfs(root.right)
            
            if root_leftTail:
                root_leftTail.right=root.right
                root.right=root.left #to connect the flattened and connected version
                root.left=None #now that the right is contains the chain, disconnet the left hand from the world
                
            last=root_rightTail or root_leftTail or root
            return last
        #to check what is returned at the end of the program
        check=dfs(root)
        print(check)
        
        
        #credits: NEETCODE 
