# import asyncio
# import itertools as it
# import os
# import random
# import time

# async def makeitem(size: int = 5) -> str:
#     return os.urandom(size).hex()

# async def randsleep(caller=None) -> None:
#     i = random.randint(0, 10)
#     if caller:
#         print(f"{caller} sleeping for {i} seconds.")
#     await asyncio.sleep(i)

# async def produce(name: int, q: asyncio.Queue) -> None:
#     n = random.randint(0, 10)
#     # n = 2
#     for _ in it.repeat(None, n):  # Synchronous loop for each single producer
#         await randsleep(caller=f"Producer {name}")
#         i = await makeitem()
#         t = time.perf_counter()
#         await q.put((i, t))
#         print(f"Producer {name} added <{i}> to queue.")

# async def consume(name: int, q: asyncio.Queue) -> None:
#     while True:
#         await randsleep(caller=f"Consumer {name}")
     
#         i, t = await q.get()
#         now = time.perf_counter()
#         f" in {now-t:0.5f} seconds."
#         q.task_done()

# async def main(nprod: int, ncon: int):
#     q = asyncio.Queue()
#     producers = [asyncio.create_task(produce(n, q)) for n in range(nprod)]
#     consumers = [asyncio.create_task(consume(n, q)) for n in range(ncon)]
#     await asyncio.gather(*producers)
#     await q.join()  # Implicitly awaits consumers, too
#     for c in consumers:
#         c.cancel()

# if __name__ == "__main__":
#     import argparse
#     random.seed(444)
#     parser = argparse.ArgumentParser()
#     parser.add_argument("-p", "--nprod", type=int, default=5)
#     parser.add_argument("-c", "--ncon", type=int, default=5)
#     ns = parser.parse_args()

#     start = time.perf_counter()

#     asyncio.run(main(**ns.__dict__))
#     elapsed = time.perf_counter() - start
#     print(f"Program completed in {elapsed:0.5f} seconds.")

# import asyncio
# import logging
# import re
# import sys
# from typing import IO
# import urllib.error
# import urllib.parse

# import aiofiles
# import aiohttp
# from aiohttp import ClientSession

# logging.basicConfig(
#     format="%(asctime)s %(levelname)s:%(name)s: %(message)s",
#     level=logging.DEBUG,
#     datefmt="%H:%M:%S",
#     stream=sys.stderr,
# )
# logger = logging.getLogger("areq")
# logging.getLogger("chardet.charsetprober").disabled = True

# HREF_RE = re.compile(r'href="(.*?)"')

# async def fetch_html(url: str, session: ClientSession, **kwargs) -> str:
#     """GET request wrapper to fetch page HTML.

#     kwargs are passed to `session.request()`.
#     """

#     resp = await session.request(method="GET", url=url, **kwargs)
#     resp.raise_for_status()
#     logger.info("Got response [%s] for URL: %s", resp.status, url)
#     html = await resp.text()
#     return html

# async def parse(url: str, session: ClientSession, **kwargs) -> set:
#     """Find HREFs in the HTML of `url`."""
#     found = set()
#     try:
#         html = await fetch_html(url=url, session=session, **kwargs)
#     except (
#         aiohttp.ClientError,
#         aiohttp.http_exceptions.HttpProcessingError,
#     ) as e:
#         logger.error(
#             "aiohttp exception for %s [%s]: %s",
#             url,
#             getattr(e, "status", None),
#             getattr(e, "message", None),
#         )
#         return found
#     except Exception as e:
#         logger.exception(
#             "Non-aiohttp exception occured:  %s", getattr(e, "__dict__", {})
#         )
#         return found
#     else:
#         for link in HREF_RE.findall(html):
#             try:
#                 abslink = urllib.parse.urljoin(url, link)
#             except (urllib.error.URLError, ValueError):
#                 logger.exception("Error parsing URL: %s", link)
#                 pass
#             else:
#                 found.add(abslink)
#         logger.info("Found %d links for %s", len(found), url)
#         return found

# async def write_one(file: IO, url: str, **kwargs) -> None:
#     """Write the found HREFs from `url` to `file`."""
#     res = await parse(url=url, **kwargs)
#     if not res:
#         return None
#     async with aiofiles.open(file, "a") as f:
#         for p in res:
#             await f.write(f"{url}\t{p}\n")
#         logger.info("Wrote results for source URL: %s", url)

