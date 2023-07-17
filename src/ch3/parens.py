

def isBalanced(parens: str) -> bool:
    stack = []
    for c in parens:
        if len(stack) == 0 and c == ")":
            return False
        if c == ")" and stack[-1] == "(":
            stack.pop()
        else:
            stack.append(c)
    return len(stack) == 0