# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(S):
    # return -2 if no adjacent
    # return -1 if min-distance > 100,000,000
    output = -2 
    minDistArray = []
    # print(max(S))
    for i in range(len(S)):
        print(min(S[i:]), max(S[i:]))

    return output

S = [0,3,3,7,5,3,11,1]
print(solution(S))
