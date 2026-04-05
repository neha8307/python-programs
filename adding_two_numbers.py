l1 = [2,4,3]
l2 = [5,4,4]

result = []
carry = 0

for i in range(len(l1)):
    total = l1[i] + l2[i] + carry
    result.append(total % 10)
    carry = total // 10

if carry:
    result.append(carry)

print(result)