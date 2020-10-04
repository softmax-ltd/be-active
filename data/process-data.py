
import os
import glob
import math
import functools

import pandas as pd

from privacy import PRIVACY_ZONES


CWD = os.getcwd() 
MIN_ALLOWED_DISTANCE = 0.5  # [km]

def isnone(x):
    return x is None or str(x).lower() == 'none'


def distance_from_coords(origin, privacy_areas):
    if any([isnone(i) for i in origin]):
        return None
    else:
        lat1, lon1 = map(float, origin)
        distances = []
        for point in privacy_areas:
            lat2, lon2 = point
            radius = 6371 # km

            dlat = math.radians(lat2 - lat1)
            dlon = math.radians(lon2 - lon1)
            a = (math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
                * math.cos(math.radians(lat2)) * math.sin(dlon / 2) * math.sin(dlon / 2))
            c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
            distances.append(radius * c)
        
        return min(distances)

def remove_start_end_point_too_close(df):

    distance_from_protected_areas = functools.partial(
        distance_from_coords, 
        privacy_areas=PRIVACY_ZONES
    )     

    if 'Begin Latitude (°DD)' in df.columns:
        lat_long_columns_begin = ['Begin Latitude (°DD)', 'Begin Longitude (°DD)']
        mask_begin = df[lat_long_columns_begin].apply(distance_from_protected_areas, axis=1) < MIN_ALLOWED_DISTANCE
        df.loc[mask_begin, lat_long_columns_begin] = None

        lat_long_columns_end = ['End Latitude (°DD)', 'End Longitude (°DD)']
        mask_end = df[lat_long_columns_end].apply(distance_from_protected_areas, axis=1) < MIN_ALLOWED_DISTANCE
        df.loc[mask_end, lat_long_columns_end] = None
    
    elif 'position_lat' in df.columns:
        lat_long_columns = ['position_lat', 'position_long']
        mask = df[lat_long_columns].apply(distance_from_protected_areas, axis=1) < MIN_ALLOWED_DISTANCE
        df.loc[mask, lat_long_columns] = None

    return df

def main():

    raw_data = os.path.join(CWD, 'raw-data/')
    processed_data = os.path.join(CWD, 'processed-data/')

    if os.path.isfile(raw_data + 'activities.csv'):
        df = pd.read_csv(raw_data + 'activities.csv')
        df = remove_start_end_point_too_close(df)
        df.to_csv(processed_data + 'activities.csv', index=0)

    activities = glob.glob(raw_data + '*csv')

    for activity in activities:
        df = pd.read_csv(activity)
        try:
            df = remove_start_end_point_too_close(df)
            new_filename = activity.split('/')[-1]
            df.to_csv(processed_data + new_filename, index=0)
        except:
            print(activity)

if __name__=='__main__':

    main()
