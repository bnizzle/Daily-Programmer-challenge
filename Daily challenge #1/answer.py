#!/usr/bin/python
import sys

def dec_to_bin(x):
  ''' convert decimal to binary, keeping leading 0's
      http://stackoverflow.com/questions/16926130/python-convert-to-binary-and-keep-leading-zeros
  '''
  return str(format(int(x), '#010b'))[2:]

def reverseBinChars(x):
  ''' reverse the binary number
      ex: 1001 => 0110
  ''' 
  reversedBinaryChars = ""
  for i in range(len(x)):
    if x[i] == "0":
      reversedBinaryChars += "1"
    else:
      reversedBinaryChars += "0"

  return reversedBinaryChars

def bin_to_dec(binaryNumber):
  '''adding 0b to get decimal number from binary number'''

  return int(binaryNumber, 2)


# convert to binary
x_bin = dec_to_bin(str(sys.argv[1]))
y_bin = dec_to_bin(str(sys.argv[2]))

matchPoints = 0

# go through each character to compare if characters match
for i in range(len(x_bin)):
  if x_bin[i] == y_bin[i]:
    matchPoints = matchPoints + 1

numOfBits =  len(x_bin)
compatibility = float(matchPoints)/numOfBits

x_avoid_bin = reverseBinChars(x_bin)
y_avoid_bin = reverseBinChars(y_bin)

# display the result
print str(compatibility*100) + "% Compatibility"
print str(sys.argv[1]) + " should avoid " + str(bin_to_dec(x_avoid_bin))
print str(sys.argv[2]) + " should avoid " + str(bin_to_dec(y_avoid_bin))