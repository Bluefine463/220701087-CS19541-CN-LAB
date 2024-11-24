import time

# Function to simulate the sender process
def sender():
    # Step 1: Input the window size and message
    window_size = int(input("Enter the window size: "))
    message = input("Enter the message to send: ")

    # Step 2: Split the message into frames
    frames = [[i, char] for i, char in enumerate(message)]
    print(f"Frames to send: {frames}")

    # Step 3: Initialize sender buffer
    with open("Sender_Buffer.txt", "w") as file:
        file.write(str(frames[:window_size]))
    print(f"Sender Buffer Initialized with: {frames[:window_size]}")

    # Step 4: Send frames one by one and wait for acknowledgment
    for i in range(len(frames)):
        print(f"\nSending Frame: {frames[i]}")
        time.sleep(1)  # Simulate delay
        with open("Sender_Buffer.txt", "w") as file:
            file.write(str(frames[i]))
        
        print("Waiting for acknowledgment...")

        # Step 5: Read acknowledgment from Receiver_Buffer
        while True:
            try:
                with open("Receiver_Buffer.txt", "r") as ack_file:
                    ack = ack_file.read().strip()
                if ack == f"ACK {frames[i][0]}":
                    print(f"Acknowledgment Received: {ack}")
                    break
                elif ack.startswith("NACK"):
                    print(f"NACK Received for Frame {frames[i][0]}, Resending...")
                    continue
            except FileNotFoundError:
                pass  # Wait until Receiver_Buffer is written
            time.sleep(1)


    print("\nAll frames sent and acknowledged!")

if __name__ == "__main__":
    sender()
