#!/bin/bash

if [ ${PWD##*/} != 'tools' ] && [ ${PWD##*/} != 'software_challenge' ]
then
  # run script
  echo -e "\nERROR: Must run script from either 'software_challenge' project root or 'software_challenge/tools'\n"
  exit
elif [ ${PWD##*/} = 'tools' ]
then
  cd ..
fi

python -Wall manage.py test -v 2 2>&1 | tee tools/results.log
