# File: /opencryocore/utils/thermal_utils.py

def celsius_to_fahrenheit(celsius: float) -> float:
    """
    Converts Celsius temperature to Fahrenheit.
    """
    return (celsius * 9 / 5) + 32

def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """
    Converts Fahrenheit temperature to Celsius.
    """
    return (fahrenheit - 32) * 5 / 9

def kelvin_to_celsius(kelvin: float) -> float:
    """
    Converts Kelvin temperature to Celsius.
    """
    return kelvin - 273.15

def celsius_to_kelvin(celsius: float) -> float:
    """
    Converts Celsius temperature to Kelvin.
    """
    return celsius + 273.15

def calculate_heat_energy(watts: float, seconds: int) -> float:
    """
    Calculates energy in joules given power in watts and time in seconds.
    """
    return watts * seconds
