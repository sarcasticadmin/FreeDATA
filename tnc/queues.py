"""
Hold queues used by more than one module to eliminate cyclic imports.
"""
import queue

DATA_QUEUE_TRANSMIT = queue.Queue()
DATA_QUEUE_RECEIVED = queue.Queue()

# Initialize FIFO queue to store received frames
MODEM_RECEIVED_QUEUE = queue.Queue()
MODEM_TRANSMIT_QUEUE = queue.Queue()
