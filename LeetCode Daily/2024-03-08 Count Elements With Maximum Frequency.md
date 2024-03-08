# Count Elements With Maximum Frequency

#easy 

You are given an array `nums` consisting of **positive** integers.

Return _the **total frequencies** of elements in_ `nums` _such that those elements all have the **maximum** frequency_.

The **frequency** of an element is the number of occurrences of that element in the array.

**Example 1:**

**Input:** nums = [1,2,2,3,1,4]
**Output:** 4
**Explanation:** The elements 1 and 2 have a frequency of 2 which is the maximum frequency in the array.
So the number of elements in the array with maximum frequency is 4.

**Example 2:**

**Input:** nums = [1,2,3,4,5]
**Output:** 5
**Explanation:** All elements of the array have a frequency of 1 which is the maximum.
So the number of elements in the array with maximum frequency is 5.

**Constraints:**

- `1 <= nums.length <= 100`
- `1 <= nums[i] <= 100`

# Solution
Pretty straight forward 

Go lang
```go
func maxFrequencyElements(nums []int) int {
    freq := make(map[int]int)
    maxVal := -1 << 31
    result := 0

    for _, num := range nums {
        freq[num] += 1
        val := freq[num]

        if val > maxVal {
            maxVal = val
            result = val

        } else if val == maxVal {
            result += val
        }
    }

    return result
}
```

Java
```java
class Solution {
    public int maxFrequencyElements(int[] nums) {
        HashMap<Integer, Integer> freq = new HashMap<>();
        int maxVal = -1 << 31;
        int result = 0;

        for(int num : nums){
            if(!freq.containsKey(num)) {
                freq.put(num, 0);
            }
            freq.put(num, freq.get(num) + 1);
            int val = freq.get(num);

            if(val > maxVal) {
                maxVal = val;
                result = val;
            
            } else if (val == maxVal) {
                result += val;
            }
        }

        return result;
    }
}
```

Python
```python
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        return sum([v for _, v in Counter(nums).items() if v == max(Counter(nums).values())])
```

JavaScript
```javascript
class Solution {
    maxFrequencyElements(nums) {
        const freq = new Map();
        let maxVal = -(1 << 31);
        let result = 0;

        for (const num of nums) {
            if (!freq.has(num)) {
                freq.set(num, 0);
            }
            freq.set(num, freq.get(num) + 1);
            const val = freq.get(num);

            if (val > maxVal) {
                maxVal = val;
                result = val;
            } else if (val === maxVal) {
                result += val;
            }
        }

        return result;
    }
}
```
