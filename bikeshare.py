import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv' }

cities = ['Chicago','New York City','Washington']
months = ['January', 'February', 'March', 'April', 'May' ,'June', 'All' ]
days = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday','Friday']

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
    while True:
        city = input('Please input the city you want to explore\n Chicago\n New York City\n Washington\n')
        city = city.title()
        if city in cities:
            break
        else: 
            print('Ops! it seems your input is not on our list. Please input another city')
        
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('Input month for specified data ...\n')
        month = month.title()
        if month in months:
            break
        else:
            print('Invalid input .... please check your spelling or enter another input\n')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Please input a day\n')
        day = day.title()
        if day in days:
            break
        else:
            print('Invalid input .... please check your spelling or enter another input')
    
    
    
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
    df = pd.read_csv(CITY_DATA[city])
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('The most common month is: ', df['month'].mode()[0])


    # TO DO: display the most common day of week
    print('The most common day is: ', df['day_of_week'].mode()[0])


    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print('The most common start hour is: ', df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('The most common start station is: ', df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print('The most common end station is: ', df['End Station'].mode()[0])


    # TO DO: display most frequent combination of start station and end station trip
    df['Combined Stations'] = df['Start Station'] + ' and ' + df['End Station']
    print('The most frequent combination of start station and end station trip is: ', df['Combined Stations'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('The total travel time is: ', df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print('The mean travel time is: ', df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('The counts of user types are: ', df['User Type'].value_counts())

    # TO DO: Display counts of gender
    if city != 'Washington':
        print('The counts of gender are: ',df['Gender'].value_counts())
    else:
        print('Sorry ... no avaliable data about gender for Washington.')

    # TO DO: Display earliest, most recent, and most common year of birth
    if city != 'Washington':
        earliest_yof = int(df['Birth Year'].min())
        print('The earliest year of birth is: ', earliest_yof)
        recent_yof = int(df['Birth Year'].max())
        print('The recent year of birth is: ', recent_yof)
        common_yof = int(df['Birth Year'].mode()[0])
        print('The common year of birth is: ', common_yof)
    else:
        print('Sorry ... no avaliable data about birth year for Washington.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
