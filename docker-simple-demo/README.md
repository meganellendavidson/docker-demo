
### Build Docker Image

```bash
docker build -t ascii-art .
```

`-t ascii-art` gives the image a name/tag. the `.` tells docker to look for the Dockerfile in the current directory.

This may take longer the first time you run  it as it creates a temporay container for each instruction, if you change the Dockerfile and rebuild, Docker will reuse cached layers up to the first change in instruction, which will make it faster.

### Run your container

```bash
docker run ascii-art
```

#### Rebuilding

you can rebuild over your original image or you can tag it as `v2` for example:

```bash
docker build -t ascii-art:v2 .

docker run ascii-art:v2
```
