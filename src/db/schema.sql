DROP TABLE IF EXISTS Book;
DROP TABLE IF EXISTS Author;
DROP TABLE IF EXISTS Category;
DROP TABLE IF EXISTS BookAuthor;
DROP TABLE IF EXISTS BookCategory;


CREATE TABLE Book
(
    isbn                NVARCHAR(50) PRIMARY KEY,
    title               TEXT      NOT NULL,
    date_of_publication DATE NULL,
    created             TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Author
(
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    name          TEXT      NOT NULL,
    created       TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    date_of_birth DATE      NOT NULL
);

CREATE TABLE Category
(
    id      INTEGER PRIMARY KEY AUTOINCREMENT,
    name    TEXT      NOT NULL,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE BookAuthor
(
    isbn      NVARCHAR(50) NOT NULL,
    author_id INTEGER NOT NULL,
    FOREIGN KEY (isbn)
        REFERENCES Book (isbn)
        ON DELETE CASCADE
        ON UPDATE NO ACTION,
    FOREIGN KEY (author_id)
        REFERENCES Author (id)
        ON DELETE CASCADE
        ON UPDATE NO ACTION
);

CREATE TABLE BookCategory
(
    isbn        NVARCHAR(50) NOT NULL,
    category_id INTEGER NOT NULL,
    FOREIGN KEY (isbn)
        REFERENCES Book (isbn)
        ON DELETE CASCADE
        ON UPDATE NO ACTION,
    FOREIGN KEY (category_id)
        REFERENCES Category (id)
        ON DELETE CASCADE
        ON UPDATE NO ACTION
);

CREATE UNIQUE INDEX category_name_index on Category (name);
CREATE UNIQUE INDEX author_name_index on Author (name);
