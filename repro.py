import time

from prefect import flow, get_run_logger, task
from prefect.task_runners import ConcurrentTaskRunner

N = 1000


@task
def f(x):
    pass


def main():
    for _ in range(1):
        start = time.time()
        tasks = [f.submit(i) for i in range(N)]
        submitted = time.time()
        with open("time.txt", "w") as file_:
            file_.write(str(submitted - start))
        get_run_logger().info("Submitted tasks in %.3f seconds", submitted - start)
    return


if __name__ == "__main__":
    # asyncio.run(flow(task_runner=DaskTaskRunner())(main)())
    # asyncio.run(flow(task_runner=ConcurrentTaskRunner())(main)())
    flow(task_runner=ConcurrentTaskRunner())(main)()
