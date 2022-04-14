INSERT INTO dojos (name, created_at, updated_at) 
VALUES('Seattle', now(), now());

INSERT INTO dojos (name, created_at, updated_at) 
VALUES('San Jose', now(), now());

INSERT INTO dojos (name, created_at, updated_at) 
VALUES('San Francisco', now(), now());	

DELETE FROM dojos WHERE dojo_id < 4

INSERT INTO dojos (name, created_at, updated_at) 
VALUES('Seattle', now(), now());

INSERT INTO dojos (name, created_at, updated_at) 
VALUES('San Jose', now(), now());

INSERT INTO dojos (name, created_at, updated_at) 
VALUES('San Francisco', now(), now());	

INSERT INTO ninjas (first_name, last_name, age, dojo_id, created_at, updated_at) 
VALUES('Kevin', 'Yu', 25, 4, now(), now());

INSERT INTO ninjas (first_name, last_name, age, dojo_id, created_at, updated_at) 
VALUES('Jane', 'Doe', 31, 4, now(), now());

INSERT INTO ninjas (first_name, last_name, age, dojo_id, created_at, updated_at) 
VALUES('John', 'DOe', 44, 4, now(), now());

INSERT INTO ninjas (first_name, last_name, age, dojo_id, created_at, updated_at) 
VALUES('Michael', 'Choi', 26, 5, now(), now());

INSERT INTO ninjas (first_name, last_name, age, dojo_id, created_at, updated_at) 
VALUES('Kevin', 'Nguyen', 21, 5, now(), now());

INSERT INTO ninjas (first_name, last_name, age, dojo_id, created_at, updated_at) 
VALUES('Alex', 'Tran', 34, 5, now(), now());

INSERT INTO ninjas (first_name, last_name, age, dojo_id, created_at, updated_at) 
VALUES('Daniel', 'Kim', 36, 6, now(), now());

INSERT INTO ninjas (first_name, last_name, age, dojo_id, created_at, updated_at) 
VALUES('Jake', 'Myers', 61, 6, now(), now());

INSERT INTO ninjas (first_name, last_name, age, dojo_id, created_at, updated_at) 
VALUES('Morgan', 'Tran', 54, 6, now(), now());

SELECT *
FROM ninjas
WHERE dojo_id = 4

SELECT *
FROM ninjas
WHERE dojo_id = 6

SELECT name AS 'dojo_name'
FROM ninjas
JOIN dojos on dojos.dojo_id = ninjas.dojo_id
ORDER BY ninjas.id DESC
LIMIT 1;
