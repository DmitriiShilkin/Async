import time
import asyncio


async def async_func(delay, task_name):
    print(f'Запуск {task_name}')
    await asyncio.sleep(delay)
    print(f'{task_name} завершилась за {delay} сек! ')


async def main():
    #ожидаем выполнения нескольких корутин одновременно
    task1 = asyncio.create_task(async_func(1, 'task1'))
    task2 = asyncio.create_task(async_func(3, 'task2'))
    task3 = asyncio.create_task(async_func(0.5, 'task3'))
    await asyncio.wait([task1, task2, task3])


# фиксируем время начала выполнения
tm = time.time()
asyncio.run(main())
print(f'total time elapsed {time.time()-tm}')
print('Теперь асинхронные задачи вызываются конкурентно.')
print('Получаем ~ 3 сек, что соответствует времени выполнения самой длительной задачи')
