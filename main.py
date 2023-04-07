import time

def countdown(user_time):
    """Function counts down time from user input given in seconds."""
    while user_time >= 0:
        # Calculate minutes and seconds from remaining time
        mins, secs = divmod(user_time, 60)
        # Print formatted time on screen
        print('{:02d}:{:02d}'.format(mins, secs), end="\r")
        # Wait for 1 second
        time.sleep(1)
        # Subtract 1 second from remaining time
        user_time -= 1
    # Display "Done!" message after countdown finishes
    print('Done!')

if __name__ == "__main__":
    # Ask user for time and pass it to the "countdown" function
    user_time = int(input('Please enter time in seconds: '))
    countdown(user_time)
