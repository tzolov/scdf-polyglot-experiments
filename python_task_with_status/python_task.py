import sys
import time

from util.task_status import TaskStatus
from util.task_args import get_task_id, get_db_url, get_task_name

try:
    status = TaskStatus(get_task_id(), get_db_url())

    # Update task status to started
    status.started()

    # Do something
    print('Start task:{}, id:{}, url:{}'.format(get_task_name(), get_task_id(), get_db_url()))
    print('Wait for 60 seconds ...')
    sys.stdout.flush()
    time.sleep(60)
    print("Goodbye!")

    # Update the status to successfully completed
    status.completed()

except Exception:
    msg = "Unexpected error:", sys.exc_info()[0]
    status.failed(1, msg, msg)


