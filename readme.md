# [exert-sanic](https://github.com/chaosannals/exert-sanic)

## 镜像

```sh
docker build -t exert-sanic .
```

## 容器

### 部署容器

```sh
docker run -v /host/app:/app -p 8000:8000 -d --name exert-sanic exert-sanic
```