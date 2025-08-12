# Write your MySQL query statement below
with temp as (
    select book_id, count(*) as cnt
    from borrowing_records
    where return_date is null
    group by book_id
),
temp1 as (
    select l.*, t.cnt as cnt
    from library_books l join temp t
    on l.book_id = t.book_id
)
select book_id, title, author, genre, publication_year, cnt as current_borrowers
from temp1
where total_copies = cnt
order by cnt desc, title asc
