from collections import deque
   
          
def is_palindrom(s):
    # make a given string not case-insensitive and remove all non-alphabetical characters.
    s = ''.join(char.lower() for char in s if char.isalpha())
    char_deque = deque(s)

    # check a given string using deque
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False
    return True


# Test case 1: Expected result False
assert is_palindrom('advght') == False, "Test case 1 failed"

# Test case 2: Expected result False
assert is_palindrom('Akttka') == True, "Test case 2 failed"

# Test case 3: Expected result False
assert is_palindrom('domi non &( imOd') == True, "Test case 3 failed"

# Test case 4: Expected result False
assert is_palindrom('loo/++++./ool') == True, "Test case 4 failed"

# Test case 5: Expected result False
assert is_palindrom('akf@#% bjt pwaka') == False, "Test case 5 failed"
  

  
