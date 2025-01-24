FROM python:3.9-slim

WORKDIR /raspberrypi-lcd-status

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "lcd_monitor.py"]
