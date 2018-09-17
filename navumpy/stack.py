# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(S):
    output = -1
    stk = []
    ops = S.split()
    for op in ops:
        if op == 'DUP':
            if len(stk) < 1:
                return -1
            dup = stk[-1]
            stk.append(dup)
        elif op == 'POP':
            if len(stk) < 1:
                return -1
            stk.pop()
        elif op == '+':
            if len(stk) < 2:
                return -1
            add1 = stk[-1]
            add2 = stk[-2]
            stk.pop()
            stk.pop()
            stk.append(add1+add2)
        elif op == '-':
            if len(stk) < 2:
                return -1
            sub1 = stk[-1]
            sub2 = stk[-2]
            stk.pop()
            stk.pop()
            stk.append(sub1-sub2)
        else:
            stk.append(int(op))
            if int(op) < 0:
                return -1
    # print(stk)
    output = stk[-1]
    return output



S = '13 DUP 4 POP 5 DUP + DUP + -'
print(solution(S))
S = '3 DUP 5 - -'
print(solution(S))
S = '5 6 + -'
print(solution(S))
