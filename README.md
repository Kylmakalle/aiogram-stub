> Repository Archived. Take a look at
> - https://github.com/Forden/aiogram-bot-template
> - https://github.com/Latand/tgbot_template
> - https://github.com/Tishka17/tgbot_template

# Aiogram cookiecutter

Template for creating flexible [aiogram](https://github.com/aiogram) bots fast

Supports **MongoDB**, **Mixpanel** and **Sentry** _out of the box_

## Installation

```bash
pip install cookiecutter
cookiecutter https://github.com/Kylmakalle/aiogram-stub.git
```


Edit `production.env`

Install Docker & docker-compose

```bash
cd mybot
docker-compose up --build

# For background start
docker-compose up --build -d

```


`.gitignore` contains some exceptions for `private` data

```
private/*
private_modules/*
private-requirements.txt
```

## Fast restart
No container rebuild required
```bash
cd mybot
docker-compose restart bot
```

## Translations

Take a look at official [example](https://github.com/aiogram/aiogram/blob/dev-2.x/examples/i18n_example.py)

Use `./update_locales.sh` to make changes on your `.po` files fast!

Check `core/localisation.py` for more info and tweaks
