import jenkins

from config import jenkins_url, jenkins_user, jenkins_password, jenkins_job, jenkins_branch
from .build_status import BuildStatus

server = jenkins.Jenkins(jenkins_url, username=jenkins_user, password=jenkins_password)


def get_latest_build_status() -> BuildStatus:
    all_jobs = server.get_job_info(jenkins_job)['jobs']
    expected_job = find_job_by_branch(all_jobs, jenkins_branch)
    return map_color(expected_job['color'])


def find_job_by_branch(all_jobs, branch: str):
    return list(filter(lambda job: job['name'] == branch, all_jobs))[0]


def map_color(color: str) -> BuildStatus:
    if color == 'red':
        return BuildStatus.FAILED
    if color == 'yellow':
        return BuildStatus.BUILDING
    if color == 'blue':
        return BuildStatus.OK

    raise Exception('Unable to map build color:' + color)
