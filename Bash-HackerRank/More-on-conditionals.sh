function triangleTagger {
    side1=$1
    side2=$2
    side3=$3
    [[ $side1 == $side2 || $side1 == $side3 || $side2 == $side3 ]] && isEquilateral $side1 $side2 $side3 || echo "SCALENE"
}

function isEquilateral {
    [[ $1 == $2 && $1 == $3 ]] && echo "EQUILATERAL" || echo "ISOSCELES"
}

read side1
read side2
read side3

triangleTagger $side1 $side2 $side3
