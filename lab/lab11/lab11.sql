.read lab11_data.sql


CREATE TABLE bluedog AS
  SELECT color, pet FROM students WHERE color = "blue" AND pet = "dog";

CREATE TABLE bluedog_songs AS
  SELECT color, pet, song FROM students WHERE color = "blue" AND pet = "dog";


CREATE TABLE smallest_int_having AS
  SELECT time,smallest FROM students GROUP BY smallest HAVING COUNT(*) = 1;


CREATE TABLE matchmaker AS
  SELECT s1.pet, s1.song, s1.color, s2.color FROM students AS s1, students AS s2 WHERE s1.time < s2.time AND s1.pet = s2.pet AND s1.song = s2.song;


CREATE TABLE sevens AS
  SELECT students.seven FROM students, numbers WHERE students.time = numbers.time AND students.number = 7  AND numbers."7" = "True";


CREATE TABLE avg_difference AS
  SELECT round(avg(abs(number - smallest))) FROM students;

