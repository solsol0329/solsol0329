CREATE TABLE contacts (
  email TEXT NOT NULL UNIQUE,
  name TEXT NOT NULL,
  age INTEGER NOT NULL
);
PRAGMA table_info('contacts');

INSERT INTO contacts(email, name, age)
values('ssafy2@ssafy.com', 'ssafy2', 10);

select rowid, * from contacts;
