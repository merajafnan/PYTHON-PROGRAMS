# The application should manage a queue of people.
#     It will prompt the user for a new name by printing :, the user can type in a name and press ENTER. The app will add the name to the queue.
#     If the user types in “n” then the application will remove the first name from the queue and print it.
#     If the user types in “x” then the application will print the list of users who were left in the queue and it will exit.
#     If the user types in “s” then the application will show the current number of elements in the queue.

from collections import deque
from urllib.parse import urldefrag
def main():
    print("Enter the names to be filled in Queue when prompted with ' : ' '")
    queue_ = []
    while True:
        user_inp = input(':')
        if user_inp != 'n' and user_inp != 's' and user_inp != 'x':
            queue_.append(user_inp)
            print(queue_)
            continue
        if user_inp == 'n':
            if len(queue_) > 0:
                queue_.pop(0)
                print(queue_)
                continue
            else:
                print('Queue is empty')
                continue
        if user_inp == 'x':
            print('Item left in Queue')
            print(queue_)
            print('Now Program will Quit')
            break
        if user_inp == 's':
            print('Count of Element left in Queue')
            print(len(queue_))
main()
