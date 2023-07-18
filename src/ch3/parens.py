

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

def nonContigBalanceLength(parens: str) -> int:
    stack = []
    count = 0
    for c in parens:
        if len(stack) == 0 and c == ")":
            continue
        if c == ")" and stack[-1] == "(":
            stack.pop()
            count +=2
        else:
            stack.append(c)
    return count
