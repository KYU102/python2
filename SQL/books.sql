INSERT INTO authors (name, created_at, updated_at) 
VALUES('Jane Austen', now(), now());

INSERT INTO authors (name, created_at, updated_at) 
VALUES('Emily Dickinson', now(), now());

INSERT INTO authors (name, created_at, updated_at) 
VALUES('Fyodor Dostoevsky', now(), now());

INSERT INTO authors (name, created_at, updated_at) 
VALUES('William Shakespeare', now(), now());

INSERT INTO authors (name, created_at, updated_at) 
VALUES( 'Lau Tzu', now(), now());

INSERT INTO books (id, title, num_of_pages, created_at, updated_at) 
VALUES(7, 'C Sharp', 100, now(), now());

INSERT INTO books (id, title, num_of_pages, created_at, updated_at) 
VALUES(8, 'Java', 110, now(), now());

INSERT INTO books (id, title, num_of_pages, created_at, updated_at) 
VALUES(9, 'Python', 120, now(), now());

INSERT INTO books (id, title, num_of_pages, created_at, updated_at) 
VALUES(10, 'PHP', 130, now(), now());

INSERT INTO books (id, title, num_of_pages, created_at, updated_at) 
VALUES(11, 'Ruby', 410, now(), now());

UPDATE books 
SET title = 'C#' 
WHERE id = 7

UPDATE authors 
SET name = 'Bill Shakespeare' 
WHERE id = 9

INSERT INTO favorites (id, authors_id, books_id) 
VALUES(1, 6, 7);

INSERT INTO favorites (id, authors_id, books_id) 
VALUES(2, 6, 8);

INSERT INTO favorites (id, authors_id, books_id) 
VALUES(3, 7, 7);

INSERT INTO favorites (id, authors_id, books_id) 
VALUES(4, 7, 8);

INSERT INTO favorites (id, authors_id, books_id) 
VALUES(5, 7, 9);

INSERT INTO favorites (id, authors_id, books_id) 
VALUES(6, 8, 7);

INSERT INTO favorites (id, authors_id, books_id) 
VALUES(7, 8, 8);

INSERT INTO favorites (id, authors_id, books_id) 
VALUES(8, 8, 9);

INSERT INTO favorites (id, authors_id, books_id) 
VALUES(9, 8, 10);

INSERT INTO favorites (id, authors_id, books_id) 
VALUES(10, 9, 7);

INSERT INTO favorites (id, authors_id, books_id) 
VALUES(11, 9, 8);

INSERT INTO favorites (id, authors_id, books_id) 
VALUES(12, 9, 9);

INSERT INTO favorites (id, authors_id, books_id) 
VALUES(13, 9, 10);

INSERT INTO favorites (id, authors_id, books_id) 
VALUES(14, 9, 11);

SELECT *
FROM authors
JOIN favorites ON favorites.authors_id = authors.id
WHERE books_id = 9;

DELETE FROM favorites WHERE books_id = 10
LIMIT 1;

INSERT INTO favorites (id, authors_id, books_id) 
VALUES(15, 10, 8);

SELECT *
FROM authors
JOIN favorites ON favorites.authors_id = authors.id
JOIN books ON favorites.books_id = books.id
WHERE authors.id = 8;

SELECT *
FROM authors
JOIN favorites ON favorites.authors_id = authors.id
JOIN books ON favorites.books_id = books.id
WHERE books.id = 11;

select *
from favorites

-- INSERT INTO authors (name)
-- VALUES ("Jane Austin"),("Emily Dickinson"),("FYodor Dostoevsky"),("William Shakespeare"),("Lau Tzu");

-- INSERT INTO books (title, num_of_pages)
-- VALUES ("C Sharp",200),("Java",200),("Python",200),("PHP",200),("Ruby",200);

-- Update books SET title = "C#" 
-- WHERE title = "C Sharp";

-- UPDATE authors SET name = "Bill Shakespeare"
-- WHERE id = 4;

-- INSERT INTO favorites (author_id,book_id)
-- VALUES (1,1),(1,2),(2,1),(2,2),(2,3),(3,1),(3,2),(3,3),(3,4),(4,1),(4,2),(4,3),(4,4),(4,5);

