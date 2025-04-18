# Book Database Diagrams

## Entity Relationship Diagram (ERD)

```mermaid
erDiagram
    BOOKS ||--o{ GENRES : has
    BOOKS ||--|| AUTHORS : written_by
    BOOKS ||--|| RATINGS : has

    BOOKS {
        int id PK
        string title
        int publication_year
    }

    AUTHORS {
        string name
        int birth_year
        string nationality
    }

    GENRES {
        string name
    }

    RATINGS {
        float goodreads
        float amazon
    }
```

## Data Flow Diagram

```mermaid
flowchart TD
    A[JSON File] -->|Read| B[Python Script]
    B -->|Process| C[SQLite Database]
    C -->|Query| D[Results]
    B -->|Display| E[Console Output]
    
    subgraph Input
    A
    end
    
    subgraph Processing
    B
    end
    
    subgraph Storage
    C
    end
    
    subgraph Output
    D
    E
    end
```

## Class Diagram

```mermaid
classDiagram
    class Book {
        +int id
        +string title
        +int publication_year
        +Author author
        +string[] genres
        +Ratings ratings
    }
    
    class Author {
        +string name
        +int birth_year
        +string nationality
    }
    
    class Ratings {
        +float goodreads
        +float amazon
    }
    
    Book "1" -- "1" Author : has
    Book "1" -- "1" Ratings : has
    Book "1" -- "*" Genre : has
```

## Sequence Diagram

```mermaid
sequenceDiagram
    participant User
    participant Script
    participant JSON
    participant SQLite
    
    User->>Script: Run script
    Script->>JSON: Read sample_data.json
    JSON-->>Script: Return book data
    Script->>SQLite: Create tables
    Script->>SQLite: Insert book records
    loop For each book
        Script->>SQLite: Insert book data
        SQLite-->>Script: Confirm insertion
    end
    Script->>SQLite: Query all books
    SQLite-->>Script: Return results
    Script->>User: Display results
```

## Database Schema Visualization

```mermaid
graph TD
    subgraph books_table
        id[ID: INTEGER PRIMARY KEY]
        title[Title: TEXT]
        pub_year[Publication Year: INTEGER]
        author_name[Author Name: TEXT]
        author_birth[Author Birth Year: INTEGER]
        author_nat[Author Nationality: TEXT]
        genres[Genres: TEXT]
        goodreads[Goodreads Rating: REAL]
        amazon[Amazon Rating: REAL]
    end
```

## Data Processing Flow

```mermaid
flowchart LR
    subgraph Input
        JSON[JSON Data]
    end
    
    subgraph Processing
        Parse[Parse JSON]
        Normalize[Normalize Data]
        Transform[Transform Genres]
    end
    
    subgraph Output
        DB[SQLite Database]
    end
    
    JSON --> Parse
    Parse --> Normalize
    Normalize --> Transform
    Transform --> DB
```

These diagrams provide different perspectives on the book database system:

1. The ERD shows the relationships between different entities in the database
2. The Data Flow Diagram illustrates how data moves through the system
3. The Class Diagram represents the object-oriented structure of the data
4. The Sequence Diagram shows the step-by-step process of data handling
5. The Database Schema shows the actual table structure
6. The Data Processing Flow shows how the data is transformed from JSON to SQLite

Each diagram uses Mermaid's syntax and can be rendered in any Markdown viewer that supports Mermaid diagrams. 