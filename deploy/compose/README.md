# Local Deployment

It requires privileged access due to a [subnet network configuration](https://eclipse-ecal.github.io/ecal/getting_started/cloud.html) and shared memory between ecal nodes.

## Using podman-compose

Doesn't work due to some issues when sharing network and pid  with the host machine.

## Using podman

Start the subscriber container:

```sh
podman run \
  -it \
  -v $PWD/volumes/ecal:/etc/ecal \
  --network host \
  --pid host \
  --ipc host \
  --cap-add ALL \
  quay.io/lrossett/ecal-cpp-subscriber:latest-f37 \
  /opt/app/_build/hello_world_rec
```

Start the publisher container:

```
podman run \
  -it \
  -v $PWD/volumes/ecal:/etc/ecal \
  --network host \
  --ipc host \
  --cap-add ALL \
  quay.io/lrossett/ecal-cpp-publisher:latest-f37 \
  /opt/app/_build/hello_world_snd
```
