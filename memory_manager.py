# One of the services provided by an operating system is memory management. The OS typically provides an API for allocating and releasing memory in a process's address space. A process should only read and write memory at addresses which have been allocated by the operating system. In this kata you will implement a simulation of a simple memory manager.

# The language you will be using has no low level memory API, so for our simulation we will simply use an array as the process address space. The memory manager constructor will accept an array (further referred to as memory) where blocks of indices will be allocated later.

# Memory Manager Contract
# allocate(size)
# allocate reserves a sequential block (sub-array) of size received as an argument in memory. It should return the index of the first element in the allocated block, or throw an exception if there is no block big enough to satisfy the requirements.

# release(pointer)
# release accepts an integer representing the start of the block allocated ealier, and frees that block. If the released block is adjacent to a free block, they should be merged into a larger free block. Releasing an unallocated block should cause an exception.

class MemoryManager:
    def __init__(self, memory):
        """
        @constructor Creates a new memory manager for the provided array.
        @param {memory} An array to use as the backing memory.
        """
        self.memory = memory

    def allocate(self, size):
        """
        Allocates a block of memory of requested size.
        @param {number} size - The size of the block to allocate.
        @returns {number} A pointer which is the index of the first location in the allocated block.
        @raises If it is not possible to allocate a block of the requested size.
        """
        
        for i in range(0,len(self.memory)):
            if type(self.memory[i]) != list:
                if len(self.memory) > size:
                    return False
                else:
                    return self.memory[i][0]
            else:
                if len(self.memory[i]) > size:
                    return False


    def release(self, pointer):
        """
        Releases a previously allocated block of memory.
        @param {number} pointer - The pointer to the block to release.
        @raises If the pointer does not point to an allocated block.
        """

    def read(self, pointer):
        """
        Reads the value at the location identified by pointer
        @param {number} pointer - The location to read.
        @returns {number} The value at that location.
        @raises If pointer is in unallocated memory.
        """
        print(self.memory[pointer])

    def write(self, pointer, value):
        """
        Writes a value to the location identified by pointer
        @param {number} pointer - The location to write to.
        @param {number} value - The value to write.
        @raises If pointer is in unallocated memory.
        """