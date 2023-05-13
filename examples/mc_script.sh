num=$1
while [ $num -gt 0 ]
do
  echo "Sim Number: ${num}" 
  ((num--))
  python monte_carlo.py  
done

