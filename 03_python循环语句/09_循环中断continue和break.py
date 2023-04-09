"""
continue和break
"""
# continue
for i in range(5):
    if i == 2:
        continue
    print(f"{i}")

# break
for i in range(1, 6):
    print("语句1")
    break
    print("语句2")
print("语句3")
