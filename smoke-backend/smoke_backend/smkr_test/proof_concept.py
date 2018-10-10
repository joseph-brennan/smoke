import docker

def this_works():
    client = docker.from_env()
    
    client.container.run("alpine", ["echo", "hello world"])
