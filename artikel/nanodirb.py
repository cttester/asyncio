#!/usr/bin/env python3

"""
Copyright (c) 2023 Oliver Lau, Heise Medien GmbH & Co. KG

Deze software is geschreven voor leer- en voorbeelddoeleinden 
en niet voor productief gebruik. F&L Media, Heise Medien en de
auteur zijn niet verantwoordelijk voor schade die ontstaat door
het gebruik van deze software en geven geen garanties voor 
de volledigheid, juiste werking of geschiktheid voor 
gebruik.
"""

import asyncio
from typing import Iterable, Any
from tornado.httpclient import AsyncHTTPClient, HTTPClientError

class NanoDirb:
    def __init__(self, **kwargs) -> None:
        self.queue = asyncio.Queue()
        self.num_workers = kwargs.get('num_workers', 10)
        self.result_callback = kwargs.get('result_callback')

    async def run(self, urls: Iterable[str]) -> None:
        workers = [asyncio.create_task(self.worker()) 
                   for _ in range(self.num_workers)]
        for url in urls:
            await self.queue.put(url)
        await self.queue.join()
        for worker in workers:
            worker.cancel()

    async def worker(self) -> None:
        while True:
            url = await self.queue.get()
            http_client = AsyncHTTPClient()
            try:
                response = await http_client.fetch(url)
                if callable(self.result_callback):
                    self.result_callback({
                        'url': url,
                        'status_code': response.code,
                    })
            except HTTPClientError as e:
                if callable(self.result_callback):
                    self.result_callback({
                        'url': url,
                        'status_code': e.code,
                    })
            except asyncio.CancelledError:
                return
            finally:
                self.queue.task_done()


async def main(**kwargs) -> None:
    def result_hook(result: Any) -> None:
        print(f"{result['status_code']}\t"
              f"{result['url']}")

    kwargs['result_callback'] = result_hook

    dirb = NanoDirb(**kwargs)
    urls = [
        'http://example.com/admin',
        'http://example.com/admin.php',
        'http://example.com/auth',
        'http://example.com/auth.php',
    ]
    await dirb.run(urls)


if __name__ == '__main__':
    asyncio.run(main(num_workers=10))
