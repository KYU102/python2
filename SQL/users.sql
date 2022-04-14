INSERT INTO users (first_name, last_name, email, created_at, update_at) 
VALUES('kevin', 'yu', 'kyu@gmail.com', now(), now());

INSERT INTO users (first_name, last_name, email, created_at, update_at) 
VALUES('john', 'doe', 'jd@gmail.com', now(), now());

INSERT INTO users (first_name, last_name, email, created_at, update_at) 
VALUES('jane', 'doe', 'hane@gmail,com', now(), now());

select *
from users

SELECT *
FROM users
WHERE email = 'kyu@gmail.com'

SELECT *
FROM users
WHERE id = 3

UPDATE users
SET last_name = 'pancakes'
WHERE id = 3

DELETE FROM users WHERE id = 2

SELECT *
FROM users 
ORDER BY first_name;

SELECT *
FROM users 
ORDER BY first_name DESC;


