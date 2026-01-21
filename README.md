

## Managing Docker Images

Dont just use 'latest' - use semantic versioning

```bash
docker build -t myapp:1.0.0 .
```

Tag something as the latests if it is the current version

```bash
docker tag myapp:1.0.0 myapp:latest
```

Listing images

```bash
docker images
```

Cleaning up unused images

```bash
docker image prune
```

more aggressive cleanup (be careful!)

```bash
docker system prune -a
```
