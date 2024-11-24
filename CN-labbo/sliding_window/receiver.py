import random
import time

# Function to simulate the receiver process
def receiver():
    expected_frame = 0  # Start with the first frame
    count=0
    while True:
        try:
            # Step 1: Read the sender buffer
            with open("Sender_Buffer.txt", "r") as file:
                frame = eval(file.read().strip())  # Convert string back to list
            print(f"\nReceived Frame: {frame}")

            # Step 2: Check the frame number
            if frame[0] == expected_frame:
                print(f"Frame {frame[0]} received correctly!")
                
                # Simulate random error
                if random.random() < 0.2:  # 20% chance of NACK
                    with open("Receiver_Buffer.txt", "w") as ack_file:
                        ack_file.write(f"NACK {frame[0]}")
                    print(f"NACK {frame[0]} sent due to simulated error.")
                else:
                    with open("Receiver_Buffer.txt", "w") as ack_file:
                        ack_file.write(f"ACK {frame[0]}")
                    print(f"ACK {frame[0]} sent.")
                    expected_frame += 1  # Move to the next frame

            else:
                print(f"Unexpected Frame {frame[0]} received! Expected {expected_frame}.")
                with open("Receiver_Buffer.txt", "w") as ack_file:
                    ack_file.write(f"NACK {frame[0]}")
                count+=1
                if count>5:
                    print("All Frames Received! Terminates....")
                    break

        except FileNotFoundError:
            pass  # Wait until Sender_Buffer is written
        except Exception as e:
            print(f"Error: {e}")
        time.sleep(1)

if __name__ == "__main__":
    receiver()
