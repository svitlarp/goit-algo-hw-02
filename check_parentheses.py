
class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, new_el):
        self.stack.append(new_el)

    def pop(self):
        if not self.is_empty():
            self.stack.pop()
        else:
            return "Empty stack"    

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]    
        else:
            return "Empty stack"    

def check_parentheses(input_string):
    # 1. strip all char except paranttheses
    parentheses_list = []
    for i in input_string:
        if i in {'(', ')', '[', ']', '{', '}'}:
            parentheses_list.append(i)
    print(parentheses_list)        
    # 2). 
    if len(parentheses_list) == 0:
        return 'there is no paranthesis in the input_string'
    elif len(parentheses_list) < 2:
        return 'error - there is only one bracket'
    else:
        stack = Stack()
        for i in parentheses_list:
            if stack.is_empty():
                stack.push(i)
            elif i not in {')', ']', '}'}:   
                stack.push(i)
            else:
                if stack.peek() == '(' and i == ')' or stack.peek() == '[' and i == ']' or stack.peek() == '{' and i == '}':
                    stack.pop()    
    # 3). check if stack is empty
    if stack.is_empty():
        return 'ok'
    else:
        return 'Error – an open parenthesis is present.'    


# Test case 1: All parentheses are present in order. Expected result 'ok'
assert check_parentheses('( ) { [() 1 ] ( 1-3 ) ( ) { } } ') == 'ok', "Test case 1 failed"

# Test case 2: The closing bracket is missing. Expected result: Error – an open parenthesis is present.'
assert check_parentheses('( 23 ( 2 - 3)') == 'Error – an open parenthesis is present.', "Test case 2 failed"

# Test case 3:  The opening brackets are missing. Expected result: 'Error – an open parenthesis is present.'
assert check_parentheses('[ 3 ]]]]') == 'Error – an open parenthesis is present.', "Test case 3 failed"

# Test case 4: All parentheses are present in order. Expected result 'ok'
assert check_parentheses("{'key': (func, [4, (2+3) ] ) }") == 'ok', "Test case 4 failed"


# str1 = '( ) { [() 1 ] ( 1-3 ) ( ) { } } '
# str2 = '( 23 ( 2 - 3)'
# str3 = '[ 3 ]]]]'
# str4 = "{'key': (func, [4, (2+3) ] ) }"

# print(check_parentheses(str1))    
# print(check_parentheses(str2))   
# print(check_parentheses(str3))   
# print(check_parentheses(str4))   