-- create database and user and give connect privilege
create database alphanode;
create user alphanode with password 'test';
grant connect on database alphanode to alphanode;

-- grant all privileges on existing objects in the public schema to the user
grant all privileges on schema public to alphanode;
grant all privileges on all tables in schema public to alphanode;
grant all privileges on all sequences in schema public to alphanode;
grant all privileges on all functions in schema public to alphanode;

-- set default privileges for future tables in public schema
alter default privileges in schema public grant all privileges on tables to alphanode;
alter default privileges in schema public grant all privileges on sequences TO alphanode;
alter default privileges in schema public grant all privileges on functions TO alphanode;

-- enable pgvector
create extension vector;