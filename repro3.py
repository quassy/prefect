from prefect import flow, get_run_logger, task


@task
def say_hi(user_name: str):
    logger = get_run_logger()
    logger.info("Hello from Prefect 2.0, %s!", user_name)


@flow
def hello(user: str = "Marvin"):
    say_hi(user)
