def count_primes(num):
   if num < 2:
       return 0
   primes = [2]
   x = 3
   while x <= num:
       for y in range(3,x,2):
           if x % y == 0:
               x += 2
               break
       else:
           primes.append(x)
           x += 2
   return len(primes)

print(count_primes(25))