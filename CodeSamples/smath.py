def num_str_to_digits(num):
    digits = []
    for char in num:
      digits.append( int(char) )
    return digits


def add_num_arrays(n1, n2):

   max_len = 0
   min_len = 0

   if len(n1) < len(n2):
       min_len = len(n1)
       max_len = len(n2)
   else:
       max_len = len(n1)
       min_len = len(n2)

   print("Last digit = ", n1[-2])

num1 = "1234567890123456789012345"
num2 = "10987654321098765432109875"

dig1 = num_str_to_digits(num1)
print("dig1 = ", dig1)
dig2 = num_str_to_digits(num2)
print("dig2 = ", dig2)

add_num_arrays(dig1, num2)