def print_reversed(s):
    reversed = []
    for item in range(len(s)-1,-1,-1):
        reversed.append(s[item])
    return ''.join(reversed)


if __name__ == "__main__":
    s = input()
    print_reversed(s)
    print_twice(s)
