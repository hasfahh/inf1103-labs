FROM python:3.13-slim

WORKDIR /app

COPY product.py .
COPY physical_product.py .
COPY digital_product.py .
COPY can_be_shipped.py .
COPY inventory.py .
COPY main.py .
COPY test_products.py .

CMD ["python", "main.py"]