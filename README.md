# traffic-analytics-api

**High-performance async backend for collecting and analyzing real-time traffic data**

##  Features
- Async processing for **parallel requests**
- Traffic aggregation & scoring (congestion, incidents, intensity)
- **PostgreSQL storage**
- **Docker-based deployment**
- Environment variable configuration

##  Tech Stack
- Litestar, Python 3, PostgreSQL
- Async (asyncio/aiohttp style requests), Docker

## Installation & Run

1. Install dependencies:
- bash
- pip install -r requirements.txt

# Run PostgreSQL via Docker:

- docker run --name traffic-db -e POSTGRES_PASSWORD=pass -p 5432:5432 postgres

# Run API server:

- uvicorn app.main:app --reload

# Achievements

- Backend collects and processes data asynchronously
- Database stores structured regional traffic reports
- 100% automation of traffic scoring pipeline
