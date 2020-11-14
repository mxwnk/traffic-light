import jenkins

from config import jenkins_url, jenkins_user, jenkins_password, jenkins_job
from .build_status import BuildStatus

server = jenkins.Jenkins(jenkins_url, username=jenkins_user, password=jenkins_password)


def get_latest_build_status() -> BuildStatus:
    latest_build = server.get_job_info(jenkins_job)['jobs'][0]
    return map_color(latest_build['color'])


def map_color(color: str) -> BuildStatus:
    if color == 'red':
        return BuildStatus.RED
    if color == 'yellow':
        return BuildStatus.YELLOW
    if color == 'green':
        return BuildStatus.GREEN

    raise Exception('Unable to map build color:' + color)
