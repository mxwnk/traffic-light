import sched
import time

from config import update_interval
from src.jenkins.build_status import BuildStatus
from src.jenkins.jenkins_client import get_latest_build_status
from src.logger import print_message
from src.traffic_light import get_traffic_light

scheduler = sched.scheduler(time.time, time.sleep)
traffic_light = get_traffic_light()


def update_traffic_light():
    try:
        current_build_status = get_latest_build_status()
        print_message(str(current_build_status))

        if current_build_status is BuildStatus.FAILED:
            traffic_light.display_red()
        if current_build_status is BuildStatus.OK:
            traffic_light.display_green()
        if current_build_status is BuildStatus.BUILDING:
            traffic_light.display_yellow()

        schedule_update()
    except Exception as e:
        print_message(e)
        traffic_light.display_error(e)


def schedule_update():
    print_message('Next Update in ' + str(update_interval) + ' seconds')
    scheduler.enter(update_interval, 1, update_traffic_light)


print_message("---- Start Traffic Light Monitor ----")
schedule_update()
update_traffic_light()
scheduler.run()
