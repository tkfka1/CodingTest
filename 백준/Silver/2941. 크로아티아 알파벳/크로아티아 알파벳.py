x = input()

# Croatian special characters
special_chars = ["c=", "c-", "d-", "lj", "nj", "s=", "z="]

answer = 0
i = 0

while i < len(x):
    if x[i:i+3] == "dz=" and i <= len(x) - 3:  # Check for triple character 'dz='
        answer += 1
        i += 3
    elif x[i:i+2] in special_chars and i <= len(x) - 2:  # Check for double characters
        answer += 1
        i += 2
    else:  # All other characters
        answer += 1
        i += 1

print(answer)
