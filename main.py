# Search and Sort Algorithms
# Authors: Cian
# Made: 14/5/2024

class Search:
    def __init__(self, array, toFind) -> None:
        self.array = array
        self.toFind = toFind

    def linearSearch(self):
        """Linear search algorithm"""
        # Iterate over each item in the array, return True if found
        return any(item == self.toFind for item in self.array)

    def binarySearch(self):
        """Binary search algorithm"""
        # Initalize variables
        low = 0
        high = len(self.array)-1
    
        while low <= high:
            midpoint = (low + high)//2 # // to floor divide
    
            if self.array[midpoint] == self.toFind: 
                return True # Returns true if found
            elif self.array[midpoint] < self.toFind:
                low = midpoint + 1
            else:
                high = midpoint - 1
        return False # Returns False if not found

class Sort:
    def __init__(self, array) -> None:
        self.array = array

    def bubbleSort(self):
        """Bubble sort algorithm"""
        for item in range(len(self.array)):
            for pos in range(0, len(self.array) - item - 1):
                if self.array[pos] > self.array[pos + 1]:
                    temp = self.array[pos]
                    self.array[pos] = self.array[pos+1]
                    self.array[pos+1] = temp

    def insertionSort(self):
        """Insertion sort algorithm"""
        
        # Iterate over list starting at second item
        for index in range(1, len(self.array)):
            toInsert = self.array[index] 
    
            # Get the current position of the last sorted item
            position = index - 1

            while position >= 0 and self.array[position] > toInsert:
                self.array[position + 1] = self.array[position]
    
                # Get the position of the next sorted item
                position = position - 1

            # Insert the item into the correct position
            self.array[position + 1] = toInsert

    def quickSortPartition(self, array, low, high): # Low & High pointer passed in params
        pivot = array[high] # Get init pivot

        pointerLow = low - 1 

        for item in range(low, high):
            if array[item] <= pivot: # Check to move right/left
                pointerLow += 1 # Incriment
                (array[pointerLow], array[item]) = (array[item], array[pointerLow]) # Swaps items

        (array[pointerLow + 1], array[high]) = (array[high], array[pointerLow + 1])

        return pointerLow + 1

    def quickSort(self, array=None, low=None, high=None): # Main quicksort function

        if low is None or high is None or array is None:
            array = self.array
            low = 0
            high = len(array) - 1

        if low < high:
            part = self.quickSortPartition(array, low, high)
            self.quickSort(array, low, part - 1) # do left of pivot
            self.quickSort(array, part + 1, high) # do right of pivot
 


def main():
    """Sort Then Find an item in the array"""
    
    """
    Search Methods:
        Search().linearSearch
        Search().binarySearch

    Sort Methods:
        Sort().bubbleSort
        Sort().insertionSort
        Sort().quickSort
    """

    # Initialize variables
    array = [3, 53, 9, 38, 2, 58]
    toFind = 9

    Sort(array).quickSort() # Sort Array
    #print(array) # Testing

    print(Search(array, toFind).binarySearch()) # Search for element, returns True if found


# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == '__main__':
    main()
