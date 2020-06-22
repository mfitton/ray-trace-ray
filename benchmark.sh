# echo "Timing execution for 1600 x 1200"
# for i in {0..4}
# do
# { time WIDTH=1600 HEIGHT=1200 python raytracing-ray.py; } &> "1600x1200-ray-benchmark-$i.txt" 
# { time WIDTH=1600 HEIGHT=1200 python raytracing.py; } &> "1600x1200-benchmark-$i.txt" 
# done


echo "Timing execution for 1200 x 900"
for i in {0..4}
do
{ time WIDTH=1200 HEIGHT=900 python raytracing-ray.py; } &> "1200x900-ray-benchmark-$i.txt"
{ time WIDTH=1200 HEIGHT=900 python raytracing.py; } &> "1200x900-benchmark-$i.txt"
done


echo "Timing execution for 600 x 450"
for i in {0..4}
do
{ time WIDTH=600 HEIGHT=450 python raytracing-ray.py; } &> "600x450-ray-benchmark-$i.txt"
{ time WIDTH=600 HEIGHT=450 python raytracing.py; } &> "600x450-benchmark-$i.txt"
done
