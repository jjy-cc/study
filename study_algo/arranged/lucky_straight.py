n = input()

half = len(n) // 2

left = sum([int(i) for i in n[:half]])
right = sum([int(i) for i in n[half:]])
if left == right:
    print("LUCKY")
else:
    print("READY")