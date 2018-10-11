import docker


def this_works():
    client = docker.from_env()
    client.images.build(path='.', tag="alpine:test")
    print(client.containers.run(image="alpine:test", auto_remove=True))
    # print(client.containers.run("alpine", ["echo", "hello world"]))


this_works()
