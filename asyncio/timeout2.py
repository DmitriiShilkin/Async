import time
import asyncio


async def some_async_task(timeout):
    try:
        print('Длительная задача начата')
        await asyncio.sleep(timeout)
        print('Длительная задача завершена')
    except asyncio.exceptions.CancelledError:
        print('Длительная задача прервана')


async def main():
    try:
        task1 = asyncio.create_task(some_async_task(0.5))
        task2 = asyncio.create_task(some_async_task(1.0))
        task3 = asyncio.create_task(some_async_task(5))
        task4 = asyncio.create_task(some_async_task(10))
        # получаем завершенные и незавершенные задачи
        done, undone = await asyncio.wait([task1, task2, task3, task4], timeout=2.0)
        print(f'Задачи готовы {[t.get_name() for t in done ]}')
        print(f'Задачи не готовы {[t.get_name() for t in undone ]}')
    except asyncio.exceptions.TimeoutError:
        print('Таймаут выполнения задачи')
    except Exception as e:
        print(f'Exception: {e}')
    except asyncio.exceptions.CancelledError as e:
        print(f'Задача прервана')
    print('Завершение выполнения асинхронных задач')


# фиксируем время начала
tm = time.time()
# запускаем основную корутину
asyncio.run(main())
print(f'Общее время работы {time.time() - tm}')
