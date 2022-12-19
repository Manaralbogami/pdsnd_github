import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              ' new york city': 'new_york_city.csv',
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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
       city = input("Kindly Enter The City ")
       city = city.lower()
       if city in ['chicago','new york city','washington']:
           break
       else:
           print ("Kindly Enter correct input")

    # get user input for month (all, january, february, ... , june)
    month = input('Kindly Enter Month: ').lower()
    while month not in ['january','february',
        'march','april','may','june','all']:
          month = input('Kindly Month all, january, february, march, april,may,june:').lower()


    # get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
        day = input("Kindly Enter Day:")
        day = day.lower()
        if day in ['all','monday','tuesday','wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
            break
        else:
            print("Kindly Enter correct input")


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
        df - pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df= df[df['day_of_week'] == day.title()]
    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].mode()[0]
    print('Most common month :',common_month)


    # display the most common day of week
    common_day_of_week = df['day_of_week'].mode()[0]
    print('Most common day of week:',common_day_of_week)


    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = df['hour'].mode()[0]
    print('Most Common Hour:',most_common_hour)
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    start_station = df['Start Station'].value_counts().idxmax()
    print('Most commonly used start station:',start_station)


    # display most commonly used end station
    end_station = df['End Station'].value_counts().idxmax()
    print('Most commonly used end station',end_station)


    # display most frequent combination of start station and end station trip
    combination_start_end_station = df.groupby(['Start Station','End Station']).count()
    print('most frequent combination of start station and end station trip:',start_station,"&" ,end_station)



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = sum(df['Trip Duration'])
    print ('total travel time: ',total_travel_time / 86400,'days')


    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('mean travel time:',mean_travel_time /3600.0,'minutes')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    count_user_type = df['User Type'].value_counts()
    print('user type:\n',count_user_type)


    # Display counts of gender
    try:
     count_user_gender = df['Gender'].value_counts()
     print('\ncount_user_gender:\n',count_user_gender)
    except KeyError:
     print('No data available for this month.')

    # Display earliest, most recent, and most common year of birth

    try:
     earliest_year = int(df['Birth Year'].min())
     print('earliest year of birth:',earliest_year )
    except KeyError:
     print('No data available for this month.')
    # most recent 
    try:
     most_recent_year = int(df['Birth Year'].max())
     print('most recent year of birth:',most_recent_year)
    except KeyError:
      print('No data available for this month.')


    # most common 
    try:
      most_common_year = int(df['Birth Year'].value_counts().idxmax())
      print('most common year of birth:',most_common_year)
    except KeyError:
      print('No data available for this month.')



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
   #Raw data is displayed upon request by the user.
   # disply 5 lines 
    print('choose Enter to see  row data , choose no to ignore')
    x = 0
    while (input()!= 'no'):
        x = x+5
        print(df.head(x))

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
