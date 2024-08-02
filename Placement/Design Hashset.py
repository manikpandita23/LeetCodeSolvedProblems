class MyHashSet:

    class ListNode:
        def __init__(self, key):
            self.key = key
            self.next = None

    def __init__(self):
        self.bucketSize = 1000
        self.buckets = [None] * self.bucketSize

    def add(self, key: int) -> None:
        index = key % self.bucketSize
        if not self.buckets[index]:
            self.buckets[index] = self.ListNode(key)
        else:
            curr = self.buckets[index]
            while curr:
                if curr.key == key:
                    return
                if not curr.next:
                    break
                curr = curr.next
            curr.next = self.ListNode(key)

    def remove(self, key: int) -> None:
        index = key % self.bucketSize
        curr = self.buckets[index]
        if not curr:
            return
        if curr.key == key:
            self.buckets[index] = curr.next
        else:
            prev = curr
            curr = curr.next
            while curr:
                if curr.key == key:
                    prev.next = curr.next
                    return
                prev = curr
                curr = curr.next

    def contains(self, key: int) -> bool:
        index = key % self.bucketSize
        curr = self.buckets[index]
        while curr:
            if curr.key == key:
                return True
            curr = curr.next
        return False
