FROM python:3.11-slim
WORKDIR /app
COPY . /app
EXPOSE 8528
CMD ["python", "bloom_mesh_node.py", "8528"]
