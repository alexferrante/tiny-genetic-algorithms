import os
import math

def write_combinations(arr):
    with open(f"{os.getcwd()}/1d-cellular-automata/lattice_combinations.txt", "w") as f:
        for i in range(len(arr)):
            binary_str_i_arr = list(arr[i])
            print(f"np.array([{','.join(binary_str_i_arr)}]).tobytes(): {i},", file=f)
    
def generate_binary(n):
  bin_arr = []
  bin_str = [0] * n
  for i in range(0, int(math.pow(2,n))):
    bin_arr.append("".join(map(str,bin_str))[::-1])
    bin_str[0] += 1
    # Iterate through entire array if there carrying
    for j in range(0, len(bin_str) - 1):

      if bin_str[j] == 2:
        bin_str[j] = 0
        bin_str[j+1] += 1
        continue

      else:
        break

    
  return bin_arr

def main():
    arr = generate_binary(7)
    write_combinations(arr)

if __name__ == "__main__":
    main()
