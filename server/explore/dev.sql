drop table public.data_chunks;
drop table public.data_documents;

truncate table public.data_chunks;
truncate table public.data_documents;

SELECT * FROM public.data_chunks;
SELECT * FROM public.data_documents;

-- tables
truncate table projects_feed;
create table projects_feed (
    feed_id serial primary key,
	feed_url varchar(255),
	feed_title text,
	feed_description text,
	feed_time timestamp, 
	feed_content text
);

select * from projects_feed;