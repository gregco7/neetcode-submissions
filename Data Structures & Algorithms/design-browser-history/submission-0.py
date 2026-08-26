#Class implemented to act as a doubly linked list node for this problem
class siteNode:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        homepageNode = siteNode(homepage)

        self.head = homepageNode
        self.tail = homepageNode

        homepageNode.next = homepageNode

    def visit(self, url: str) -> None:
        
        newNode = siteNode(url)
        self.tail.next = newNode
        newNode.prev = self.tail
        self.tail = newNode
        
    def back(self, steps: int) -> str:

        curr = self.tail
        while curr.prev and steps > 0:
            curr = curr.prev
            steps -= 1
        if curr:
            self.tail = curr
            return curr.val
        

    def forward(self, steps: int) -> str:

        curr = self.tail
        while curr.next and steps > 0:
            curr = curr.next
            steps -= 1
        if curr:
            self.tail = curr
            return curr.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)