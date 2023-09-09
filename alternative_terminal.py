import time
from blessed import Terminal


# Initialize the terminal
term = Terminal()

def display_status_page():
    with term.fullscreen(), term.cbreak():
        # Sample distances
        forward_distance = 10  # Replace with your actual forward distance
        right_distance = 5     # Replace with your actual right/left distance
        while True:
            forward_distance = (forward_distance - 1)%10
            right_distance = (right_distance - 1)%5
            # Clear the screen
            print(term.clear)

            # Center the status page
            with term.location(0, term.height // 2 - 5):
                # Display right/left distance (90 degrees to forward)
                print(term.center(f"Right/Left Distance: {right_distance} meters"))

                # Create a horizontal line of "-" for the forward distance
                print(term.center(" "*right_distance*4 + "—" * abs(right_distance*4) + " "*-right_distance*4))
                
                # Create vertical lines of "|" for the right/left distance
                for _ in range(forward_distance*2):
                    print(term.center("|"))
                print(term.center(f"Forward Distance: {forward_distance} meters"))

                print()
                print(term.center("Press 'q' to exit."))

            # Check for user input (q to exit)
            key = term.inkey(timeout=1)
            if key.lower() == 'q':
                break

if __name__ == "__main__":
    display_status_page()
