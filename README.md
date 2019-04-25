foreman-server
=========

foreman/katello installer

These repos are disabled by so accidental updates to foreman do not happen during system updates.

```
foreman-plugins
foreman-rails
foreman
puppetlabs-pc1
```

Role Variables
--------------

```
foreman_admin_password (required)
foreman_admin_username: default(admin)
foreman_org_name: (required)
katello_version: default(latest)
foreman_version: default(latest)
```

Dependencies
------------

A list of other roles hosted on Galaxy should go here, plus any details in
regards to parameters that may need to be set for other roles, or variables that
are used from other roles.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables
passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: foreman-server, x: 42 }

License
-------

GPLv3

Author Information
------------------

Philip Bove (phil@bove.online)
