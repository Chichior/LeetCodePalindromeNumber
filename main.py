def isPalindrome(x):
    x = str(x)
    y = x[::-1]

    if x == y:
        return True
    else:
        return False


print(isPalindrome(121))


