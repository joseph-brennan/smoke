==================
Smoke Architecture
==================


Purpose
-------

Smoke is a web application which will allow teachers and
students to create environments to learn any programming
language, all without the hassle of having to download and
install any software; free of any system dependencies, to be
fully OS agnostic.

Smoke will facilitate the learning of languages,
test driven development, and coding by being more accessible;
all of these, done thorough a web browser with an internet connection.

Architecture Model
------------------

MVC 
------------------
The Model-View-Controller(MVC) is an architectural pattern which how to design a program structure.
It contains three main logical components: the model, the view, and the controller. These three 
components are closely related, but they are independent of each other. The changes inside each 
component do not affect other components. Each component provides an interface to the outer 
component for calling. In this way, the software can be modularized, and the modification of 
the appearance or the change of data does not require modification of other components, 
which greatly facilitates maintenance and upgrade.

-Model
 It is the data or information that the program needs to operate.
-View
 It faces the final user directly and it is the user interface that is provided to the user.
-Controller
 It is responsible for selecting the data in the "model" according to the instructions entered 
 by the user from the "view", and then performing corresponding operations to produce the final result.
 


Controller - Flask
------------------

Flask is used as the controller for the MVC architecture, bridging the gap
between what the user sees and what is happening behind the scenes.  It is a
micro-framework designed to do only what it needs to do, and do it well.
Flask provides many tools to keep the backend clean and concise through both built in extensions
and community made extensions.

- Flask-SQLAlchemy [fsqla]_

    Flask provides direct access to the database (SQLAlchemy)

    * Has built-in support with "useful defaults and extra helpers" to quicken and simplify database management

- Flask-Migrate [fmig]_

    Flask-Migrate allows a migration repository for the database (SQLAlchemy), or multiple databases, through the
    use of the Flask and Flask-Script command-line interface

- Flask-Marshmallow [fmar]_

    Flask-marshmallow allows integration between the Flask app and marshmallow,
    a library used for converting complex datatypes into Python datatypes and vice versa

- Flask-CORS [fcors]_

    Cross Origin Resource Sharing that allows Cross Origin AJAX_ (Asynchronous JavaScript
    and XML)



    * Allows web apps to send and retrieve data without changing the user's view of the page

- Flask-JWT_
    .. _Flask-JWT: https://flask-jwt-extended.readthedocs.io/en/latest/

    JSON Web Tokens authenticate the user and are managed through the Flask-JWT-Extended
    library




Model - ORM - SQLAlchemy
-------------------------

model - **add info**




View
-----

front-end - **add info**


Clic()
------

 click **add info**


Resources
---------

If you wish to learn more about the technologies used to make **smoke**
possible, visit these links:

* Flask_

.. _Flask: http://flask.pocoo.org/

* SQLAlchemy_

.. _SQLAlchemy: https://www.sqlalchemy.org/library.html

* Sphinx-doc_

.. _Sphinx-doc: http://www.sphinx-doc.org/en/master/

* PEP257_

.. _PEP257: https://www.python.org/dev/peps/pep-0257/



RST Syntax Examples
===================

You can use ``backticks`` for showing ``highlighted`` code

one asterisk: *text* for emphasis (italics),
two asterisks: **text** for strong emphasis (boldface), and


Structural Elements
===================

Section Title
-------------








A bullet list

  + Nested bullet list.
  + Nested item 2.

- Item 2.

  Paragraph 2 of item 2.

  * Nested bullet list.
  * Nested item 2.

    - Third level.
    - Item 2.

  * Nested item 3.

Enumerated Lists
----------------

1. Arabic numerals.

   a) lower alpha)

      (i) (lower roman)

          A. upper alpha.

             I) upper roman)

2. Lists that don't start at 1:

   3. Three

   4. Four

   C. C

   D. D

   iii. iii

   iv. iv

Literal Blocks
--------------

Literal blocks are indicated with a double-colon ("::") at the end of
the preceding paragraph (over there ``-->``).  They can be indented::

    if literal_block:
        text = 'is left as-is'
        spaces_and_linebreaks = 'are preserved'
        markup_processing = None

Or they can be quoted without indentation::

>> Great idea!
>
> Why didn't I think of that?


Block Quotes
------------

Block quotes consist of indented body elements:

    My theory by A. Elk.  Brackets Miss, brackets.  This theory goes
    as follows and begins now.  All brontosauruses are thin at one
    end, much much thicker in the middle and then thin again at the
    far end.  That is my theory, it is mine, and belongs to me and I
    own it, and what it is too.

    -- Anne Elk (Miss)

Doctest Blocks
--------------

>>> print 'Python-specific usage examples; begun with ">>>"'
Python-specific usage examples; begun with ">>>"
>>> print '(cut and pasted from interactive Python sessions)'
(cut and pasted from interactive Python sessions)
