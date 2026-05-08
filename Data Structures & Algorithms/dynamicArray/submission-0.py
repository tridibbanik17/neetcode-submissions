# ============================================================
# Dynamic Array
# Category : Arrays & Hashing
# Difficulty: Easy
# NeetCode : https://neetcode.io/problems/dynamicArray
# ============================================================
# Runtime : 28 ms   | Beats 82.54%
# Memory  : 7.9 MB  | Beats 98.89%
# Submitted: 2026-05-08
# ============================================================

class DynamicArray:
    
    def __init__(self, capacity: int):
        if (capacity <= 0):
            raise ValueError("Capacity must be > 0.")
        self._capacity = capacity
        self._size = 0
        self._data = [None]*capacity

    def get(self, i: int) -> int:
        if (i < 0 or i >= self._size):
            raise IndexError("Index out of range.")
        return self._data[i]

    def set(self, i: int, n: int) -> None:
        if (i < 0 or i >= self._size):
            raise IndexError("Index out of range.")
        self._data[i] = n

    def pushback(self, n: int) -> None:
        if (self._size == self._capacity):
            self.resize()
        self._data[self._size] = n
        self._size += 1

    def popback(self) -> int:
        if (self._size == 0):
            raise IndexError("List is empty.")
        val = self._data[self._size - 1]
        self._data[self._size - 1] = None
        self._size -= 1
        return val
 

    def resize(self) -> None:
        new_capacity = self._capacity*2
        new_data = [None]*new_capacity
        for i in range(self._size):
            new_data[i] = self._data[i]
        self._data = new_data
        self._capacity = new_capacity

    def getSize(self) -> int:
        return self._size
    
    def getCapacity(self) -> int:
        return self._capacity
