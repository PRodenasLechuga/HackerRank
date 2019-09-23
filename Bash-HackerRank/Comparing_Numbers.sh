function compare_numbers {
    if [[ $1 -gt $2 ]]
    then
        echo "X is greater than Y"
    fi

    if [[ $1 -eq $2 ]]
    then
        echo "X is equal to Y"
    fi

    if [[ $1 -lt $2 ]]
    then
        echo "X is less than Y"
    fi
}



read int1 
read int2

compare_numbers $int1 $int2