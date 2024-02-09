from oracle import *
from helper import *

def get_signature(m, n):
  result = -1
  mult = pow(Sign(1), -1, n)
  for i in range(2, m):
      sigma = Sign(m // i) * Sign(i) * mult
      sigma %= n
      if not Verify(m, sigma):
          continue 
      result = sigma
      break
  return result


def main():
  with open('project_3_2/input.txt', 'r') as f:
    n = int(f.readline().strip())
    msg = f.readline().strip()

  Oracle_Connect()    

  m = ascii_to_int(msg)
  sigma = get_signature(m, n) 

  print(sigma)

  Oracle_Disconnect()

if __name__ == '__main__':
  main()
