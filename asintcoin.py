import asyncio
import time
import requests_async as requests
import pprint


out = []
async def one():
    r = await requests.get("https://api.binance.com/api/v3/depth?limit=15&symbol=BTCUSDT")
    # pprint.pprint(r.text)
    out.append(r.text)
    return r

async def main():
    background_tasks = set()
   
    for el in range(1000): 
        task = asyncio.create_task(one())
        background_tasks.add(task)
        task.add_done_callback(background_tasks.discard)
        # await task1
    await task

t = time.time()
asyncio.run(main())
print(time.time()-t, 'время выполнение')

print(len(out), 'количество положительный ответов')


