import pyeto
import numpy as np

# Crop Evapotranspiration:

lux = 25000                     # radiation [lux]

t = 29.5                        # air temperature [deg C]
ws = 7.56                       # wind speed [km h-1]
elevation = 1800                # elevation [m]
altitude = 1800                 # height from sea level [m]
day_of_year = 240               # day of the year
latitude = np.deg2rad(48)       # in radians 
dl_hours = 12.9                 # day light hours in hours
sunshine_hours = 5.5            # sunshine hours in hours
albedo = 0.23                   # albedo
tmin = 26                       # min temperature
tmax = 33                       # max temperature

def net_rad_calculator(day_of_year, latitude, dl_hours, sunshine_hours, albedo, tmin, tmax, t):

    # Extraterrestrial Radiation
    sol_dec = pyeto.sol_dec(day_of_year)
    sha = pyeto.sunset_hour_angle(latitude, sol_dec)
    ird = pyeto.inv_rel_dist_earth_sun(day_of_year)
    et_rad = pyeto.et_rad(latitude, sol_dec, sha, ird)  # Extraterrestrial Radiation
    sol_rad = pyeto.sol_rad_from_sun_hours(dl_hours, sunshine_hours, et_rad)    # Gross incoming solar radiation  
    ni_sw_rad = pyeto.net_in_sol_rad(sol_rad, albedo)   # Net incoming shortwave radiation


    # Net outgoing longwave radiation
    cs_rad = pyeto.cs_rad(altitude, et_rad)             # clear sky radiation [MJ m-2 day-1]
    avp = pyeto.avp_from_tmin(tmin)  
    no_lw_rad = pyeto.net_out_lw_rad(tmin + 273.5, tmax + 273.5, sol_rad, cs_rad, avp)

    return pyeto.net_rad(ni_sw_rad, no_lw_rad)


net_rad = net_rad_calculator(day_of_year, latitude, dl_hours, sunshine_hours, albedo, tmin, tmax,t)   
# net_rad : Net radiation at crop surface [MJ m-2 day-1]
t = t + 273.5                                           # Air temperature at 2 m height [deg Kelvin]
ws = ws / 3.6                                           # Wind speed at 2 m height [m s-1]
svp = pyeto.svp_from_t(t - 273.5)                       # Saturation vapour pressure [kPa]
avp = pyeto.avp_from_tmin(tmin)                         # Actual vapour pressure [kPa].
delta_svp = pyeto.delta_svp(t - 273.5)                  # Slope of saturation vapour pressure curve [kPa degC-1].
psy = pyeto.psy_const(pyeto.atm_pressure(elevation))    # Psychrometric constant [kPa deg C]

ET = pyeto.fao56_penman_monteith(net_rad, t, ws, svp, avp, delta_svp, psy)

# Crop Reference Evapotranspiration (ETo)
print(f"Reference Evapotranspiration (ETo): {ET:.2f} mm/day")

# Crop Evapotranspiration (ETc)

Kc = 1.0 # Crop coefficient
ETc = Kc * ET
print(f"Crop Evapotranspiration (ETc) with Kc={Kc}: {ETc:.2f} mm/day")