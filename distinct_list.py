s = input("Enter numbers(Separate by space):")
numbers = list(map(int, s.split()))

def distList(l):
    return list(set(l))

print(distList(numbers))