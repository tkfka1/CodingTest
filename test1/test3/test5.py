def find_smallest_constructor(N):
    for i in range(max(1, N - 9 * len(str(N))), N):
        print(i)
        if i + sum(map(int, str(i))) == N:
            
            return i
    return 0

# Test the function with the provided example
print(find_smallest_constructor(216))