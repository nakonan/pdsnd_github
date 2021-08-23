import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    known_city = False
    while (not known_city):
        city = input('Please enter the city name:\n').lower()
        if city in CITY_DATA.keys():
            known_city = True
    
    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    month = 'not_recorded'
    while (month != 'all' and month not in months):
        month = input('Please select a month (january, february, ... , june) or all:\n').lower()
        
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    week_days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day = 'inexistent'
    while (day != 'all' and day not in week_days):
        day = input('What day of the week do you want the statitics (monday, tuesday, ... sunday) or all:\n').lower()


    # Printing summary of the input: starting with the selected city
    print('\nLet\'s analyze bikeshare pattern in {}'.format(city))
    # The selected month
    if month == 'all':
        print('For the full period of {} through {}'.format(months[0], months[len(months)-1]))
    else:
        print('Only for the month of {}'.format(month))
    # And then the seleceted day of the week
    if day == 'all':
        print('Throughtout all weeks')
    else:
        print('Restricted to {}s only'.format(day))
    
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month 
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week 
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    # ------------------------------------------------------
    '''
      Since the bikeshare event occurs only through a given day, working
      either with 'Start Time' or with 'End Time' should result in the 
      same statistics. Hereafter, we will work with 'Start Time'.
    '''
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month from the Start Time column to create a month column
    df['month'] = df['Start Time'].dt.month

    # Most common month (from 1 to 6)
    most_common_month = df['month'].mode()[0]
    
    # Displaying now the most common travel month
    print('The most common travel month is          : {}'.format(most_common_month))

    # TO DO: display the most common day of week
    # ------------------------------------------------------
    # extract day from the Start Time column to create a day column
    df['day'] = df['Start Time'].dt.day

    # find the most common day (from 1 to 7)
    most_common_day = df['day'].mode()[0]
    
    # Displaying now the most common travel week
    print('The most common travel day of the week is: {}'.format(most_common_day))

    # TO DO: display the most common start hour
    # ------------------------------------------------------
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # find the most common hour (from 0 to 23)
    most_common_hour = df['hour'].mode()[0]    
    
    # Displaying now the most common travel start hour
    print('The most common travel hour is           : {}'.format(most_common_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    # ------------------------------------------------------
    common_start_station = df['Start Station'].mode()[0]

    # Displaying now the most common travel start station
    print('The most common travel start station is: {}'.format(common_start_station))

    # TO DO: display most commonly used end station
    # ------------------------------------------------------
    common_end_station = df['End Station'].mode()[0]
    
    # Displaying now the most common travel end station
    print('The most common travel end station is: {}'.format(common_end_station))


    # TO DO: display most frequent combination of start station and end station trip
    start_station, end_station = df[['Start Station', 'End Station']].mode().loc[0, :]
    
    # Displaying now the most common travel end station
    print('Frequent Start-End station: ({}, {})'.format(start_station,end_station))

    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = int(df['Trip Duration'].sum())
    
    # Additional conversion for easy displays
    (days, hours, minutes, secs) = time_conversion(total_travel_time)
    
    # Now displaying the total travel time
    print('The total travel time is equivalent to: {} day(s), {} hour(s), {} minute(s) and {} second(s); or {} seconds.'.format(days, hours, minutes, secs, total_travel_time))
    
    # TO DO: display mean travel time
    mean_travel_time = int(df['Trip Duration'].mean())

    # Additional conversion for easy displays
    (days, hours, minutes, secs) = time_conversion(mean_travel_time)
    
    # Now displaying the mean travel time
    print('The mean travel time is: {} day(s), {} hour(s), {} minute(s) and {} second(s); or {} seconds.'.format(days, hours, minutes, secs, mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def time_conversion(total_time):
    """Converts input time (in second) into days, hour, minutes and seconds."""

    day = total_time // 86400
    hour = (total_time % 86400) // 3600
    minute = ((total_time % 86400) % 3600) // 60
    sec = ((total_time % 86400) % 3600) % 60
    
    return (day, hour, minute, sec)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    
    # Displaying now count of user types
    print('Subscriber and Customer travelers were:')
    print('{}'.format(user_types.to_string()))


    # TO DO: Display counts of gender
    try:
        user_gender = df['Gender'].dropna().value_counts()
        
        # Displaying now gender count
        print('Travelers who provided their gender were:')
        print('{}'.format(user_gender.to_string()))
    except KeyError:
        print("Genders were not recorded for this city.")
        
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        user_earliest_birth_year = df['Birth Year'].dropna().min()
        user_most_recent_birth_year = df['Birth Year'].dropna().max()
        user_common_birth_year = df['Birth Year'].dropna().mode()

        # Displaying now statistics on birth year
        print('Statistics of travelers who provided birth year')
        print('  - Earliest birth year   : {}'.format(int(user_earliest_birth_year)))
        print('  - Most recent birth year: {}'.format(int(user_most_recent_birth_year)))
        print('  - Common birth year     : {}'.format(int(user_common_birth_year[0])))
    except KeyError:
        print("Birth years were not recorded for this city.")
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_data(df):
    '''Displays few rows of the dataframe (df)'''
	
    view_data = input('\nWould you like to view few rows of individual trip data? Enter yes or no\n')
	
    if view_data == 'yes':
        view_display = view_data
        view_more = (view_display == 'yes')
        next_rows_to_view = int(input('\nHow many rows at once would you like to view? Please enter a number:\n'))
        start_loc = 0
        while view_more:
            print(df.iloc[start_loc:start_loc + next_rows_to_view])
            start_loc += next_rows_to_view
            view_display = input('Do you wish to continue? Enter yes or no: ').lower()
            view_more = (view_display != 'no')


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        display_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
