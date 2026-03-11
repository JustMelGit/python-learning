##import logging
##import threading
##import time
##
##def thread_function(name):
##    logging.info("Thread %s: starting", name)
##    time.sleep(2)
##    logging.info("Thread %s: finishing", name)
##
##if __name__ == "__main__":
##    format = "%(asctime)s: %(message)s"
##    logging.basicConfig(format=format, level=logging.INFO,
##                        datefmt="%H:%M:%S")
##
##    logging.info("Main    : before creating thread")
##    x = threading.Thread(target=thread_function, args=(1,), daemon = False)
##    logging.info("Main    : before running thread")
##    x.start()
##    logging.info("Main    : wait for the thread to finish")
##    x.join()
##    logging.info("Main    : all done")


##
##import logging
##import threading
##import time
##import concurrent.futures
##
##def thread_function(name):
##    logging.info("Thread %s: starting", name)
##    time.sleep(2)
##    logging.info("Thread %s: finishing", name)
##
##if __name__ == "__main__":
##    format = "%(asctime)s: %(message)s"
##    logging.basicConfig(format=format, level=logging.INFO,
##                        datefmt="%H:%M:%S")
##    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
##        executor.map(thread_function, range(3))
        
##    threads = list()
##    for index in range(3):
##        logging.info("Main    : create and start thread %d.", index)
##        x = threading.Thread(target=thread_function, args=(index,))
##        threads.append(x)
##        x.start()
##
##    for index, thread in enumerate(threads):
##        logging.info("Main    : before joining thread %d.", index)
##        thread.join()
##        logging.info("Main    : thread %d done", index)

##class FakeDatabase:
##    def __init__(self):
##        self.value = 0
##        self._lock = threading.Lock()
##
##    def locked_update(self, name):
##        logging.info("Thread %s: starting update", name)
##        logging.debug("Thread %s about to lock", name)
##        with self._lock:
##            logging.debug("Thread %s has lock", name)
##            local_copy = self.value
##            local_copy += 1
##            time.sleep(0.1)
##            self.value = local_copy
##            logging.debug("Thread %s about to release lock", name)
##        logging.debug("Thread %s after release", name)
##        logging.info("Thread %s: finishing update", name)
##
##if __name__ == "__main__":
##    format = "%(asctime)s: %(message)s"
##    logging.basicConfig(format=format, level=logging.INFO,
##                        datefmt="%H:%M:%S")
##    logging.getLogger().setLevel(logging.DEBUG)
##
##    database = FakeDatabase()
##    logging.info("Testing update. Starting value is %d.", database.value)
##    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
##        for index in range(2):
##            executor.submit(database.locked_update, index)
##    logging.info("Testing update. Ending value is %d.", database.value)


##import threading
##
##l = threading.Lock()
##print("before first acquire")
##l.acquire()
##print("before second acquire")
##l.acquire()
##print("acquired lock twice")


##import concurrent.futures
##import logging
##import queue
##import random
##import threading
##import time
##
##def producer(queue, event):
##    """Pretend we're getting a number from the network."""
##    while not event.is_set():
##        message = random.randint(1, 101)
##        logging.info("Producer got message: %s", message)
##        queue.put(message)
##
##    logging.info("Producer received event. Exiting")
##
##def consumer(queue, event):
##    """Pretend we're saving a number in the database."""
##    while not event.is_set() or not queue.empty():
##        message = queue.get()
##        logging.info(
##            "Consumer storing message: %s (size=%d)", message, queue.qsize()
##        )
##
##    logging.info("Consumer received event. Exiting")
##
##if __name__ == "__main__":
##    format = "%(asctime)s: %(message)s"
##    logging.basicConfig(format=format, level=logging.INFO,
##                        datefmt="%H:%M:%S")
##
##    pipeline = queue.Queue(maxsize=10)
##    event = threading.Event()
##    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
##        executor.submit(producer, pipeline, event)
##        executor.submit(consumer, pipeline, event)
##
##        time.sleep(0.1)
##        logging.info("Main: about to set event")
##        event.set()


##import requests
##import time
##
##
##def download_site(url, session):
##    with session.get(url) as response:
##        print(f"Read {len(response.content)} from {url}")
##
##
##def download_all_sites(sites):
##    with requests.Session() as session:
##        for url in sites:
##            download_site(url, session)
##
##
##if __name__ == "__main__":
##    sites = [
##        "https://www.jython.org",
##        "http://olympus.realpython.org/dice",
##    ] * 80
##    start_time = time.time()
##    download_all_sites(sites)
##    duration = time.time() - start_time
##    print(f"Downloaded {len(sites)} in {duration} seconds")



