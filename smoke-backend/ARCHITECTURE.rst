##################
Smoke Architecture
##################

Purpose
=======

Smoke allows teachers to create learning environments for students to learn
any programming language.

With a test driven development, Smoke allows teachers to define a set of
**answers** and allows a student to design the **solutions** *in any language*.
To prevent language dependencies, Smoke first wraps the input language in a
custom Python wrapper. To test the validity of the input code's solutions and
the predefined, valid answers, Smoke performs equality based unit testing.

Designed to operate through a web interface, Smoke avoids any system, api, or
language dependencies. Further, Smoke is easily modifiable due to the
containerization implementation provided by Docker.


Architecture Model - MVC
========================

MVC 
---

.. image:: https://upload.wikimedia.org/wikipedia/commons/a/a0/MVC-Process.svg

The Model-View-Controller([MVC]_) is an architectural pattern. It contains
three main logical components are the model, the view, and the controller.
These three components are closely related, but still independent of each
other. Each component provides an interface to the outer component for
calling. In this way, the software can be modularized, and the modification of
any component does not effect the state of the others. This greatly
facilitates maintenance and upgrade.

:Model: The data the program needs to operate.
:View: The user interface that is provided to the user, different for separate
    platforms.
:Controller: Responsible for selecting data in the model according to the
    instructions entered by the user from the view. Performs corresponding
    operations to produce the final result.


Controller - Flask
------------------

Flask is used as the controller for the MVC architecture, bridging the gap
between what the user sees and what is happening behind the scenes. [f]_  It
is a micro-framework designed to do only what it needs to do, and do it well.
Flask provides many tools to keep the backend clean and concise through both
built in extensions and community made extensions.

- Flask-SQLAlchemy [fsqla]_

    Provides direct access to the SQL database through SQLAlchemy.

    * Has built-in support with "useful defaults and extra helpers" to quicken
      and simplify database management.

- Flask-Migrate [fmig]_

    Provides migration through databases with different or
    modified schemas. [fsqlaschema]_

- Flask-Marshmallow [fmar]_

    Provides serialization and persistence of Smoke's objects for quick
    communication with the SQL database.

- Flask-CORS [fcors]_

    Provides AJAX Cross Origin Resource Sharing. [ajax]_

    * Allows web apps to send and retrieve data without changing the user's
      view of the page

- Flask-JWT [fjwt]_

    Provides JSON Web Tokens authenticate the user and control access to the
    backend.

Model - ORM - SQLAlchemy
------------------------

SQLAlchemy is an object-relational mapping (ORM) tool. Facilities
communication between Python programs and databases. Translates Python classes
into entries for SQL's relational databases. Automatically converts function
calls to SQL statements. This allows programmers to write ORM programs instead
of SQL statements.


View - ViewJS
-------------

VueJS is an 'approachable, versatile,' and efficient framework for building
user web interfaces. [vue]_ Allows the programmer to build different
components on a web single page, makes it easier to maintain, and easier to
test.

- Vue.js-Components [vuecomponents]_

    Allows Smoker to have all the different components such as the editor,
    console, comments area, and testing screen separate.

- Vue.js-Testing [vuetesting]_

    Unit testing framework for vue objects.

- Vue.js-Responsiveness [vueresponsiveness]_

    Responsive framework to enable display modification without a web page
    refresh.