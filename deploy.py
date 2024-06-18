from pathlib import Path
import os
import sys
from celery import Celery

CELERY_IP = os.environ["CELERY_IP"]
CELERY_PORT = os.environ["CELERY_PORT"]
CELERY_NAME = os.environ["CELERY_NAME"]

celery_app = Celery(
    CELERY_NAME, broker=f"redis://{CELERY_IP}:{CELERY_PORT}", backend=f"redis://{CELERY_IP}:{CELERY_PORT}"
)

if __name__ == "__main__":
    changed_files = sys.argv[1:]
    changed_models = [Path(x).parents[-3] for x in changed_files if x.startswith("models/")]
    changed_models = list(set(changed_models))
    print(changed_models)
    # if changed_models != []:
    #     pipeline(changed_models)