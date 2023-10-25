import time
import asyncio


# стандартный обработчик исключений
def handle_exception(loop, context):
    # context["message"] will always be there; but context["exception"] may not
    msg = context.get("exception", context["message"])
    print(f"Перехвачено исключение: {msg}")
    print("Выполняем очистку ресурсов...")


# асинхронная функция с вызовом исключения
async def async_func_exception():
    print(f'Асинхронная задача начата')
    await asyncio.sleep(1)
    raise RuntimeError('Во время выполнения асинхронной задачи произошел сбой')


# основная асинхронная функция
async def main():
    try:
        # добавляем обработчик исключений к циклу событий
        loop = asyncio.get_event_loop()
        loop.set_exception_handler(handle_exception)
        # работаем дальше как обычно
        task1 = asyncio.create_task(async_func_exception())
        task2 = asyncio.create_task(async_func_exception())
        await asyncio.wait([task1, task2])
    except Exception as e:
        print(f'Exception: {e}')
    print('Завершение выполнения асинхронных задач')


# фиксируем время начала
tm = time.time()
# запускаем основную корутину
asyncio.run(main())
print(f'Общее время работы {time.time() - tm}')
