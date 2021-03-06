import sys
import ctypes

sys.path.append('../')
# from pyrtma.client import rtmaClient
# from pyrtma.message import AddMessage, Message
import pyrtma

# Create a user defined message from a ctypes.Structure or basic ctypes
class USER_MESSAGE(ctypes.Structure):
    _fields_ = [
            ('str', ctypes.c_byte * 16),
            ('val', ctypes.c_double),
            ('arr', ctypes.c_int * 8)
            ]

# Choose a unique message type id number
MT_USER_MESSAGE = 1234

# Add the message definition to pyrtma.core module internal dictionary
pyrtma.AddMessage(msg_name='USER_MESSAGE', msg_type=MT_USER_MESSAGE, msg_def=USER_MESSAGE)

def publisher(server='127.0.0.1:7111'):
    # Setup Client
    mod = pyrtma.rtmaClient()
    mod.connect(server_name=server)

    # Build a packet to send
    msg = pyrtma.Message('USER_MESSAGE')
    py_string = b'Hello World'
    msg.data.str[:len(py_string)] = py_string
    msg.data.val = 123.456
    msg.data.arr[:] = list(range(8))

    while True:
        c = input('Hit enter to publish a message. (Q)uit.')
        
        if c not in ['Q', 'q']:
            mod.send_message(msg)
            print('Sent a packet')
        else:
            mod.send_signal('EXIT')
            print('Goodbye')
            break


def subscriber(server='127.0.0.1:7111'):
    # Setup Client
    mod = pyrtma.rtmaClient()
    mod.connect(server_name=server)

    # Select the messages to receive
    mod.subscribe(['USER_MESSAGE', 'EXIT'])

    print('Waiting for packets...')
    while True:
        msg = mod.read_message(timeout=-1)        

        if msg is not None:
            if msg.msg_name == 'USER_MESSAGE':
                print(msg)
            elif msg.msg_name == 'EXIT':
                print('Goodbye.')
                break


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--server', default='127.0.0.1:7111', help='RTMA Message Manager ip address.')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--pub', default=False, action='store_true', help='Run as publisher.')
    group.add_argument('--sub', default=False, action='store_true', help='Run as subscriber.')

    args = parser.parse_args()

    if args.pub:
        print('pyrtma Publisher')
        publisher(args.server)
    elif args.sub:
        print('pyrtma Subscriber')
        subscriber(args.server)
    else:
        print('Unknown input')
