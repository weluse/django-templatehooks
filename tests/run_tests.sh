#!/bin/bash -ex

python manage.py test --settings settings base
python manage.py test --settings settings_example example
