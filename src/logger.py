from datetime import datetime


def print_message(msg: str):
    current_time = datetime.now().strftime("%H:%M:%S")
    print('[{}]: {}'.format(current_time, msg))
