import math

# Function to add Hamming Code to the binary data
def add_hamming_code(data):
    m = len(data)
    r = 0

    # Calculate the number of parity bits required
    while (2**r) < (m + r + 1):
        r += 1

    total_bits = m + r
    hamming_code = ['0'] * total_bits

    # Place data bits in non-parity positions
    j = 0
    for i in range(total_bits):
        if (i + 1) & i == 0:  # Check if position is a power of 2
            continue
        hamming_code[i] = data[j]
        j += 1

    # Calculate parity bits
    for i in range(r):
        parity_pos = (2**i) - 1
        parity = 0
        for k in range(parity_pos, total_bits, 2**(i + 1)):
            for bit in range(k, min(k + 2**i, total_bits)):
                parity ^= int(hamming_code[bit])  # Calculate parity using XOR
        hamming_code[parity_pos] = str(parity)  # Update the parity bit



    return ''.join(hamming_code)

# Main sender program
def sender():
    # Step 1: Input text and convert to binary
    text = input("Enter the text: ")
    binary_data = ''.join(format(ord(char), '08b') for char in text)
    print(f"Binary Data: {binary_data}")

    # Step 2: Add Hamming Code
    encoded_data = add_hamming_code(binary_data)
    print(f"Encoded Data with Hamming Code: {encoded_data}")

    # Step 3: Save encoded data to file
    with open("channel.txt", "w") as file:
        file.write(encoded_data)
    print("Data saved to channel.txt.")

# Run sender program
if __name__ == "__main__":
    sender()
