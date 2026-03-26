arr = list(map(int, input().split()))
if all(x == arr[0] for x in arr):
    print("Perfect Array")
else:
    print("Not Perfect")