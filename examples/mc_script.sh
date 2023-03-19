num=$1
while [ $num -ge 0 ]
do
  echo "Sim Number: ${num}" >> output 
  ((num--))
  python monte_carlo.py >> output 
done