# async def bulk_crawl_and_write(file: IO, urls: set, **kwargs) -> None:
#     """Crawl & write concurrently to `file` for multiple `urls`."""
#     async with ClientSession() as session:
#         tasks = []
#         for url in urls:
#             tasks.append(
#                 write_one(file=file, url=url, session=session, **kwargs)
#             )
#         await asyncio.gather(*tasks)

# if __name__ == "__main__":
#     import pathlib
#     import sys

#     assert sys.version_info >= (3, 7), "Script requires Python 3.7+."
#     here = pathlib.Path(__file__).parent

#     with open(here.joinpath(r"C:\Users\gnl999935\Documents\cat urls.txt")) as infile:
#         urls = set(map(str.strip, infile))

#     outpath = here.joinpath(r"C:\Users\gnl999935\Documents\foundurls1.txt")
#     with open(outpath, "w") as outfile:
#         outfile.write("source_url\tparsed_url\n")

#     asyncio.get_event_loop().run_until_complete(bulk_crawl_and_write(file=outpath, urls=urls))
#     # asyncio.run(bulk_crawl_and_write(file=outpath, urls=urls))


import asyncio
import logging
import re
import sys
from typing import IO
import urllib.error
import urllib.parse

import aiofiles
import aiohttp
from aiohttp import ClientSession

logging.basicConfig(
    format="%(asctime)s %(levelname)s:%(name)s: %(message)s",
    level=logging.DEBUG,
    datefmt="%H:%M:%S",
    stream=sys.stderr,
)
logger = logging.getLogger("areq")
logging.getLogger("chardet.charsetprober").disabled = True

HREF_RE = re.compile(r'href="(.*?)"')

async def fetch_html(url: str, session: ClientSession, **kwargs) -> str:
    """GET request wrapper to fetch page HTML.

    kwargs are passed to `session.request()`.
    """

    resp = await session.request(method="GET", url=url, **kwargs)
    resp.raise_for_status()
    logger.info("Got response [%s] for URL: %s", resp.status, url)
    html = await resp.text()
    return html

async def parse(url: str, session: ClientSession, **kwargs) -> set:
    """Find HREFs in the HTML of `url`."""
    found = set()
    try:
        html = await fetch_html(url=url, session=session, **kwargs)
    except (
        aiohttp.ClientError,
        aiohttp.http_exceptions.HttpProcessingError,
    ) as e:
        logger.error(
            "aiohttp exception for %s [%s]: %s",
            url,
            getattr(e, "status", None),
            getattr(e, "message", None),
        )
        return found
    except Exception as e:
        logger.exception(
            "Non-aiohttp exception occured:  %s", getattr(e, "__dict__", {})
        )
        return found
    else:
        for link in HREF_RE.findall(html):
            try:
                abslink = urllib.parse.urljoin(url, link)
            except (urllib.error.URLError, ValueError):
                logger.exception("Error parsing URL: %s", link)
                pass
            else:
                found.add(abslink)
        logger.info("Found %d links for %s", len(found), url)
        return found

async def write_one(file: IO, url: str, **kwargs) -> None:
    """Write the found HREFs from `url` to `file`."""
    res = await parse(url=url, **kwargs)
    if not res:
        return None
    async with aiofiles.open(file, "a") as f:
        for p in res:
            await f.write(f"{url}\t{p}\n")
        logger.info("Wrote results for source URL: %s", url)

async def bulk_crawl_and_write(file: IO, urls: set, **kwargs) -> None:
    """Crawl & write concurrently to `file` for multiple `urls`."""
    async with ClientSession() as session:
        tasks = []
        for url in urls:
            tasks.append(
                write_one(file=file, url=url, session=session, **kwargs)
            )
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    import pathlib
    import sys

    assert sys.version_info >= (3, 7), "Script requires Python 3.7+."
    here = pathlib.Path(__file__).parent

    with open(here.joinpath(r"C:\Users\gnl999935\Documents\cat urls.txt")) as infile:
        urls = set(map(str.strip, infile))

    outpath = here.joinpath(r"C:\Users\gnl999935\Documents\foundurls1.txt")
    with open(outpath, "w") as outfile:
        outfile.write("source_url\tparsed_url\n")

    asyncio.get_event_loop().run_until_complete(bulk_crawl_and_write(file=outpath, urls=urls))
    # asyncio.run(bulk_crawl_and_write(file=outpath, urls=urls))