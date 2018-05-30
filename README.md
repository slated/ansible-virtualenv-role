Role Name
=========

Install virtualenv and virtualenvwrapper, configure env vars for
virtualenvwrapper, and make a Python virtualenv.

Requirements
------------

An installed python executable at the location of the `virtualenv_python` var.
Pip and python "-dev" packages will be needed almost always.
The _python_ role takes care of these.

Role Variables
--------------

Path to python for mkvirtualenv:

    virtualenv_python: /usr/bin/python3

Locate and configure WORKON_HOME and PROJECT_HOME at
~ansible_user/workon_dir and ~ansible_user/project_dir
(respectively). By default these are under $HOME of the
`ansible_user`.

    virtualenv_workon_dir: pyves
    virtualenv_project_dir: pyves

Create a project with mkvirtualenv using `virtualenv_python` if
(and only if) `virtualenv_project` var is set.

    virtualenv_project: myproject
    
Dependencies
------------

    rm-software.s-python

Example Playbook
----------------

    - hosts: servers
      - import_role:
          name: virtualenv
        vars:
          virtualenv_python: /usr/bin/python3.6
          virtualenv_project: myproject
        
