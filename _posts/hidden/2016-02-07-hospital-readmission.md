---
layout: post
title: Hospital Readmission Description
author:
category: hidden
tags: 
comments: true
use_math: true

---

**Table of Contents**

<hr style="height:2px; background-color:#b6b6b6"/>

* TOC
{:toc}

<hr style="height:2px; background-color:#b6b6b6"/>

# Creating a Database

Setting up the server

after installing postgresql run

service postgresql start
sudo su - postgres
psql
select * from pg_shadow

gives us:

postgres=# select * from pg_shadow;

 usename  | usesysid | usecreatedb | usesuper | usecatupd | userepl | passwd | v
aluntil | useconfig 
----------+----------+-------------+----------+-----------+---------+--------+--
--------+-----------
 postgres |       10 | t           | t        | t         | t       |        |  
        | 
 ezbc     |    16384 | f           | f        | f         | f       |        |  
        | 
(2 rows)

change permissions for ezbc:

ALTER USER ezbc CREATEDB SUPERUSER;



Create a database with

initdb -D data

Then run psql

psql postgres

Then allow the postgresql lock file to be written in /var/run with

sudo chmod a+w /var/run/postgresql

Start the database server with

postgres -D data


From here follow
[these](http://wiki.wsmoak.net/cgi-bin/wiki.pl?action=browse&diff=1&id=PhoenixPostgres)
instructions for how to change database permissions for your user.

Then run the phoenix server:

mix phoenix.server









