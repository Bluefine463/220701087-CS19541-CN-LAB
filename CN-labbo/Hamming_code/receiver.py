import math

# Function to detect and correct errors in Hamming Code
def correct_hamming_code(data):
    r = math.ceil(math.log2(len(data) + 1))
    error_position = 0

    # Check parity bits
    for i in range(r):
        parity_pos = (2**i) - 1
        parity = 0
        for k in range(parity_pos, len(data), 2**(i + 1)):
            for bit in range(k, min(k + 2**i, len(data))):
                parity ^= int(data[bit])
        if parity != 0:
            error_position += (2**i)

    # Correct error if detected
    if error_position > 0:
        print(f"Error detected at position: {error_position}")
        data = list(data)
        if error_position - 1 < len(data):
            data[error_position - 1] = '0' if data[error_position - 1] == '1' else '1'
        else:
            print("Error position out of bounds!")
        data = ''.join(data)
    else:
        print("No errors detected.")

    return data

# Function to remove parity bits
def remove_parity_bits(data):
    original_data = []
    for i in range(len(data)):
        if (i + 1) & i != 0:  # Skip parity bit positions
            original_data.append(data[i])
    return ''.join(original_data)

# Main receiver program
def receiver():
    # Step 1: Read encoded data from file
    with open("channel.txt", "r") as file:
        received_data = file.read().strip()
    print(f"Received Data: {received_data}")

    # Step 2: Correct Hamming Code
    corrected_data = correct_hamming_code(received_data)
    print(f"Corrected Data: {corrected_data}")

    # Step 3: Remove parity bits
    original_binary = remove_parity_bits(corrected_data)
    print(f"Original Binary Data: {original_binary}")

    # Step 4: Convert binary to text
    output_text = ''.join(chr(int(original_binary[i:i + 8], 2)) for i in range(0, len(original_binary), 8))
    print(f"Output Text: {output_text}")

# Run receiver program
if __name__ == "__main__":
    receiver()
