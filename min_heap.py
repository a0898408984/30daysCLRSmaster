class MinHeap:
    def __init__(self):
        self.h = []
        self.key_index = {}
        self.len = 0

    def parent(self, i):
        return int((i-1)/2)

    def insertKey(self, key):
        self.h.append(key)
        self.len += 1
        self.key_index[key] = self.len - 1
        while True:
            i1 = self.key_index[key]
            if i1 == 0:
                break
            i2 = self.parent(i1)
            if self.h[i1] < self.h[i2]:
                tmp = self.h[i1]
                self.h[i1] = self.h[i2]
                self.h[i2] = tmp
                self.key_index[self.h[i1]] = i1
                self.key_index[self.h[i2]] = i2
            else:
                break

    def decreaseKey(self, old_key, new_key):
        i = self.findIndex(old_key)
        if i == None:
            print('(MinHeap)Not found',old_key)
            return
        self.key_index.pop(self.h[i],None)
        self.h[i]  = new_key 
        self.key_index[self.h[i]] = i
        while(i != 0 and self.h[self.parent(i)] > self.h[i]):
            self.key_index[self.h[i]], self.key_index[self.h[self.parent(i)]] = (
            self.parent(i), i)
            self.h[i] , self.h[self.parent(i)] = (
            self.h[self.parent(i)], self.h[i])
            i = self.parent(i)

    def heapify(self, index):
        i1 = (index + 1)* 2 - 1
        i2 = i1 + 1
        minIndex = i1
        minKey = None
        # case 1 no children
        if i1 + 1 > self.len:
            return
        # case 2 no i2 
        elif i2 + 1 > self.len:
            minIndex = i1
            minKey = self.h[i1]
        # case 3
        else:
            minKey = self.h[i1]
            if  minKey > self.h[i2]:
                minKey = self.h[i2]
                minIndex = i2
        if self.h[index] > minKey:
            self.h[index], self.h[minIndex] = (
                self.h[minIndex], self.h[index])
            self.key_index[self.h[minIndex]] , self.key_index[self.h[index]] = (
                minIndex, index)
        self.heapify(minIndex)

    def extractMin(self):
        if self.len == 1:
            ans = self.h[0]
            self.h = []
            self.key_index = {}
            self.len = 0
            return ans
        elif self.len < 1:
            return None
        self.key_index[self.h[-1]]  = 0
        self.key_index.pop(self.h[0],None)
        self.h[0], self.h[-1] = (
        self.h[-1], self.h[0])
        ans = self.h.pop()
        self.len -= 1
        self.heapify(0)
        return ans
  
    def getMin(self):
        return self.h[0]

    def isEmpty(self) -> bool:
        return self.len == 0

    def isExisted(self, key) ->bool:
        return self.findIndex(key) != None

    def findIndex(self, key):
        index_i = self.key_index.get(key) if self.key_index.get(key) != None else None
        return index_i 

def test():
    heap = MinHeap()
    heap.insertKey((3,2))
    heap.insertKey((3,3))
    heap.insertKey((3,4))
    heap.insertKey((4,5))
    heap.extractMin()
    print(heap.h)
    heap.extractMin()
    print(heap.h)
    heap.extractMin()
    print(heap.h)
    heap.extractMin()
    print(heap.h)
    heap.extractMin()
    print(heap.h)


if __name__ == '__main__':
    test()