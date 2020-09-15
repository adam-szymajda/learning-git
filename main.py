min_value = 100
max_value = 999


palindromes = []

for i in range(min_value, max_value):
    for j in range(min_value, max_value):
      if i<j:
          m = i*j
          if str(m) == str(m)[::-1]:
              palindromes.append(m)

print(max(palindromes))
