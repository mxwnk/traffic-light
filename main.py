import sched
import time

from config import update_interval
from src.jenkins.build_status import BuildStatus
from src.jenkins.jenkins_client import get_latest_build_status
from src.traffic_light import get_traffic_light

scheduler = sched.scheduler(time.time, time.sleep)
traffic_light = get_traffic_light()


def update_traffic_light():
    try:
        current_build_status = get_latest_build_status()
        print("Current Builld Status:" + str(current_build_status))

        if current_build_status is BuildStatus.RED:
            traffic_light.display_red()
        if current_build_status is BuildStatus.GREEN:
            traffic_light.display_green()
        if current_build_status is BuildStatus.YELLOW:
            traffic_light.display_yellow()

        schedule_update()
    except Exception as e:
        print("Error updating traffig light:" + e)


def schedule_update():
    scheduler.enter(update_interval, 1, update_traffic_light)


schedule_update()

print("Start Jenkins Traffic Light")
scheduler.run()
