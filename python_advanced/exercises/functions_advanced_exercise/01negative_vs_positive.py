numbers = [int(x) for x in input().split()]
negative_sum = 0
positive_sum = 0


for number in numbers:
    if number < 0:
        negative_sum += number
    else:
        positive_sum += number

print(negative_sum, positive_sum, sep='\n')

if abs(negative_sum) > positive_sum:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")
