def sieve_of_eratosthenes(n):
  primes = [True] * (n + 1)
  primes[0], primes[1] = False, False  
  p = 2
  
  while p * p <= n:
    if primes[p]:
      for i in range(p * p, n + 1, p):
        primes[i] = False
    p += 1
    
  answer = []
  for i in range(n + 1):
    if primes[i]:
      answer.append(i)

  return answer

print("Prime numbers up to 1000:", sieve_of_eratosthenes(1000))
