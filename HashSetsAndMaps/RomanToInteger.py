## O(n) time O(1) space

class Solution(object):
    def romanToInt(self, s):
        roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000} ## hashmap for values of roman numerals
        output = 0 ## running sum
        for i in range(len(s)): ## loop through the indexes of s
            if i + 1 < len(s) and roman_dict[s[i]] < roman_dict[s[i + 1]]: # If this numeral is smaller than the next one and if the index of the next one is within bounds (it exists)
                output = output - roman_dict[s[i]] ## subtract
            else:
                output = output + roman_dict[s[i]] ## add
        return output
    
    
## Brute Force

class Solution(object):
    def romanToInt(self, s):
        output = 0
        i = 0  # Manually iterate through the string
        while i < len(s): 
            # Check if we're at a subtractive pair (check next char exists)
            if i < len(s) - 1 and (s[i], s[i+1]) in [("I", "V"), ("I", "X"), ("X", "L"), ("X", "C"), ("C", "D"), ("C", "M")]:
                if (s[i], s[i+1]) == ("I", "V"):
                    output += 4  # IV = 4
                elif (s[i], s[i+1]) == ("I", "X"):
                    output += 9  # IX = 9
                elif (s[i], s[i+1]) == ("X", "L"):
                    output += 40  # XL = 40
                elif (s[i], s[i+1]) == ("X", "C"):
                    output += 90  # XC = 90
                elif (s[i], s[i+1]) == ("C", "D"):
                    output += 400  # CD = 400
                elif (s[i], s[i+1]) == ("C", "M"):
                    output += 900  # CM = 900
                i = i + 2  # Skip the next character since it's already accounted for
            else: # Process single numerals normally
                if s[i] == "I":
                    output += 1
                elif s[i] == "V":
                    output += 5
                elif s[i] == "X":
                    output += 10
                elif s[i] == "L":
                    output += 50
                elif s[i] == "C":
                    output += 100
                elif s[i] == "D":
                    output += 500
                elif s[i] == "M":
                    output += 1000
                i = i + 1  # Move to the next numeral
        return output