##import threading
##import time
####from random import randint
##                    
##class SharedCounter(object):
##  
##    def __init__(self, val = 0):
##        self.lock = threading.Lock()
##        self.counter = val
##        
##    def increment(self):
##        print("Waiting for a lock")
##        self.lock.acquire()
##        try:
##            print('Acquired a lock, counter value: ', self.counter)
##            self.counter = self.counter + 1
##        finally:
##            print('Released a lock, counter value: ', self.counter)
##            self.lock.release()

##def task(c):
##    # picking up a random number
####    r = randint(1,5)
##    # running increment for a random number of times
##    for i in range(5):
##      c.increment()
##    print('Done')

##if __name__ == '__main__':
##    sCounter = SharedCounter()
##
##    t1 = threading.Thread(target=task, args=(sCounter,))
##    t1.start()
##    
##    t2 = threading.Thread(target=task, args=(sCounter,))
##    t2.start()
##
##    print('Waiting for worker threads')
##    t1.join()
##    t2.join()
##    
##    print('Counter:', sCounter.counter)
##

##import asyncio
##
##async def fetch_data():
##    print('start fetching')
##    await asyncio.sleep(2)
##    print('done fetching')
##    return {'data':1}
##
##
##async def print_numbers():
##    for i in range(10):
##        print(i)
##        await asyncio.sleep(0.25)
##
##async def main():
##    task1 = asyncio.create_task(fetch_data())
##    task2 = asyncio.create_task(print_numbers())
##    value = await task1
##    print(value)
##    await task2
##
##
##asyncio.run(main())



##import asyncio
##import random
##
### ANSI colors
##c = (
##    "\033[0m",   # End of color
##    "\033[36m",  # Cyan
##    "\033[91m",  # Red
##    "\033[35m",  # Magenta
##)
##
##async def makerandom(idx: int, threshold: int = 6) -> int:
##    print(c[idx + 1] + f"Initiated makerandom({idx}).")
##    i = random.randint(0, 10)
##    while i <= threshold:
##        print(c[idx + 1] + f"makerandom({idx}) == {i} too low; retrying.")
##        await asyncio.sleep(idx + 1)
##        i = random.randint(0, 10)
##    print(c[idx + 1] + f"---> Finished: makerandom({idx}) == {i}" + c[0])
##    return i
##
##async def main():
##    res = await asyncio.gather(*(makerandom(i, 10 - i - 1) for i in range(3)))
##    return res
##
##if __name__ == "__main__":
##    random.seed(444)
##    r1, r2, r3 = asyncio.run(main())
##    print()
##    print(f"r1: {r1}, r2: {r2}, r3: {r3}")
##




##import asyncio
##import random
##import time
##
##async def part1(n: int) -> str:
##    i = random.randint(0, 10)
##    print(f"part1({n}) sleeping for {i} seconds.")
##    await asyncio.sleep(i)
##    result = f"result{n}-1"
##    print(f"Returning part1({n}) == {result}.")
##    return result
##
##async def part2(n: int, arg: str) -> str:
##    i = random.randint(0, 10)
##    print(f"part2{n, arg} sleeping for {i} seconds.")
##    await asyncio.sleep(i)
##    result = f"result{n}-2 derived from {arg}"
##    print(f"Returning part2{n, arg} == {result}.")
##    return result
##
##async def chain(n: int) -> None:
##    start = time.perf_counter()
##    p1 = await part1(n)
##    p2 = await part2(n, p1)
##    end = time.perf_counter() - start
##    print(f"-->Chained result{n} => {p2} (took {end:0.2f} seconds).")
##
##async def main(*args):
##    await asyncio.gather(*(chain(n) for n in args))
##
##if __name__ == "__main__":
##    import sys
##    random.seed(444)
##    args = [1, 2, 3] if len(sys.argv) == 1 else map(int, sys.argv[1:])
##    start = time.perf_counter()
##    asyncio.run(main(*args))
##    end = time.perf_counter() - start
##    print(f"Program finished in {end:0.2f} seconds.")


