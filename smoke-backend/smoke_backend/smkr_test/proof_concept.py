import docker

def this_works():
    client = docker.from_env()
    
    print(client.containers.run("alpine", ["echo", "hello world"]))

this_works()
