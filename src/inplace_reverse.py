# how do we implement an array-reverse function in place?
def reverse(arr):
    # this doesn't work - it creates a copy under the hood
    # slicing creates a copy
    # return arr[::-1]

    left = 0
    right = len(arr)-1

    # how do we iterate?
    # if there's an odd number of elements in the input arr
    # we have the case where left & right are both going to land on the middle elem

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return arr


arr = [26, 42, 16, 22, 8, 7, 4, 5]
print(reverse(arr))


def validParenthesesSequence(s):
    left_bracket = s.count('(')
    right_bracket = s.count(')')
    return left_bracket == right_bracket & (left_bracket + right_bracket) % 2 == 0


def buyAndSellStock(prices):
    if len(prices) == 1:
        return 0

    max_at_point = [max(prices[i:]) - prices[i] for i in range(len(prices))]
    return max(max_at_point)


def validParenthesesSequence(s):
    if len(s) <= 1:
        return False
    if s[0] == ')':
        return False
    if s[-1] == '(':
        return False

    paren_dict = {"(": 0, ")": 0}
    for i in range(len(s)):
        paren_dict[s[i]] += 1

    return paren_dict[")"] == paren_dict["("]


print(validParenthesesSequence("()()(())"))
print(validParenthesesSequence("(((((((((("))
