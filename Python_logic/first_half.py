'''
Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".


first_half('WooHoo') → 'Woo'
first_half('HelloThere') → 'Hello'
first_half('abcdef') → 'abc'
'''

def first_half (even_string):
  print_string = ''
  half = len(even_string) // 2
  for index in range(0,half):
    print_string += even_string[index]
  return print_string
    
even_string = 'abcdef'
print(first_half(even_string))