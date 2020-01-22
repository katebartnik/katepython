import asyncio

# taka funkcja nazywana jest korutyną
async def say(what, when):
    await asyncio.sleep(when)
    print(what)

await say('hello', 1)
# #loop = asyncio.get_event_loop()
#loop = asyncio.get_running_loop()
#loop.run_until_complete(say('hello world', 1))
#loop.close()

