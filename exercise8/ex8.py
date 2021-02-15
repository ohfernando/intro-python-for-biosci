#script in part from https://stackoverflow.com/questions/51212158/how-to-find-angle-between-gps-coordinates-in-pandas-dataframe-python?answertab=votes#tab-top

import sys
import numpy as np

#360


a=open(sys.argv[1],'r')
count=0
listofcoordinates=[]
individualcoordinate=[]
for line in a:
    n=line.split()
    if count==0:
        for coord in n:
            individualcoordinate.append(float(coord))
    else:
        templist=[]
        for coord in n:
            templist.append(float(coord))
        listofcoordinates.append(templist)
    count=count+1



#individualcoordinate=[28.08025,154.24466]
#listofcoordinates=[[48.12035,154.24366],[25.29035,104.24466],[27.08125,157.24466],[20.08455,163.24461]]

def vector_calc(lat, long, ht,xfixed,yfixed,zfixed=0):
    '''
    Calculates the vector from a specified point on the Earth's surface to a fixed locus.
    '''
    a = 6378137.0  # Equatorial radius of the Earth
    b = 6356752.314245  # Polar radius of the Earth

    e_squared = 1 - ((b ** 2) / (a ** 2))  # e is the eccentricity of the Earth
    n_phi = a / (np.sqrt(1 - (e_squared * (np.sin(lat) ** 2))))

    x = (n_phi + ht) * np.cos(lat) * np.cos(long)
    y = (n_phi + ht) * np.cos(lat) * np.sin(long)
    z = ((((b ** 2) / (a ** 2)) * n_phi) + ht) * np.sin(lat)


    v = ((xfixed - x), (yfixed - y), (zfixed - z))

    return v

def angle_calc(lat1, long1, lat2, long2, xfixed,yfixed, ht1=0, ht2=0):
    '''
    Calculates the angle between the vectors from 2 points to a fixed locus.
    '''
    # Convert from degrees to radians
    lat1_rad = (lat1 / 180) * np.pi
    long1_rad = (long1 / 180) * np.pi
    lat2_rad = (lat2 / 180) * np.pi
    long2_rad = (long2 / 180) * np.pi

    v1 = vector_calc(lat1_rad, long1_rad, ht1,xfixed,yfixed)
    v2 = vector_calc(lat2_rad, long2_rad, ht2,xfixed,yfixed)

    # The angle between two vectors, vect1 and vect2 is given by:
    # arccos[vect1.vect2 / |vect1||vect2|]
    dot = np.dot(v1, v2)  # The dot product of the two vectors
    v1_mag = np.linalg.norm(v1)  # The magnitude of the vector v1
    v2_mag = np.linalg.norm(v2)  # The magnitude of the vector v2

    theta_rad = np.arccos(dot / (v1_mag * v2_mag))
    # Convert radians back to degrees
    theta = (theta_rad / np.pi) * 180

    return theta

xfixed=individualcoordinate[0]
yfixed=individualcoordinate[1]
anglelist=[]


for coordinates in listofcoordinates:
    x1=coordinates[0]
    y1=coordinates[1]
    try:
        index=listofcoordinates.index(coordinates)
        newcoordinates=listofcoordinates[index+1]
        x2=newcoordinates[0]
        y2=newcoordinates[0]
    except IndexError:
        x2=listofcoordinates[0][0]
        y2=listofcoordinates[0][1]
    anglelist.append(angle_calc(x1,y1,x2,y2,xfixed,yfixed))


anglecount=0
for item in anglelist:
    anglecount=anglecount+item

if anglecount>=360:
    print('the point is likely inside area')
else:
    print('the point is likely outside area')
    
    
#angles add up to 360 if inside coordinatrs
#else probably less than that




