# def check_parentheses(expression: str) -> bool:

#     answer = None

#     for i in range(0, len(expression), 1):
#         if expression[:i] == "()":
#             answer = True
#             break
#         else:
#             answer = False
#     return answer

# def check_parentheses(expression: str) -> bool:

#     for i in range(0, len(expression), 1):
#         if expression[:i] == "()":
#             return True
#     return False


def check_parentheses(expression: str) -> bool:

    #Used to check the parentheses
    check_parentheses = []

    for i in expression:

        if i == "(":
            check_parentheses.append(i) #With this first iteration "(" will be added to the list
        
        elif i == ")": #Then it checks if the next iteration is ")", if not it will return False otherwise it's True
            if not check_parentheses:
                return False
            
            #Then we remove the last element in the list and goes over the next iteration
            check_parentheses.pop()
    
    return True

# check_parentheses("(())")
# check_parentheses("()()")

print(check_parentheses("()()"))

print(check_parentheses("(()))("))

