import pyeto

# Crop Evapotranspiration:

lux = 25000       # radiation [lux]
t = 22.74        # air temperature [deg C]
ws = 2.88          # wind speed [km h-1]
elevation = 2000 # elevation [m]

net_rad = lux/1388.4    # net_rad : Net radiation at crop surface [MJ m-2 day-1]
t = t + 273.5           # Air temperature at 2 m height [deg Kelvin]
ws = ws * 0.27          # Wind speed at 2 m height [m s-1]
svp = pyeto.svp_from_t(t - 273.5)       # Saturation vapour pressure [kPa]
avp = pyeto.avp_from_tmin(t - 273.5)    # Actual vapour pressure [kPa].
delta_svp = pyeto.delta_svp(t - 273.5)  # Slope of saturation vapour pressure curve [kPa degC-1].
psy = pyeto.psy_const(pyeto.atm_pressure(elevation))    # Psychrometric constant [kPa deg C]

ET = pyeto.fao56_penman_monteith(net_rad, t, ws, svp, avp, delta_svp, psy)

print(ET)

K = 1.2

ETc = K * ET

print(ETc)