##import asyncio
##import itertools as it
##import os
##import random
##import time
##
##async def makeitem(size: int = 5) -> str:
##    return os.urandom(size).hex()
##
##async def randsleep(caller=None) -> None:
##    i = random.randint(0, 10)
##    if caller:
##        print(f"{caller} sleeping for {i} seconds.")
##    await asyncio.sleep(i)
##
##async def produce(name: int, q: asyncio.Queue) -> None:
##    n = random.randint(0, 10)
##    for _ in it.repeat(None, n):  # Synchronous loop for each single producer
##        await randsleep(caller=f"Producer {name}")
##        i = await makeitem()
##        t = time.perf_counter()
##        await q.put((i, t))
##        print(f"Producer {name} added <{i}> to queue.")
##
##async def consume(name: int, q: asyncio.Queue) -> None:
##    while True:
##        await randsleep(caller=f"Consumer {name}")
##        i, t = await q.get()
##        now = time.perf_counter()
##        print(f"Consumer {name} got element <{i}>"
##              f" in {now-t:0.5f} seconds.")
##        q.task_done()
##
##async def main(nprod: int, ncon: int):
##    q = asyncio.Queue()
##    producers = [asyncio.create_task(produce(n, q)) for n in range(nprod)]
##    consumers = [asyncio.create_task(consume(n, q)) for n in range(ncon)]
##    await asyncio.gather(*producers)
##    await q.join()  # Implicitly awaits consumers, too
##    for c in consumers:
##        c.cancel()
##
##if __name__ == "__main__":
##    import argparse
##    random.seed(444)
##    parser = argparse.ArgumentParser()
##    parser.add_argument("-p", "--nprod", type=int, default=5)
##    parser.add_argument("-c", "--ncon", type=int, default=10)
##    ns = parser.parse_args()
##    start = time.perf_counter()
##    asyncio.run(main(**ns.__dict__))
##    elapsed = time.perf_counter() - start
##    print(f"Program completed in {elapsed:0.5f} seconds.")


##import asyncio
##
##async def py35_coro():
##    """Native coroutine, modern syntax"""
##    s = await stuff()
##    return s
##
##async def stuff():
##    return 0x10, 0x20, 0x30
##
##print(py35_coro())


##def gen():
##    yield 0x10,0x20,0x30
##
##g = gen()



##async def mygen(u: int = 10):
##    """Yield powers of 2."""
##    i = 0
##    while i < u:
##        yield 2 ** i
##        i += 1
##        await asyncio.sleep(0.1)
##
##
##async def main():
##    g = [i async for i in mygen()]
##    f = [j async for j in mygen() if not (j//3%5)]
##    return g,f
##
##g,f = asyncio.run(main())




# import asyncio

# async def coro(seq) -> list:
#     """'IO' wait time is proportional to the max element."""
# ##    print(f'am sleeping for {max(seq)} sec')
#     await asyncio.sleep(max(seq))
#     return list(reversed(seq))
##


##async def main():
##    # This is a bit redundant in the case of one task
##    # We could use `await coro([3, 2, 1])` on its own
##    t = asyncio.create_task(coro([3, 2, 1]))  # Python 3.7+
##    await t
##    print(f't: type {type(t)}')
##    print(f't done: {t.done()}')
##t = asyncio.run(main())


# import time
##async def main():
##    t = asyncio.create_task(coro([3, 2, 1]))
##    t2 = asyncio.create_task(coro([10, 5, 0]))  # Python 3.7+
##    print('Start:', time.strftime('%X'))
##    a = await asyncio.gather(t, t2)
##    print('End:', time.strftime('%X'))  # Should be 10 seconds
##    print(f'Both tasks done: {all((t.done(), t2.done()))}')
##    return a
##
##a = asyncio.run(main())


##async def main():
##    t = asyncio.create_task(coro([3, 2, 1]))
##    t2 = asyncio.create_task(coro([10, 5, 0]))
##    print('Start:', time.strftime('%X'))
##    for res in asyncio.as_completed((t, t2)):
##        compl = await res
##        print(f'res: {compl} completed at {time.strftime("%X")}')
##    print('End:', time.strftime('%X'))
##    print(f'Both tasks done: {all((t.done(), t2.done()))}')
##
##a = asyncio.run(main())


# import asyncio
# import random

# # ANSI colors
# c = (
#     "\033[0m",   # End of color
#     "\033[36m",  # Cyan
#     "\033[91m",  # Red
#     "\033[35m",  # Magenta
# )

