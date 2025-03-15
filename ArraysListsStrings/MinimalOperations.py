def minimalOperations(words):
    new_array = []
    for word in words:
        same_counter = 0
        i = 0
        for i in range(len(word) - 1):
            if word[i] == word[i+1]:
                same_counter = same_counter + 1
                i = i + 1
        new_array.append(same_counter)
    return new_array
# wrong

def minimalOperations(words):
    result = []
    for word in words:
        same_counter = 0
        i = 0
        while i < len(word) - 1:  # Using a while loop inside for a per-word basis
            if word[i] == word[i + 1]:  # Found adjacent duplicate
                same_counter = same_counter + 1
                i = i + 2
        result.append(same_counter)
    return result
## TLE ^

## Solution
def minimalOperations(words):
    result = []
    for word in words:
        same_counter = 0
        i = 0
        while i < len(word):
            count = 1  # Start counting occurrences of the same letter
            while i + 1 < len(word) and word[i] == word[i + 1]:
                count += 1
                i += 1  # Move forward until the streak breaks
            same_counter += count // 2  # Every two adjacent letters = 1 operation
            i += 1  # Move to the next different character
        result.append(same_counter)
    return result
