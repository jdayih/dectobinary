# input an integer greater than zero
def dec_to_binary(x):
  y = []
  
  while x>0:
    if x%2==0:
      y.append(0)
      x = x/2
    else:
      y.append(1)
      x = (x-1)/2
      
  binary = y[::-1]
  
  for number in binary:
    print(str(number), end ="")

