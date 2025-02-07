
    ## left pointer will be left =0, right pointer will be length(str) - 1
    ## skip nonalphanumeric characters
    ## check if first character is the same as the last,
    ## if not return False
    ## if it is the same move left pointer to the right, and right pointer to the left
    ## iterate left and right
    ## do the same (check if the characters are the same)

def is_palindrome(s):
   left = 0
   right = len(s) - 1
   while right > left: 
        if not s[left].isalnum():
            left +=1
            continue
        if not s[right].isalnum():
            right -=1
            continue
        if s[left].lower() != s[right].lower():
            return False
        left +=1
        right -=1
   return True

is_palindrome()

