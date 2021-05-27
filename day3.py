#Task Day 3

#Given an integer, , perform the following conditional actions:
#If  is odd, print Weird
# If  is even and in the inclusive range of  to , print Not Weird
# If  is even and in the inclusive range of  to , print Weird
# If  is even and greater than , print Not Weird
# Complete the stub code provided in your editor to print whether or not  is weird.

def function(N):
    print("Weird" if ((N % 2 != 0) or (N % 2 == 0 and N in range(6, 21))) else "Not Weird")

if __name__ == '__main__':
    N = int(input().strip())
    function(N)
