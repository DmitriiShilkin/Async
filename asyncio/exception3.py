import time
import asyncio


async def async_func_exception():
    try:
        print(f'Асинхронная задача начата')
        await asyncio.shield(asyncio.sleep(5))
        raise RuntimeError('Во время выполнения асинхронной задачи произошел сбой')
    #перехватываем исключение говорящее о том, что задача была отменена
    except asyncio.exceptions.CancelledError as e:
        print(f'Задача была отменена')
        raise


async def main():
    try:
        #создаем асинхронные задачи
        t1 = asyncio.create_task(async_func_exception())
        t2 = asyncio.create_task(async_func_exception())
        #даем им выполняться какое-то время
        await asyncio.sleep(1)
        #отменяем задачу 1
        t1.cancel()
        #собираем задачи вместе
        result = await asyncio.gather(t1, t2, return_exceptions=True)
        #печатаем результат
        print(result)
    except Exception as e:
        print(f'Exception: {e}')
    except asyncio.exceptions.CancelledError as e:
        print(f'Задача прервана {e}')
    print('Завершение выполнения асинхронных задач')



# фиксируем время начала
tm = time.time()
# запускаем основную корутину
asyncio.run(main())
print(f'Общее время работы {time.time() - tm}')
