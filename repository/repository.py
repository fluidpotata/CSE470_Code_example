import sqlite3

def get_all_books():
    conn = sqlite3.connect('main.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM books')
    books = [{'id': row[0], 'title': row[1], 'author': row[2]} for row in cursor.fetchall()]
    conn.close()
    return books

def add_book(title, author):
    conn = sqlite3.connect('main.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO books (title, author) VALUES (?, ?)', (title, author))
    conn.commit()
    conn.close()

def delete_book(book_id):
    conn = sqlite3.connect('main.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM books WHERE id = ?', (book_id,))
    conn.commit()
    conn.close()
