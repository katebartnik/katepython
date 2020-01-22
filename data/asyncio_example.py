
import asyncio
import time
import aiohttp


async def download_site(session, url):
    async with session.get(url) as response:
        print("Read {0} from {1}".format(response.content_length, url))


async def download_all_sites(sites):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in sites:
            task = asyncio.ensure_future(download_site(session, url))
            tasks.append(task)
        await asyncio.gather(*tasks, return_exceptions=True)


sites = [
    'https://www.python.org',
    'http://olympus.realpython.org/dice'
] * 80
start_time = time.time()
#await download_all_sites(sites)
asyncio.run(download_all_sites(sites)) # w ten sposób trzeba to zrobić poza Jupyter, ponieważ Jupyter ma swoją
                                       # własną pętlę (event loop)
                                       # w wątku może być tylko jedna pętla
duration = time.time() - start_time
print(f"Downloaded {len(sites)} sites in {duration} seconds")
