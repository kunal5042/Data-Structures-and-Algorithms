# Question: https://leetcode.com/problems/reverse-words-in-a-string-iii/
# Easy


class Solution:
    def reverseWords(self, string: str) -> str:
        # input 
        # a string of ASCII characters 
        # string doesn't contain leading or trailing spaces
        # at least one word is present in s
        # all words are separated by a single space
        
        # output
        # resultant string --> x
        # where all words in original string are present in x 
        # each word in itself is reversed in x
        # order of words and whitespaces is maintained in x
        
        # apprach - 1
        # we can split the string into array (let's call it arr_words) of words using the delimitter as whitespace 
        # we can then reverse each word 
        # after reversing each word we can join the array back to form a string using whitespaces in between
        # first operation takes O(n) time
        # second operation takes O(w * m) time where w = number of words and m = length of max words
        # third operation O(n) time 
        # total - O(2n + w*m) or O(n + w*m) time
        
        # approach - 2
        # we create an array x
        # we traverse the array forward 
        # as we encounter a whitespace --> we traverse backwards while pushing each char to x
        # as soon as we encounter another whitespace or the end of the string we stop push a whitespace and continue traversing forwards
        # we do this till the end of the array
        # at last we pop one character from x and join it 
        # time - O(2 * n) or O(n)
        
        whitespace = " "        
        result = []
        
        for idx, char in enumerate(string + whitespace):
            if char == whitespace:
                idx -= 1
                while idx > -1 and string[idx] != whitespace:
                    result.append(string[idx])
                    idx -= 1
                result.append(whitespace)
        
        result.pop()
        return "".join(result)
                


# October 01, 2023

'''

# Kunal Wadhwa

'''