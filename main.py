import time


def countdown(seconds):
    """Counts down from the given number of seconds."""
    while seconds >= 0:
        mins, secs = divmod(seconds, 60)
        print(f'{mins:02d}:{secs:02d}', end="\r")
        time.sleep(1)
        seconds -= 1
    print('Done!')


def get_user_time():
    """Gets time input from the user in seconds, ensuring it's valid."""
    while True:
        try:
            user_input = int(input('Please enter time in seconds: '))
            if user_input < 0:
                print("Please enter a positive number.")
            else:
                return user_input
        except ValueError:
            print("Invalid input. Please enter a valid number.")


if __name__ == "__main__":
    user_time = get_user_time()
    countdown(user_time)