# async def makerandom(idx: int, threshold: int = 6) -> int:
#     print(c[idx + 1] + f"Initiated makerandom({idx}).")
#     i = random.randint(0, 10)
#     print(i)
#     while i <= threshold:
#         print(c[idx + 1] + f"makerandom({idx}) == {i} too low; retrying.")
#         await asyncio.sleep(idx + 1)
#         i = random.randint(0, 10)
#     print(c[idx + 1] + f"---> Finished: makerandom({idx}) == {i}" + c[0])
#     return i

# async def main():
#     res = await asyncio.gather(*(makerandom(i, 10 - i - 1) for i in range(3)))
#     return res

# if __name__ == "__main__":
#     random.seed(444)
#     r1, r2, r3 = asyncio.run(main())
#     print()
#     print(f"r1: {r1}, r2: {r2}, r3: {r3}")


#REVIEW
# import logging
# import threading
# import time

# def thread_function(name):
#     logging.info("Thread %s: starting", name)
#     time.sleep(2)
#     logging.info("Thread %s: finishing", name)

# if __name__ == "__main__":
#     format = "%(asctime)s: %(message)s"
#     logging.basicConfig(format=format, level=logging.INFO,
#                         datefmt="%H:%M:%S")

#     logging.info("Main    : before creating thread")
#     x = threading.Thread(target=thread_function, args=(1,))
#     logging.info("Main    : before running thread")
#     x.start()
#     logging.info("Main    : wait for the thread to finish")
#     x.join()
#     logging.info("Main    : all done")


# import logging
# import threading
# import time

# def thread_function(name):
#     logging.info("Thread %s: starting", name)
#     time.sleep(2)
#     logging.info("Thread %s: finishing", name)

# if __name__ == "__main__":
#     format = "%(asctime)s: %(message)s"
#     logging.basicConfig(format=format, level=logging.INFO,
#                         datefmt="%H:%M:%S")

#     threads = list()
#     for index in range(3):
#         logging.info("Main    : create and start thread %d.", index)
#         x = threading.Thread(target=thread_function, args=(index,))
#         threads.append(x)
#         x.start()

#     for index, thread in enumerate(threads):
#         logging.info("Main    : before joining thread %d.", index)
#         thread.join()
#         logging.info("Main    : thread %d done", index)


import logging
import threading
import time

import concurrent.futures

# def thread_function(name):
#     logging.info("Thread %s: starting", name)
#     time.sleep(2)
#     logging.info("Thread %s: finishing", name)


# if __name__ == "__main__":
#     format = "%(asctime)s: %(message)s"
#     logging.basicConfig(format=format, level=logging.INFO,
#                         datefmt="%H:%M:%S")

#     with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
#         executor.map(thread_function, range(3))


# class FakeDatabase:
#     def __init__(self):
#         self.value = 0

#     def update(self, name):
#         logging.info("Thread %s: starting update", name)
#         local_copy = self.value
#         local_copy += 1
#         time.sleep(0.1)
#         self.value = local_copy
#         logging.info("Thread %s: finishing update", name)


# if __name__ == "__main__":
#     format = "%(asctime)s: %(message)s"
#     logging.basicConfig(format=format, level=logging.INFO,
#                         datefmt="%H:%M:%S")

#     database = FakeDatabase()
#     logging.info("Testing update. Starting value is %d.", database.value)
#     with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
#         for index in range(2):
#             executor.submit(database.update, index)
#     logging.info("Testing update. Ending value is %d.", database.value)




# class FakeDatabase:
#     def __init__(self):
#         self.value = 0
#         self._lock = threading.Lock()

#     def locked_update(self, name):
#         logging.info("Thread %s: starting update", name)
#         logging.debug("Thread %s about to lock", name)
#         with self._lock:
#             logging.debug("Thread %s has lock", name)
#             local_copy = self.value
#             local_copy += 1
#             time.sleep(0.1)
#             self.value = local_copy
#             logging.debug("Thread %s about to release lock", name)
#         logging.debug("Thread %s after release", name)
#         logging.info("Thread %s: finishing update", name)


# if __name__ == "__main__":
#     format = "%(asctime)s: %(message)s"
#     logging.basicConfig(format=format, level=logging.INFO,
#                         datefmt="%H:%M:%S")
#     # logging.getLogger().setLevel(logging.DEBUG)

#     database = FakeDatabase()
#     logging.info("Testing update. Starting value is %d.", database.value)
#     with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
#         for index in range(2):
#             executor.submit(database.locked_update, index)
#     logging.info("Testing update. Ending value is %d.", database.value)
#     # logging.getLogger().setLevel(logging.DEBUG)

# import random 

# SENTINEL = object()

