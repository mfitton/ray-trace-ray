for CHUNK_SIZE in 20 50 100 200 500 1000 2000 5000 10000
do
	echo "Timing execution for $CHUNK_SIZE"
	CHUNK_SIZE="$CHUNK_SIZE" time python raytracing.py
	echo "Done Timing execution for $CHUNK_SIZE"
	echo "\n"
done
