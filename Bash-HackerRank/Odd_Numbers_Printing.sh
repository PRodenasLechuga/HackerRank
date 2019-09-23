#!/bin/bash

function is_odd {
  [ $(($1 % 2)) == 1 ] && echo $i
}

for i in {1..99}
do
    is_odd $i
done