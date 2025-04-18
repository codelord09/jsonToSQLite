# JSON to SQLite Sample Project

This project demonstrates how to read JSON data and store it in an SQLite database using Python. It includes a sample dataset of 30 books with detailed information about each book, including author details, genres, and ratings.

## Project Structure

- `json_to_sqlite.py`: Main Python script that handles JSON processing and database operations
- `sample_data.json`: Sample JSON file containing 30 book entries with nested data
- `books.db`: SQLite database file (created when running the script)
- `diagrams.md`: Mermaid diagrams showing database structure and data flow
- `requirements.txt`: No external dependencies required

## Features

- Reads nested JSON data with complex structure
- Creates SQLite database tables with proper schema
- Stores JSON data in normalized form
- Demonstrates basic database operations
- Includes comprehensive documentation and diagrams
- Sample dataset of 30 diverse books

## Setup and Running

1. Ensure you have Python 3.x installed on your system
2. Clone or download this repository
3. Run the script:
```bash
python json_to_sqlite.py
```

## Sample Data Structure

The sample JSON file contains book data with the following structure:
- Book information (id, title, publication year)
- Author details (name, birth year, nationality)
- Genres (as an array)
- Ratings (from both Goodreads and Amazon)

## Database Schema

The SQLite database contains a single table `books` with the following columns:
- id (INTEGER PRIMARY KEY)
- title (TEXT)
- publication_year (INTEGER)
- author_name (TEXT)
- author_birth_year (INTEGER)
- author_nationality (TEXT)
- genres (TEXT, comma-separated)
- goodreads_rating (REAL)
- amazon_rating (REAL)

## Data Flow

1. The script reads the JSON data from `sample_data.json`
2. Creates a new SQLite database file `books.db`
3. Creates the books table with the appropriate schema
4. Processes each book entry and inserts it into the database
5. Displays the results of the insertion

## Diagrams

The project includes several Mermaid diagrams in `diagrams.md` that visualize:
- Entity Relationship Diagram (ERD)
- Data Flow Diagram
- Class Diagram
- Sequence Diagram
- Database Schema
- Data Processing Flow

## Notes

- No external dependencies required (uses Python's built-in modules)
- The script handles nested JSON data and flattens it for SQLite storage
- Genres are stored as comma-separated strings in the database
- The script includes error handling and proper database connection management 