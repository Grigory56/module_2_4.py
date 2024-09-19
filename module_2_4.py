
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_primers = True
for i in range(1,len(numbers)):
    for j in range(1,i):
          if numbers[i] % numbers[j] == 0:
               is_primers = False
               break
    if is_primers:
        primes.append(numbers[i])
    else:
        not_primes.append(numbers[i])
        is_primers=True
print('Primes: ',primes)
print('Not Primes: ',not_primes)
