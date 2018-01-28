---
author: Elijah Bernstein-Cooper
category:
- personal
- hidden
comments: true
date: 2016-02-07 00:00
hidden: true
layout: post
redirect_from: /hidden/2016/02/07/hospital-readmission
tags: null
title: Hospital Readmission Description
use_math: true
---

**Table of Contents**

<hr style="height:2px; background-color:#b6b6b6"/>

* TOC
{:toc}

<hr style="height:2px; background-color:#b6b6b6"/>

# Creating a Database

The local page will be at
http://localhost:4000/hidden/2016/02/07/hospital-readmission

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


# Create the database

Create ecto user in postgres

~~~ bash
createuser ecto --pwprompt
~~~

Create the database

~~~ bash
createdb -Oecto -Eutf8 test_DB
~~~

Make sure you can login to your postgres database by running the following
command:

~~~ bash
psql test_DB --user ecto --password
~~~


~~~ bash
mix phoenix.gen.html UserTest usertest name:string email:string bio:string number_of_pets:integer
~~~


# Migrating the data

Loading CSV into database as a table.


# database links
http://www.phoenixframework.org/v0.13.1/docs/ecto-models

http://www.phoenixframework.org/docs/mix-tasks



# Drop a database

~~~
psql postgres

DROP DATABASE hospital_readmission_server_dev;
~~~

Remove schema from `priv/repo/migrations/`

# Create DB

~~~
mix ecto.create
~~~

Runs any pending migrations. Migrations are table structure changes called
"schema". Database has list of all previous schemas. When migrating Phoenix
checks if previous migrations have been performed.

~~~
mix ecto.migrate
~~~

Create a new migration.

~~~
mix ecto.gen.migration add_hospitals_table
~~~

Created file `priv/repo/migrations/20160306220657_add_hospitals_table.exs`

Now specify the columns in our new table, `hospitals_table`. Lets add just a
few columns of different data types to get the idea.

~~~
defmodule HospitalReadmissionServer.Repo.Migrations.AddHospitalsTable do
  use Ecto.Migration

  def change do
    create table(:hospitals) do
      add :hospital_name, :string
      add :provider_number, :integer
      add :start_date, :datetime
      add :end_date, :datetime
      timestamps
    end
  end
end
~~~

Changing schema in `hospitals_table` by running

~~~
mix ecto.migrate
~~~

To view the table changes

~~~
psql hospital_readmissions_server_dev
~~~

`\d` will display the tables in the database. `\d hospitals` will display the
hospitals table columns:

~~~
     Column      |            Type             |                       Modifiers
                        
-----------------+-----------------------------+--------------------------------
------------------------
 id              | integer                     | not null default nextval('hospi
tals_id_seq'::regclass)
 hospital_name   | character varying(255)      | 
 provider_number | integer                     | 
 start_date      | date                        | 
 end_date        | date                        | 
 inserted_at     | timestamp without time zone | not null
 updated_at      | timestamp without time zone | not null
~~~

Phoenix creates the hospitals_id_seq table automatically. Running `\d
hospitals_id_seq` gives us

~~~
      Sequence "public.hospitals_id_seq"
    Column     |  Type   |        Value        
---------------+---------+---------------------
 sequence_name | name    | hospitals_id_seq
 last_value    | bigint  | 1
 start_value   | bigint  | 1
 increment_by  | bigint  | 1
 max_value     | bigint  | 9223372036854775807
 min_value     | bigint  | 1
 cache_value   | bigint  | 1
 log_cnt       | bigint  | 0
 is_cycled     | boolean | f
 is_called     | boolean | f
Owned by: public.hospitals.id
~~~

which maps changes to the `hospitals` table.

## Copying the table

Create a migration to copy csv data to hospitals database table.

~~~
mix ecto.gen.migration populate_hospitals
* creating priv/repo/migrations
* creating priv/repo/migrations/20160306223423_populate_hospitals.exs
~~~

Now we will generate a psql script for ecto to run which will copy the csv. Ecto
needs to know the location of the csv file. Define the data location with

~~~
  def change do
    abs_path = Path.absname 'priv/repo/data_files/Hospital_Readmissions_Reduction_Program.csv'
    IO.puts abs_path
    execute """
      copy hospitals(
        hospital_name,
        provider_number,
        start_date,
        end_date) 
        FROM '#{abs_path}' 
        WITH csv header;
    """
~~~

in `priv/repo/migrations/20160306223423_populate_hospitals.exs`

~~~
psql hospital_readmission_server_dev
~~~

Perform the migration:

~~~
mix ecto.migrate
~~~

Now to get the page up and running adjust the schema for the hospitals table in
`web/models/hospital.ex`

~~~
defmodule HospitalReadmissionServer.Hospital do
  use HospitalReadmissionServer.Web, :model

  schema "hospitals" do
    field :hospital_name, :string
    field :provider_number, :integer
    field :start_date, Ecto.DateTime
    field :end_date, Ecto.DateTime

    timestamps
  end

  @required_fields ~w(hospital_name)
  @optional_fields ~w(provider_number start_date end_date)

  @doc """
  Creates a changeset based on the `model` and `params`.

  If no params are provided, an invalid changeset is returned
  with no validation performed.
  """
  def changeset(model, params \\ :empty) do
    model
    |> cast(params, @required_fields, @optional_fields)
  end
end
~~~