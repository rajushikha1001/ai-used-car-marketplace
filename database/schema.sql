CREATE TABLE cars (
  id SERIAL PRIMARY KEY,
  make VARCHAR(50),
  model VARCHAR(50),
  year INT,
  mileage INT,
  price DECIMAL(10, 2),
  condition VARCHAR(20),
  location VARCHAR(100)
);

CREATE TABLE reviews (
  id SERIAL PRIMARY KEY,
  car_id INT,
  user_id INT,
  review TEXT,
  sentiment VARCHAR(20),
  FOREIGN KEY (car_id) REFERENCES cars(id)
);

CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100),
  email VARCHAR(100)
);
