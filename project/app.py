import account
import queue
import threading

NUMBER_OF_WORKERS = 1

price_chan = queue.Queue()
workers = []


def start():
    login = account.login_user(account.LOCAL_PATH, account.FILE_NAME)
    start_workers(NUMBER_OF_WORKERS)
    price_chan.join()


def start_workers(num_workers: int):
    for _ in range(num_workers):
        t = threading.Thread(target=worker, args=(price_chan,))
        t.start()
        workers.append(t)


def worker(q):
    while True:
        item = q.get()
        # Processing goes here
        if item is None:
            break
        q.task_done()
    return



