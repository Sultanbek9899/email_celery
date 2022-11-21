from celery import task

@task
def get_sum():
    return 2 + 2
