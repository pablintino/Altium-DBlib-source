#!/bin/bash

echo 'Input DB password'
read pass
shopt -s nullglob
for i in *.sql; do
    sqlcmd -S 127.0.0.1,1433 -d altium_db -U librarian_rw -P $pass -i $i
done
