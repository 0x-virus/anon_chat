[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
## Anonymous Chat
This is an implementation of anonymous chat using the Flask framework and websocket technology. In this chat, you do not have a name, only the date and text of the message.
## Installation

```bash
  git clone https://github.com/0x-virus/anon_chat
  pip3 install -r requirements.txt
```

## Configuration
After installation, you need to change the configuration. To do this, just edit the config.py file

|Attribute     |Description                      |
|--------------|---------------------------------|
|MYSQL_USER    |database username                |
|MYSQL_PASSWORD|database password                |
|MYSQL_DB      |database name                    |
|MYSQL_TABLE   |name of the table in the database|
|MYSQL_HOST    |database ip address              |
|MYSQL_PORT    |database port                    |

Important! The database with the name specified in MYSQL_DB must be created manually. The table is created automatically