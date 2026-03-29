# Simple Library Information System

This project, **Simple Library Information System**, is implemented in Python. It simulates basic operations of a digital library, including user registration, resource searching, borrowing and returning materials, and book reviews.

The system was designed to combine **library science concepts** with **basic programming techniques** such as functions, loops, and object-oriented programming.

---

## Project Motivation

With the rapid growth of digital libraries, library systems must manage not only collections but also user services and borrowing records.

This project aims to:

- Simulate the core operations of a library system
- Practice Python programming concepts
- Apply knowledge from **Library and Information Science**
- Explore how digital systems support library management

The project also introduces a **book review and rating feature**, which allows readers to evaluate materials and help other users select resources.

## Features

The system currently supports the following functions:

### 1. Search Library Resources
Users can search library collections to check resource information and availability.

### 2. Register Library Card
New users can register and obtain a **library card ID** generated from their birthdate.

### 3. User Login
Users must log in to access most functions such as borrowing or reviewing books.

### 4. Borrow Resources
Logged-in users can borrow available books or media resources.

### 5. Return Resources
Users can return borrowed materials and update the system status.

### 6. View User Information
Users can view their personal profile and borrowed items.

### 7. Add Library Resources (Librarian)
Librarians can add new resources into the library system.

### 8. Book Rating and Review
Users can rate books (1–5 stars) and leave comments.  
The system calculates an **average rating** for each item.

---

## System Design

The system is mainly built using **Object-Oriented Programming (OOP)**.

Main data objects include:

### User

Stores user information and borrowing records.

**Attributes**

- name
- gender
- birth
- phone
- email
- password
- borrowed resources
- library card ID

**Key functions**

- generate library card ID
- borrow resources
- return resources
- display user information

### Book

Represents a book in the library collection.

**Attributes**

- title
- author
- publisher
- ID number
- classification number
- availability
- rating records
- comments

**Key features**

- store user ratings
- calculate average rating
- display book information

### Journal

Represents journal resources with metadata such as:

- title
- subject
- publisher
- format
- publication frequency

## Media

Represents multimedia resources.

Attributes include:

- title
- author
- genre
- format
- duration
- description
- rating system (same as books)

---

## Project Structure
```text
Library-Information-System
│
├── classes.py
│   Defines the main system classes:
│   - User
│   - Book
│   - Journal
│   - Media
│
├── functions.py
│   Implements system operations and user interactions.
│
└── README.md
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/raechang21/Simple_Library_Information_System.git
```

### 2. Install dependencies

The project uses:
```text
numpy
```
Install it with:
```bash
pip install numpy
```

## Running the Program
Run the python program with:
```bash
python function.py
```

The system will display a main menu allowing users to select functions such as:
-	search resources
- register
-	login
-	borrow books
-	return books
-	rate books
