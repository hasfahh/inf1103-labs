FROM python:3.13-slim

WORKDIR /app

COPY supplier.py .
COPY product.py .
COPY physical_product.py .
COPY digital_product.py .
COPY can_be_shipped.py .
COPY product_factory.py .
COPY inventory.py .
COPY order_line.py .
COPY order.py .
COPY discount_strategy.py .
COPY input_helpers.py .
COPY product_loader.py .
COPY main.py .
COPY predict_first.py .
COPY products.csv .
COPY tests/ tests/

CMD ["python", "main.py"]