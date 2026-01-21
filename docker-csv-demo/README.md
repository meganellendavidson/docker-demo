
Running in attached mode where Docker Compose keeps the terminal connected to show the containers output
```bash
docker compose up --build
```

adding `-d` will run the containers in the background, you'll need to use:

To view the logs/output
```bash
docker compose logs
```

To stop them
```bash
docker compose down
```
