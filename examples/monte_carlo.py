import os
import numpy as np
import orhelper
from random import gauss
import math


class LandingPoints(list):
    "A list of landing points with ability to run simulations and populate itself"

    def __init__(self):
        self.ranges = []
        self.bearings = []

    def add_simulations(self, num):
        with orhelper.OpenRocketInstance() as instance:

            # Load the document and get simulation
            orh = orhelper.Helper(instance)
            doc = orh.load_doc(os.path.join('/home/robbot/Desktop/UW/Waterloo-Rocketry/', '2p4SimWRSE.ork'))
            sim = doc.getSimulation(0)

            # Randomize various parameters
            opts = sim.getOptions() 
            rocket = opts.getRocket()

            # Run num simulations and add to self
            for p in range(num):
                print('Running simulation ', p)

                # Set Options

                # Units are in m/s so conversion needed
                opts.setLaunchRodLength(260 * 2.54) # 260 inches to cm
                opts.setLaunchRodAngle(math.radians(gauss(5, 1)))  # 5 +- 1 deg in Launch Angle
                opts.setLaunchRodDirection(math.radians(gauss(90, 1)))  # 90 +- 1 deg in direction
                
                opts.setWindSpeedAverage(gauss(9 * 0.44707, 1 * 0.44707))  # 9 mph +- 1 in wind
                opts.setWindSpeedDeviation(gauss(0.9 * 0.44707, 0.1 * 0.44707))  # 0.9 mph +- 0.1 Std.Dev of wind
                opts.setWindTurbulenceIntensity(0.1)  # 10%
                opts.setWindDirection(gauss(90, 30))  # 90+-30 deg

                opts.setLaunchLongitude(-106) # -106E
                opts.setLaunchLatitude(32.9) # 32.9N
                opts.setLaunchAltitude(4848*0.3048) # 4848 ft

                opts.setLaunchTemperature(gauss(27.778, 1))  # 27.778 +- 1 Celcius (82 F) in Temperature
                opts.setLaunchPressure(gauss(1008, 1))  # 1008 mbar +- 1 in Pressure




                """
                
                for component_name in ('Nose cone', 'Body tube'):  # 5% in the mass of various components
                    component = orh.get_component_named(rocket, component_name)
                    mass = component.getMass()
                    component.setMassOverridden(True)
                    component.setOverrideMass(mass * gauss(1.0, 0.05))
                """

                airstarter = AirStart(1000)  # simulation listener to drop from 0m
                lp = LandingPoint(self.ranges, self.bearings)
                orh.run_simulation(sim, listeners=(airstarter, lp))
                self.append(lp)
                print("lp", self.ranges, self.bearings)

    def print_stats(self):
        print(
            'Rocket landing zone %3.2f m +- %3.2f m bearing %3.2f deg +- %3.4f deg from launch site. Based on %i simulations.' % \
            (np.mean(self.ranges), np.std(self.ranges), np.degrees(np.mean(self.bearings)),
             np.degrees(np.std(self.bearings)), len(self)))


class LandingPoint(orhelper.AbstractSimulationListener):
    def __init__(self, ranges, bearings):
        self.ranges = ranges
        self.bearings = bearings

    def endSimulation(self, status, simulation_exception):
        worldpos = status.getRocketWorldPosition()
        conditions = status.getSimulationConditions()
        launchpos = conditions.getLaunchSite()
        
        """
        geodetic_computation = conditions.getGeodeticComputation()

        if geodetic_computation != geodetic_computation.FLAT:
            raise Exception("GeodeticComputationStrategy type not supported")
        """
    
        self.ranges.append(range_flat(launchpos, worldpos))
        self.bearings.append(bearing_flat(launchpos, worldpos))


class AirStart(orhelper.AbstractSimulationListener):

    def __init__(self, altitude):
        self.start_altitude = altitude

    def startSimulation(self, status):
        position = status.getRocketPosition()
        position = position.add(0.0, 0.0, self.start_altitude)
        status.setRocketPosition(position)


METERS_PER_DEGREE_LATITUDE = 111325
METERS_PER_DEGREE_LONGITUDE_EQUATOR = 111050


def range_flat(start, end):
    dy = (end.getLatitudeDeg() - start.getLatitudeDeg()) * METERS_PER_DEGREE_LATITUDE
    dx = (end.getLongitudeDeg() - start.getLongitudeDeg()) * METERS_PER_DEGREE_LONGITUDE_EQUATOR
    return math.sqrt(dy * dy + dx * dx)


def bearing_flat(start, end):
    dy = (end.getLatitudeDeg() - start.getLatitudeDeg()) * METERS_PER_DEGREE_LATITUDE
    dx = (end.getLongitudeDeg() - start.getLongitudeDeg()) * METERS_PER_DEGREE_LONGITUDE_EQUATOR
    return math.pi / 2 - math.atan(dy / dx)


if __name__ == '__main__':
    print("Time, Altitude, Total Acceleration, Total Velocity, Stability, Pressure")
    points = LandingPoints()
    points.add_simulations(1)
    points.print_stats()
