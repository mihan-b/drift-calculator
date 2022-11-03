import math
def drift(range, time, wind_speed, wind_direction):
    #change to actual val for rocket
    surface_area=1
    mass=20
    avg_alt=(range[0]+range[1])/2
    density=get_density(avg_alt)
    #0.67 is approx drag
    force=density*surface_area*(wind_speed**2)*0.67
    #a=f/m
    acceleration=force/mass
    #d=1/2at^2
    displacement = 1/2*acceleration*(time**2)
    drift = [displacement, wind_direction]
    return drift

def get_density(alt):
    #feet to km
    alt_km=alt*0.000305
    #approximation of density as a function of altitude
    density=(-(alt_km-44.3308)/42.2665)**(7418/1743)
    return density

def to_vector(drift):
    magnitude=drift[0]
    direction_deg=drift[1]
    #deg to rad
    direction_rad=direction_deg*0.01745329251
    north=magnitude*math.cos(direction_rad)
    east=magnitude*math.sin(direction_rad)
    return([north, east])

def sum_drift(vectors):
    north_list=[]
    east_list=[]
    for i in vectors:
        north_list.append(i[0])
        east_list.append(i[1])
    north_sum=sum(north_list)
    east_sum=sum(east_list)
    return[north_sum, east_sum]

def distance_calc(total_drift):
    distance=math.sqrt(((total_drift[0])**2)+((total_drift[1])**2))
    heading_rad=math.atan((total_drift[0])/(total_drift[1]))
    heading_deg=90-heading_rad*57.2958
    return[distance, heading_deg]

def main():
    num_alts=input("Enter number of ranges: ")
    num_alts=int(num_alts)
    size_of_ranges=10000/num_alts

    ranges=[]
    count = 0
    while count<num_alts:
        lower_lim=count*size_of_ranges
        upper_lim=(count+1)*size_of_ranges
        ranges.append([lower_lim, upper_lim])
        count+=1

    drifts=[]
    for i in ranges:
        print("Enter the time spent in the range (seconds)", i)
        time=input()
        time=int(time)
        print("Enter the wind speed in the range (kts)", i)
        speed_kts=input()
        speed_kts=int(speed_kts)
        #knots to m/s
        speed=speed_kts/1.94384
        print("Enter the wind direction in the range (deg)", i)
        dir=input()
        dir=int(dir)
        drifts.append(drift(i, time, speed, dir))

    vectors=[]
    for i in drifts:
        vectors.append(to_vector(i))

    total_drift=sum_drift(vectors)
    total_distance=distance_calc(total_drift)

    print("Drift Estimates")
    print("----------------")
    print("Total drift north:", "\t", round(total_drift[0],5), "m")
    print("Total drift east: ", "\t", round(total_drift[1],5), "m")
    print("Total distance: ", "\t", round(total_distance[0],5), "m")
    print("Direction/Heading: ", "\t", round(total_distance[1],5), "\N{DEGREE SIGN}")

main()