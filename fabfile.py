from fabric.api import run, env, local, put, sudo, task, reboot, parallel

env.use_ssh_config = True

@task
def whats_the_time():
    run("date")
