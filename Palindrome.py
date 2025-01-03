def is_palindrome():
    user_input = input("Enter a string: ")
    n = len(user_input)
    for i in range(n // 2): 
        if user_input[i] != user_input[n - i - 1]:
            print("String is not a palindrome")
            return
    print("String is a palindrome")

is_palindrome()



