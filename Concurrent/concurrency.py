# import requests
# import time


# def download_site(url, session):
#     with session.get(url) as response:
#         print(f"Read {len(response.content)} from {url}")


# def download_all_sites(sites):
#     with requests.Session() as session:
#         for url in sites:
#             download_site(url, session)


# if __name__ == "__main__":
#     sites = [
#         "https://www.jython.org",
#         "http://olympus.realpython.org/dice",
#     ] * 80
#     start_time = time.time()
#     download_all_sites(sites)
#     duration = time.time() - start_time
#     print(f"Downloaded {len(sites)} in {duration} seconds")


# import concurrent.futures
# import requests
# import threading
# import time


# thread_local = threading.local()


# def get_session():
#     if not hasattr(thread_local, "session"):
#         thread_local.session = requests.Session()
#     return thread_local.session


# def download_site(url):
#     session = get_session()
#     with session.get(url) as response:
#         print(f"Read {len(response.content)} from {url}")


# def download_all_sites(sites):
#     with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
#         executor.map(download_site, sites)


# if __name__ == "__main__":
#     sites = [
#         "https://www.jython.org",
#         "http://olympus.realpython.org/dice",
#     ] * 80
#     start_time = time.time()
#     download_all_sites(sites)
#     duration = time.time() - start_time
#     print(f"Downloaded {len(sites)} in {duration} seconds")



# import asyncio
# import time
# import aiohttp


# async def download_site(session, url):
#     async with session.get(url) as response:
#         print("Read {0} from {1}".format(response.content_length, url))


# async def download_all_sites(sites):
#     async with aiohttp.ClientSession() as session:
#         tasks = []
#         for url in sites:
#             task = asyncio.ensure_future(download_site(session, url))
#             tasks.append(task)
#         await asyncio.gather(*tasks, return_exceptions=True)


# if __name__ == "__main__":
#     sites = [
#         "https://www.jython.org",
#         "http://olympus.realpython.org/dice",
#     ] * 80
#     start_time = time.time()
#     asyncio.get_event_loop().run_until_complete(download_all_sites(sites))
#     duration = time.time() - start_time
#     print(f"Downloaded {len(sites)} sites in {duration} seconds")



# import requests
# import multiprocessing
# import time

# session = None


# def set_global_session():
#     global session
#     if not session:
#         session = requests.Session()


# def download_site(url):
#     with session.get(url) as response:
#         name = multiprocessing.current_process().name
#         print(f"{name}:Read {len(response.content)} from {url}")


# def download_all_sites(sites):
#     with multiprocessing.Pool(initializer=set_global_session) as pool:
#         pool.map(download_site, sites)


# if __name__ == "__main__":
#     sites = [
#         "https://www.jython.org",
#         "http://olympus.realpython.org/dice",
#     ] * 80
#     start_time = time.time()
#     download_all_sites(sites)
#     duration = time.time() - start_time
#     print(f"Downloaded {len(sites)} in {duration} seconds")

# import time


# def cpu_bound(number):
#     return sum(i * i for i in range(number))


# def find_sums(numbers):
#     for number in numbers:
#         cpu_bound(number)


# if __name__ == "__main__":
#     numbers = [5_000_000 + x for x in range(20)]

#     start_time = time.time()
#     find_sums(numbers)
#     duration = time.time() - start_time
#     print(f"Duration {duration} seconds")

# import multiprocessing
# import time


# def cpu_bound(number):
#     return sum(i * i for i in range(number))


# def find_sums(numbers):
#     with multiprocessing.Pool() as pool:
#         pool.map(cpu_bound, numbers)


# if __name__ == "__main__":
#     numbers = [5_000_000 + x for x in range(20)]

#     start_time = time.time()
#     find_sums(numbers)
#     duration = time.time() - start_time
#     print(f"Duration {duration} seconds")


# import logging
# import threading
# import time


# def thread_function(name):
#     logging.info("Thread %s: starting",name)
#     time.sleep(2)
#     logging.info("Thread %s: finishing",name)

# if __name__ == "__main__":
#     format = "%(asctime)s: %(message)s"
#     logging.basicConfig(format=format, level = logging.INFO,
#         datefmt = "%H:%M:%S")

#     logging.info("Main before creating thread")
#     x = threading.Thread(target=thread_function,args=(1,),daemon=True)
#     logging.info("Main : bofore running thread")
#     x.start()
#     logging.info("Main : wait for the thread to finishd")
#     x.join()
#     logging.info("Main all done")

import logging
import threading
import time
import concurrent.futures


def thread_function(name):
    logging.info("Thread %s: starting",name)
    time.sleep(2)
    logging.info("Thread %s: finishing",name)

# if __name__ == "__main__":
#     format = "%(asctime)s: %(message)s"
#     logging.basicConfig(format=format, level = logging.INFO,
#         datefmt = "%H:%M:%S")

#     with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
#         executor.map(thread_function,range(3))

class FakeDatabase:
    def __init__(self,name):
        logging.info("Thread %s: starting update", name)
        local_copy = self.value
        local_copy+=1
        time.sleep(0.1)
        self.value = local_copy
        logging.info("Thread %s: finishing update", name)



if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level = logging.INFO,
        datefmt = "%H:%M:%S")

    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(thread_function,range(3))