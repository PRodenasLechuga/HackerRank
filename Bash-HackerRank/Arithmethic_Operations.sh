function do_the_operations {
    echo $(($1+$2))
    echo $(($1-$2))
    echo $(($1*$2))
    echo $(($1/$2))
}

read int1 
read int2

do_the_operations $int1 $int2
