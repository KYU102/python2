SELECT 
	name,
    language,
    percentage
    
FROM countries
JOIN languages 
	on languages.country_id = countries.id
WHERE language = 'Slovene';


SELECT 
	countries.name, 
    count(cities.name) AS num_of_cities
    
FROM countries
JOIN cities 
	ON cities.country_id = countries.id
GROUP BY countries.name 
ORDER BY num_of_cities DESC


SELECT *
FROM cities
WHERE population > 500000 
ORDER BY population DESC

SELECT * 
FROM languages
WHERE percentage > 89
ORDER BY percentage DESC


SELECT countries.name, countries.surface_area, countries.population
FROM countries
JOIN cities ON cities.country_id = countries.id
WHERE countries.surface_area < 501 AND countries.population >100000



SELECT *
FROM countries
WHERE government_form LIKE '%Constitutional Monarchy%' AND capital > 200 AND life_expectancy > 75


SELECT 
	countries.name AS country_name, 
    cities.name AS city_name, 
    district, 
    cities.population AS city_population
    
FROM countries
JOIN cities ON cities.country_id = countries.id
WHERE district = 'Buenos Aires' AND cities.population > 500000


SELECT region, count(name) AS tot_countries
FROM countries
GROUP BY region
ORDER BY tot_countries DESC

