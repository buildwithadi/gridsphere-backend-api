# Import the necessary modules from FastAPI and uvicorn.
# uvicorn is a lightweight, high-performance ASGI server, which is what we'll use to run our FastAPI app.
import uvicorn

from fastapi import FastAPI
import ref_eva

# Create an instance of the FastAPI class.
# This is the main object that provides all the functionality for your API.
app = FastAPI()

# Define a GET endpoint for the reference evapotranspiration calculation.
# This endpoint takes multiple query parameters to perform the calculation.
@app.get("/ref_evapo")
def ref_evapo(day_of_year: float, latitude: float, dl_hours: float, sunshine_hours: float, albedo: float, tmin: float, tmax: float, tavg: float, altitude: float, ws: float):
    """
    This API endpoint calculates a reference evapotranspiration (ET) value.

    Args:
        day_of_year (float): The day of the year (1-365).
        latitude (float): Latitude in degrees.
        dl_hours (float): Daylight hours.
        sunshine_hours (float): Sunshine hours.
        albedo (float): Surface albedo.
        tmin (float): Minimum temperature.
        tmax (float): Maximum temperature.
        tavg (float): Average temperature.
        altitude (float): Altitude above sea level.
        ws (float): Wind speed.

    Returns:
        A JSON object containing the calculated reference evapotranspiration.
    """
    # Call the net_rad_calculator function from the ref_eva module to get the net radiation.
    net_rad = ref_eva.net_rad_calculator(day_of_year, latitude, dl_hours, sunshine_hours, albedo, tmin, tmax, altitude)

    # Call the ref_evt function from the ref_eva module to calculate the reference evapotranspiration.
    ET = ref_eva.ref_evt(net_rad, tavg, ws, tmin, altitude)

    # Return the result as a JSON object.
    return {"reference_evapotranspiration": ET}

# This block allows you to run the application directly from the command line.
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
