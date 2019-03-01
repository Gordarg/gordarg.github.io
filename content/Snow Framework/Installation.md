# Manual Installation:

1. Install IIS, Apache, nginx, Zend Server, WildFly, appserver.io, or etc ...

        Notes:
        Enable short tags on server
        Enable mysqli extension
        Enable Engine using following syntax:
            $ sudo a2enmod rewrite
            $ sudo systemctl restart apache2

1. Install MySQL DBMS
1. Clone project to web server's root directory

        Notes:
        Allow read+execute

1. Create database
1. Generate schema

        Script files:
        database/KMS.sql
        database/Logs.sql

1. Config Framework

        Store Database details, languages, Brand and SEO Details in `/Config.php`
        BASEURL: HTTP(S) internet address which is accessable by browser and agents

1. Config web-client

        Store baseurl in /public/js/Hi.js

1. Create default user

        INSERT INTO `users` (Username, HashPassword, Role)
                VALUES ('admin','fdcfc214459c57ab954b9a8ebde4a96ad761411d94e2fb8a414c0d25d38d2de3c831ce12eff572177b038bb610e301bb924dfc90833804a4409cd0c0e594d70e', 'ADMIN'
                )

        And use following
        Username: admin
        HashPassword: 123
        for dashboard login