import heapq
from typing import List, Union

class ContinuousMedian:
    """
    A class for calculating the continuous median of a stream of numbers.

    Attributes:
    - lower_half: Max heap to store the lower half of the numbers.
    - upper_half: Min heap to store the upper half of the numbers.
    """

    def __init__(self) -> None:
        """
        Initializes the ContinuousMedian object with two empty heaps.
        """
        self.lower_half: List[int] = []  # Max heap
        self.upper_half: List[int] = []  # Min heap

    def add_number(self, num: int) -> None:
        """
        Adds a number to the stream and balances the heaps accordingly.

        Args:
        - num: The number to add to the stream.
        """
        if not self.lower_half or num <= -self.lower_half[0]:
            heapq.heappush(self.lower_half, -num)
        else:
            heapq.heappush(self.upper_half, num)

        # Balance the heaps
        if len(self.lower_half) > len(self.upper_half) + 1:
            heapq.heappush(self.upper_half, -heapq.heappop(self.lower_half))
        elif len(self.upper_half) > len(self.lower_half):
            heapq.heappush(self.lower_half, -heapq.heappop(self.upper_half))

    def find_median(self) -> Union[int, float]:
        """
        Calculates the median of the current stream of numbers.

        Returns:
        - The median value as an integer if the number of elements is odd.
        - The median value as a float if the number of elements is even.
        """
        if len(self.lower_half) == len(self.upper_half):
            return (-self.lower_half[0] + self.upper_half[0]) / 2
        else:
            return -self.lower_half[0]

'''

# Kunal Wadhwa

'''