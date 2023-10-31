-- sudo -u postgres psql -f init.sql

-- User accounts
create user watcher with password 'watcher';

-- Database
create database watcher;

-- DB permissions
grant all on database watcher to watcher;

-- Table permissions
\connect watcher
grant all on all tables in schema public to watcher;

SET TIMEZONE='UTC';
