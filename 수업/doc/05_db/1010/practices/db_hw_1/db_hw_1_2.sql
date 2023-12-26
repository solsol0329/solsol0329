CREATE TABLE users (
  email TEXT NOT NULL UNIQUE,
  name TEXT NOT NULL,
  age INTEGER NOT NULL,
  phoneNumber VARCHAR(20) NOT NULL,
  gender INTEGER,
  address VARCHAR(50) NOT NULL default 'no address'
);

ALTER TABLE users
RENAME COLUMN phoneNumber TO number;

DROP TABLE users;

PRAGMA table_info('users')