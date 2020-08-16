#!/bin/bash

echo 'Input DB password'
read pass
shopt -s nullglob
for i in *.sql; do
    sqlcmd -S svc.pablintino.com,4490 -d altium_db -U librarian_rw -P $pass -i $i
done
