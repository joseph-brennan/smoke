import docker


def this_works():
    
    client = docker.from_env()
    client.containers.build()
    print(client.containers.run("alpine", ["echo", "hello world"]))


this_works()
