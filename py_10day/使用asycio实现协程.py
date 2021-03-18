import time
import asyncio  # 异步IO库， 单线程实现并发 —— 协程


# async  关键字     await关键字

async def work1():  # aysnc  任务work1是异步的
    for i in range(5):
        print(f'work1:听音乐...')
        await asyncio.sleep(1)


async def work2():
    for i in range(5):
        print(f'work2:打游戏...')
        await asyncio.sleep(1)


async def main():
    task1 = asyncio.create_task(work1())  # 任务一
    task2 = asyncio.create_task(work2())  # 任务二
    await task1
    await task2


if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(f'共花费时间{(end - start):.2f}秒')
