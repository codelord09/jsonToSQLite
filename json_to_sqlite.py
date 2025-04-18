"""Cursor Command to generate diagram.md : Create diagrams in markdown using mermaid fenced code blocks:"""

import json
import sqlite3
from typing import Dict, List
from logger_config import setup_logger

# Set up logger
logger = setup_logger()


def create_tables(conn: sqlite3.Connection) -> None:
    """Create necessary tables in the SQLite database."""
    cursor = conn.cursor()

    try:
        # Create books table
        cursor.execute(
            """
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            publication_year INTEGER,
            author_name TEXT,
            author_birth_year INTEGER,
            author_nationality TEXT,
            genres TEXT,
            goodreads_rating REAL,
            amazon_rating REAL
        )
        """
        )

        conn.commit()
        logger.info("Database table 'books' created successfully")
    except sqlite3.Error as e:
        logger.error(f"Error creating database tables: {str(e)}")
        raise


def insert_book(conn: sqlite3.Connection, book: Dict) -> None:
    """Insert a book record into the database."""
    cursor = conn.cursor()

    try:
        # Convert genres list to comma-separated string
        genres_str = ",".join(book["genres"])

        cursor.execute(
            """
        INSERT OR REPLACE INTO books (
            id, title, publication_year, author_name, author_birth_year,
            author_nationality, genres, goodreads_rating, amazon_rating
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
            (
                book["id"],
                book["title"],
                book["publication_year"],
                book["author"]["name"],
                book["author"]["birth_year"],
                book["author"]["nationality"],
                genres_str,
                book["ratings"]["goodreads"],
                book["ratings"]["amazon"],
            ),
        )

        conn.commit()
        logger.debug(
            f"Book inserted successfully - ID: {book['id']}, Title: {book['title']}, Author: {book['author']['name']}"
        )
    except sqlite3.Error as e:
        logger.error(
            f"Error inserting book - ID: {book['id']}, Title: {book['title']}: {str(e)}"
        )
        raise


def main():
    try:
        # Read JSON data
        logger.info("Starting JSON data import process")
        with open("sample_data.json", "r") as file:
            data = json.load(file)
        logger.info(f"JSON data loaded successfully - Found {len(data['books'])} books")

        # Connect to SQLite database
        logger.info("Establishing database connection")
        conn = sqlite3.connect("books.db")

        try:
            # Create tables
            logger.info("Initializing database schema")
            create_tables(conn)

            # Insert books
            logger.info("Beginning book insertion process")
            for book in data["books"]:
                insert_book(conn, book)

            # Query and display results
            logger.info("Querying database for verification")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM books")
            rows = cursor.fetchall()

            logger.info(
                f"Database verification complete - Total books in database: {len(rows)}"
            )
            for row in rows:
                logger.debug(
                    f"Database entry - ID: {row[0]}, Title: {row[1]}, Author: {row[3]}"
                )

        except sqlite3.Error as e:
            logger.error(f"Database operation failed: {str(e)}")
            raise
        finally:
            conn.close()
            logger.info("Database connection closed successfully")

    except FileNotFoundError:
        logger.error("Required file 'sample_data.json' not found")
        raise
    except json.JSONDecodeError as e:
        logger.error(f"JSON parsing error: {str(e)}")
        raise
    except Exception as e:
        logger.error(f"Unexpected error occurred: {str(e)}")
        raise


if __name__ == "__main__":
    main()
