# Text Embedding Cosine Similarity Tool

This tool calculates the cosine similarity between two text strings using OpenAI's text embeddings.

## Prerequisites

- Docker and Docker Compose installed
- OpenAI API key

## Quick Start

1. **Clone this repository**

```bash
git clone git@github.com:adorosario/compute-cosine-similarity-embeddings.git
cd compute-cosine-similarity-embeddings
```

2. **Set up your OpenAI API key**

Create a `.env` file from the example:
```bash
cp .env.example .env
```

Then edit the `.env` file and add your OpenAI API key:
```
OPENAI_API_KEY=your_openai_api_key_here
```

3. **Run with Docker Compose**

```bash
docker-compose up -d
docker-compose exec app bash
python similarity.py "This is the first string" "This is the second string"
```

## Usage Examples

Compare two phrases:
```bash
pythong similarity.py "The quick brown fox jumps over the lazy dog" "A fast auburn fox leaps above the sleepy canine"
```

## Running without Docker

If you prefer to run without Docker:

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Create and edit the `.env` file with your OpenAI API key:
```
OPENAI_API_KEY=your_openai_api_key_here
```

3. Run the script:
```bash
python similarity.py "First string" "Second string"
```

## How It Works

The tool uses OpenAI's `text-embedding-3-small` model to:
1. Convert both text strings into vector embeddings
2. Calculate the cosine similarity between these vectors
3. Return a similarity score between 0 and 1 (where 1 means identical)

## Customizing

To modify the Docker setup:
- Edit `docker-compose.yml` to change environment variables or volume mounts
- Edit `Dockerfile` if you need additional packages or a different Python version

## File Structure

- `similarity.py`: Main script that performs the text similarity calculation
- `Dockerfile`: Defines the Docker image for the application
- `docker-compose.yml`: Sets up the service with environment variables and volumes
- `requirements.txt`: Lists Python package dependencies
