Philippine Provinces and Cities
===============================

[https://github.com/ojtibi/philippine-provinces-and-cities-sql](https://github.com/ojtibi/philippine-provinces-and-cities-sql)

[OJ Tibi](https://github.com/ojtibi)

This is a very basic SQL script containing the complete list of Philippine provinces and each city/municipality underneath. Extremely useful for Filipino developers who are looking for ready-baked data for their projects.

Short History
-------------

I haven't really found a readily-available script from the Internet to get this list from, so I created this list with references from [Wikipedia](http://en.wikipedia.org/wiki/List_of_cities_and_municipalities_in_the_Philippines).

Technical Details
-----------------

* Generated from **MySQL 5.1.57 ISAM tables**
* Default length for province/city names is **`varchar(300)`**
* Primary/foreign keys are **`unsigned int(11)`**
* Tables collated with **utf8\_unicode\_ci**
* Used **PHPMyAdmin 3.5.0** with **ANSI** compatibility for the SQL output

Usage
-----

**Vanilla Mode**

Just call the `philippine_provinces_and_cities.sql` from your favorite CLI client, or import it using a database administration GUI of your choice. :)

**Python Generator**

If you're using different table names and/or columns, use the quick Python generator:

* Make sure you have the **cmd2** Python module by running `sudo easy_install cmd2`
* Download the files from the master branch, or just clone it using `git clone https://github.com/ojtibi/philippine-provinces-and-cities-sql.git <targetdir>`
* `cd` into your `<targetdir>`, and run `python ppc.py`. Use `table` to enter the values you need for your table names and/or columns, and use `spit` to generate, `quit` to exit
* Use the generated `ppc.sql`. :)

Credits
-------

* Marconi Moreto ([https://github.com/marconi](https://github.com/marconi)) for providing the Python generator and dynamic template mappings


Changelog
---------

**0.2**

* Removed timestamps from vanilla script and templates.

**0.1**

* Initial version, contains tables for Philippine Cities and Provinces
* Fixed unicode issues for city values (ñ)
* Pulled and merged Python generator script for custom table and field names, fixed misspelled template placeholders