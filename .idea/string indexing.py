# indexing = accessing elements of a sequence using [] (indexing operator)
#          [start : end : step]

credit_number = "1234-5678-9012-3456"

#print(credit_number[8])
#print(credit_number[0:9])
#print(credit_number[:9])
#print(credit_number[9:])
#print(credit_number[-1])
#print(credit_number[::2])
#print(credit_number[::3])

#last_digits = credit_number[-4:]
#print(f"XXXX-XXXX-XXXX-{last_digits}")
 
credit_number = credit_number[::-1]
print(credit_number)


