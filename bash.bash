#!/bin/bash

# Navigate to the directory where your Python program is located
cd /Desktop

# Infinite loop to continuously run the Python program
while true
do
    # Run the Python program
    python3 FlightTracker.py
    
    # Optionally, you can add a delay (in seconds) between each run
    # Adjust the sleep duration as needed
    sleep 10  # This will wait for 10 seconds before running the script again
done
