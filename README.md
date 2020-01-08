# Convert NFS to GCS
## # Usage
You can use `docker run` to do this or using `docker-compose` I wrote below. 

### ## Docker-compose
```yaml
# docker-compose.yml
version: "3"

services:
  app:
    image: vietanhs0817/convert-to-gcs:latest
    # This command bellow support for revert when something wrong
    # command: ["-a", "revert", "-f", "/app/changelog/changelog_2020_01_08.json"]
    tty: true
    volumes:
      - ./changelog:/app/changelog
    # You can use env file
    env_file:
      - .env
    # or environment
    # environment:
    #   GCS: "GCS_BASE64"
    #   DATABASE_URI: "DATABASE_CONNECTION_STRING"
    #   GCS_BUCKET: "BUCKET_NAME"
```
```shell script
docker-compose up
```
