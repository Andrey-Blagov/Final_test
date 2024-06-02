-- Создать базу данных
CREATE DATABASE Human_Friends;
USE Human_Friends;

-- Создать таблицы
CREATE TABLE Pets (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    type VARCHAR(50),
    commands TEXT,
    birth_date DATE
);

CREATE TABLE Pack_Animals (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    type VARCHAR(50),
    commands TEXT,
    birth_date DATE
);

-- Заполнить таблицы данными
INSERT INTO Pets (name, type, commands, birth_date) VALUES
('Bobby', 'Dogs', 'sit, lie down', '2021-01-10'),
('Murka', 'Cats', 'meow', '2020-05-15'),
('Snowy', 'Hamsters', 'run', '2022-03-20');

INSERT INTO Pack_Animals (name, type, commands, birth_date) VALUES
('Bucephalus', 'Horses', 'gallop', '2019-02-25'),
('Camel', 'Camels', 'carry load', '2018-11-11'),
('Eeyore', 'Donkeys', 'carry load', '2021-06-05');

-- Удалить верблюдов из таблицы Pack_Animals
DELETE FROM Pack_Animals WHERE type = 'Camels';

-- Объединить таблицы лошадей и ослов в одну таблицу
CREATE TABLE Horses_And_Donkeys AS
SELECT * FROM Pack_Animals WHERE type IN ('Horses', 'Donkeys');

-- Создать новую таблицу для молодых животных
CREATE TABLE Young_Animals AS
SELECT *, TIMESTAMPDIFF(MONTH, birth_date, CURDATE()) AS age_in_months
FROM (
    SELECT name, type, commands, birth_date
    FROM Pets
    UNION ALL
    SELECT name, type, commands, birth_date
    FROM Pack_Animals
) AS combined
WHERE birth_date > DATE_SUB(CURDATE(), INTERVAL 3 YEAR)
AND birth_date <= DATE_SUB(CURDATE(), INTERVAL 1 YEAR);

-- Объединить все таблицы в одну
CREATE TABLE All_Animals AS
SELECT *, 'Pets' AS previous_table FROM Pets
UNION ALL
SELECT *, 'Pack_Animals' AS previous_table FROM Pack_Animals;
