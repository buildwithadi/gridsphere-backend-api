import pyeto
import numpy as np

"""
Calculating Reference Evapotranspiration using the following data:
# day_of_year                   :   unitless
# latitude                      :   degree
# dl_hours (daylight hours)     :   hours
# sunshine_hours                :   hours
# albedo                        :   unitless
# tmin (minimum temperature)    :   Celcius
# tmax (maximum temperature)    :   Celcius
# altitude                      :   meters
# tavg (average temperature)    :   Celcius
# ws (wind speed)               :   meter per seconds  
"""


# net_rad : Net radiation at crop surface [MJ m-2 day-1]
def net_rad_calculator(day_of_year, latitude, dl_hours, sunshine_hours, albedo, tmin, tmax, altitude):  

    # Conveting the values:
    latitude = np.deg2rad(latitude)     # Radian
    tmin = tmin + 273.5                 # Kelvin
    tmax = tmax + 273.5                 # Kelvin


    # Extraterrestrial Radiation
    sol_dec = pyeto.sol_dec(day_of_year)
    sha = pyeto.sunset_hour_angle(latitude, sol_dec)
    ird = pyeto.inv_rel_dist_earth_sun(day_of_year)
    et_rad = pyeto.et_rad(latitude, sol_dec, sha, ird)                          # Extraterrestrial Radiation
    sol_rad = pyeto.sol_rad_from_sun_hours(dl_hours, sunshine_hours, et_rad)    # Gross incoming solar radiation  
    ni_sw_rad = pyeto.net_in_sol_rad(sol_rad, albedo)                           # Net incoming shortwave radiation


    # Net outgoing longwave radiation
    cs_rad = pyeto.cs_rad(altitude, et_rad)                                     # clear sky radiation [MJ m-2 day-1]
    avp = pyeto.avp_from_tmin(tmin - 273.5)                                     # Actual vapour pressure [kPa].
    no_lw_rad = pyeto.net_out_lw_rad(tmin, tmax, sol_rad, cs_rad, avp)

    return pyeto.net_rad(ni_sw_rad, no_lw_rad)



def ref_evt(net_rad,tavg,ws,tmin,altitude): 

    # Conveting the values:
    tmin = tmin + 273.5                 # Kelvin
    tavg = tavg + 273.5                 # Kelvin

    svp = pyeto.svp_from_t(tavg - 273.5)                                        # Saturation vapour pressure [kPa]
    avp = pyeto.avp_from_tmin(tmin - 273.5)                                     # Actual vapour pressure [kPa].
    delta_svp = pyeto.delta_svp(tavg - 273.5)                                   # Slope of saturation vapour pressure curve [kPa degC-1].
    psy = pyeto.psy_const(pyeto.atm_pressure(altitude))                         # Psychrometric constant [kPa deg C]

    ET = pyeto.fao56_penman_monteith(net_rad, tavg, ws, svp, avp, delta_svp, psy)

    return ET
