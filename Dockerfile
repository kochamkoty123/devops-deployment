# Lekki oficjalny obraz Pythona
FROM python:3.9-slim

# Ustawienie katalogu roboczego wewnątrz kontenera
WORKDIR /app

# Ustawienia środowiska Pythona (brak plików .pyc i brak buforowania logów)
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Kopiowanie i instalacja zależności (osobna warstwa dla szybszego budowania)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Kopiowanie kodu źródłowego aplikacji
COPY . .

# Oznaczenie portu aplikacji
EXPOSE 5000

# Komenda uruchamiająca aplikację
CMD ["python", "app.py"]