# def producer(pipeline):
#     """Pretend we're getting a message from the network."""
#     for index in range(2):
#         message = random.randint(1, 101)
#         logging.info("Producer got message: %s", message)
#         pipeline.set_message(message, "Producer")

#     # Send a sentinel message to tell consumer we're done
#     pipeline.set_message(SENTINEL, "Producer")


# def consumer(pipeline):
#     """Pretend we're saving a number in the database."""
#     message = 0
#     while message is not SENTINEL:
#         message = pipeline.get_message("Consumer")
#         if message is not SENTINEL:
#             logging.info("Consumer storing message: %s", message)


# class Pipeline:
#     """
#     Class to allow a single element pipeline between producer and consumer.
#     """
#     def __init__(self):
#         self.message = 0
#         self.producer_lock = threading.Lock()
#         self.consumer_lock = threading.Lock()
#         self.consumer_lock.acquire()

#     def get_message(self, name):
#         logging.debug("%s:about to acquire getlock", name)
#         self.consumer_lock.acquire()
#         logging.debug("%s:have getlock", name)
#         message = self.message
#         logging.debug("%s:about to release setlock", name)
#         self.producer_lock.release()
#         logging.debug("%s:setlock released", name)
#         return message

#     def set_message(self, message, name):
#         logging.debug("%s:about to acquire setlock", name)
#         self.producer_lock.acquire()
#         logging.debug("%s:have setlock", name)
#         self.message = message
#         logging.debug("%s:about to release getlock", name)
#         self.consumer_lock.release()
#         logging.debug("%s:getlock released", name)


# if __name__ == "__main__":
#     format = "%(asctime)s: %(message)s"
#     logging.basicConfig(format=format, level=logging.INFO,
#                         datefmt="%H:%M:%S")
#     logging.getLogger().setLevel(logging.DEBUG)

#     pipeline = Pipeline()
#     with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
#         executor.submit(producer, pipeline)
#         executor.submit(consumer, pipeline)

# import queue

# class Pipeline(queue.Queue):
#     def __init__(self):
#         super().__init__(maxsize=10)

#     def get_message(self, name):
#         logging.debug("%s:about to get from queue", name)
#         value = self.get()
#         logging.debug("%s:got %d from queue", name, value)
#         return value

#     def set_message(self, value, name):
#         logging.debug("%s:about to add %d to queue", name, value)
#         self.put(value)
#         logging.debug("%s:added %d to queue", name, value)

# def producer(pipeline, event):
#     """Pretend we're getting a number from the network."""
#     while not event.is_set():
#         message = random.randint(1, 101)
#         logging.info("Producer got message: %s", message)
#         pipeline.set_message(message, "Producer")

#     logging.info("Producer received EXIT event. Exiting")


# def consumer(pipeline, event):
#     """Pretend we're saving a number in the database."""
#     while not event.is_set() or not pipeline.empty():
#         message = pipeline.get_message("Consumer")
#         logging.info(
#             "Consumer storing message: %s  (queue size=%s)",
#             message,
#             pipeline.qsize(),
#         )

#     logging.info("Consumer received EXIT event. Exiting")



# if __name__ == "__main__":
#     format = "%(asctime)s: %(message)s"
#     logging.basicConfig(format=format, level=logging.INFO,
#                         datefmt="%H:%M:%S")
#     # logging.getLogger().setLevel(logging.DEBUG)

#     pipeline = Pipeline()
#     event = threading.Event()
#     with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
#         executor.submit(producer, pipeline, event)
#         executor.submit(consumer, pipeline, event)

#         time.sleep(0.1)
#         logging.info("Main: about to set event")
#         event.set()


import concurrent.futures
import logging
import queue
import random
import threading
import time

def producer(queue, event):
    """Pretend we're getting a number from the network."""
    while not event.is_set():
        message = random.randint(1, 101)
        logging.info("Producer got message: %s", message)
        queue.put(message)

    logging.info("Producer received event. Exiting")

def consumer(queue, event):
    """Pretend we're saving a number in the database."""
    while not event.is_set() or not queue.empty():
        message = queue.get()
        logging.info(
            "Consumer storing message: %s (size=%d)", message, queue.qsize()
        )

    logging.info("Consumer received event. Exiting")

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    pipeline = queue.Queue(maxsize=10)
    event = threading.Event()
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipeline, event)
        executor.submit(consumer, pipeline, event)

        time.sleep(0.1)
        logging.info("Main: about to set event")
        event.set()