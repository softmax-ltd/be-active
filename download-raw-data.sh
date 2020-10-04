source config.sh

python /app/garmin-connect-export/gcexport.py \
	--username $GARMIN_USERNAME \
	--password  $GARMIN_PASSWORD \
	-c $N_ACTIVITIES \
	-d raw-data \
	-f original 

for filename in ./raw-data/*.zip; do
	unzip -o $filename -d raw-data 
done

python convert.py raw-data/