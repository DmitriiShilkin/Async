import asyncio
import time


async def async_func_exception():
    try:
        print(f'Асинхронная задача начата')
        await asyncio.sleep(1)
        raise RuntimeError('Во время выполнения асинхронной задачи произошел сбой')
    except Exception as e:
        print(f'Поймали исключение: {e} в функции async_func_exception')


async def main():
    task1 = asyncio.create_task(async_func_exception())
    task2 = asyncio.create_task(async_func_exception())
    await asyncio.wait([task1, task2])
    print('Завершение выполнения асинхронных задач')


# фиксируем время начала
tm = time.time()
# запускаем основную корутину
asyncio.run(main())
print(f'Общее время работы {time.time()-tm}')
