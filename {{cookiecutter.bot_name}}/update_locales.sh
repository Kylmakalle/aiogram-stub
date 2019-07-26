#!/usr/bin/env bash
pybabel extract modules/ private/ private_modules/ -o locales/{{cookiecutter.bot_name}}.pot -k __:1,2 --project={{cookiecutter.bot_name}} --version=0.1 --no-location --add-comments=NOTE
pybabel update -d locales -i locales/{{cookiecutter.bot_name}}.pot
