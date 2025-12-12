-- Show the full description (columns) of the table Books
-- from the database alx_book_store using INFORMATION_SCHEMA.
-- Example usage:
--   mysql -u root -p alx_book_store < task_4.sql
--   mysql -u root -p -D alx_book_store < task_4.sql

SELECT
    COLUMN_NAME,
    COLUMN_TYPE,
    IS_NULLABLE,
    COLUMN_KEY,
    COLUMN_DEFAULT,
    EXTRA
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = 'alx_book_store'
  AND TABLE_NAME = 'Books'
ORDER BY ORDINAL_POSITION;