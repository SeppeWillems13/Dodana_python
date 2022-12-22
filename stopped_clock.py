def main():
    departure_home_hours = int(input("Departure home hours:"))
    departure_home_minutes = int(input("Departure home minutes:"))
    arrival_friend_hours = int(input("Arrival friend hours:"))
    arrival_friend_minutes = int(input("Arrival friend minutes:"))
    departure_friend_hours = int(input("Departure friend hours:"))
    departure_friend_minutes = int(input("Departure friend minutes:"))
    arrival_home_hours = int(input("Arrival home hours:"))
    arrival_home_minutes = int(input("Arrival home minutes:"))

    def time_to_minutes(hours, minutes):
        return hours * 60 + minutes

    def minutes_to_hour_and_minutes(minutes):
        hours = int(minutes // 60)
        minutes = int(minutes % 60)
        return hours, minutes

    # Calculate the total time spent at the friend's house
    time_spent_at_friend_house = time_to_minutes(departure_friend_hours, departure_friend_minutes) - time_to_minutes(arrival_friend_hours, arrival_friend_minutes)

    # Calculate the total time for the round trip
    round_trip_time = time_to_minutes(arrival_home_hours, arrival_home_minutes) - time_to_minutes(departure_home_hours, departure_home_minutes)

    # Calculate the time when Andrea left her own home
    time_left_home = (time_spent_at_friend_house - round_trip_time) / 2

    # Calculate the correct time when Andrea returns home
    correct_arrival_time = time_spent_at_friend_house + time_left_home

    # Check if the arrival time is on the next day
    if correct_arrival_time < time_to_minutes(departure_friend_hours, departure_friend_minutes):
        correct_arrival_time += 1440  # Add 24 hours in minutes to make it the next day

    # Convert the correct time in minutes back into hours and minutes
    correct_arrival_hours, correct_arrival_minutes = minutes_to_hour_and_minutes(correct_arrival_time)

    # Print the result
    print(correct_arrival_hours, correct_arrival_minutes)
