class MyHashMap:

    class ListNode:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.next = None

    def __init__(self):
        self.bucketSize = 1000
        self.buckets = [None] * self.bucketSize

    def put(self, key: int, value: int) -> None:
        index = key % self.bucketSize
        if not self.buckets[index]:
            self.buckets[index] = self.ListNode(key, value)
        else:
            curr = self.buckets[index]
            while curr:
                if curr.key == key:
                    curr.value = value
                    return
                if not curr.next:
                    break
                curr = curr.next
            curr.next = self.ListNode(key, value)

    def get(self, key: int) -> int:
        index = key % self.bucketSize
        curr = self.buckets[index]
        while curr:
            if curr.key == key:
                return curr.value
            curr = curr.next
        return -1

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
