from pathlib import Path
import os
import sys
from celery import Celery

CELERY_IP = os.environ["CELERY_IP"]
CELERY_PORT = os.environ["CELERY_PORT"]
CELERY_NAME = os.environ["CELERY_NAME"]
CELERY_WORKER = os.environ["CELERY_WORKER"]
CELERY_TASK = os.environ["CELERY_TASK"]

celery_app = Celery(
    CELERY_NAME, broker=f"redis://{CELERY_IP}:{CELERY_PORT}", backend=f"redis://{CELERY_IP}:{CELERY_PORT}"
)

def deploy_public_model(changed_models):
    celery_job = celery_app.send_task(f"{CELERY_WORKER}.{CELERY_TASK}", args=([changed_models]))
    return True


if __name__ == "__main__":
    changed_files = sys.argv[1:]
    changed_models = [str(Path(x).parents[-4]) for x in changed_files if x.startswith("models/")]
    changed_models = list(set(changed_models))
    print(changed_models)
    if changed_models != []:
        deploy_public_model(changed_models)