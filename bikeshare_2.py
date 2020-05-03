import time
import datetime as dt
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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ''
    while city == '' or city.lower() != 'Chicago'.lower() or city.lower() != 'New York'.lower() or city.lower() != 'Washington'.lower():
        city = input ('\nWould you like to see data from wich city? Chicago, New York or Washington?\n')
        if city.lower() == 'Chicago'.lower() or city.lower() == 'New York'.lower() or city.lower() == 'Washington'.lower():
            break
        elif city.lower() != 'Chicago'.lower() or city.lower() != 'New York'.lower() or city.lower() != 'Washington'.lower():
            print('\n{} is not in the list of citys\n'.format(city.title()))


    # get user input for month (all, january, february, ... , june)
    month_filter = ''
    day_filter = ''
    month = ''
    day = ''
    while True:
        month_filter = input ('\nWould you like to filter by month? y/n\n')
        if month_filter == 'y':
            while True:
                month = input('\nWich month do you like to filter? January, February, March, April, May or June?\n')
                if month.lower() == '' or month.lower() == 'January'.lower() or month.lower() == 'February'.lower() or month.lower() == 'March'.lower() or month.lower() == 'April'.lower() or month.lower() == 'May'.lower() or month.lower() == 'June'.lower():
                    while True:
                        day_filter = input ('\nWould you like to filter by day? y/n\n')
                        if day_filter == 'y':
                            while True:
                                day = input('\nWich day do you like to filter? Monday, Tuesday, Wenesday, Thursday, Friday, Saturday or Sunday?\n')
                                if day.lower() == 'Monday'.lower() or day.lower() == 'Tuesday'.lower() or day.lower() == 'Wednesday'.lower() or day.lower() == 'Thursday'.lower() or day.lower() == 'Friday'.lower() or day.lower() == 'Saturday'.lower() or day.lower() == 'Sunday'.lower():
                                    break
                                elif day.lower() == '' or day.lower() != 'Monday'.lower() or day.lower() != 'Tuesday'.lower() or day.lower() != 'Wednesday  '.lower() or day.lower() != 'Thursday  '.lower() or day.lower() != 'Friday  '.lower() or day.lower() != 'Saturday  '.lower() or day.lower() != 'Sunday  '.lower():
                                    print('{} is not a valid day'.format(day.title()))
                        elif day_filter == 'n':
                            break
                        break
                    break
                elif month.lower() == '' or month.lower() != 'January'.lower() or month.lower() != 'February'.lower() or month.lower() != 'March'.lower() or month.lower() != 'April'.lower() or month.lower() != 'May'.lower() or month.lower() != 'June'.lower():
                    print('{} is not a valid month'.format(month.title()))
            break
        elif month_filter == 'n':
            while True:
                day_filter = input ('\nWould you like to filter by day? y/n\n')
                if day_filter == 'y':
                    while True:
                        day = input('\nWich day do you like to filter? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday?\n')
                        if day.lower() == 'Monday'.lower() or day.lower() == 'Tuesday'.lower() or day.lower() == 'Wednesday'.lower() or day.lower() == 'Thursday'.lower() or day.lower() == 'Friday'.lower() or day.lower() == 'Saturday'.lower() or day.lower() == 'Sunday'.lower():
                            break
                        elif day.lower() == '' or day.lower() != 'Monday'.lower() or day.lower() != 'Tuesday'.lower() or day.lower() != 'Wednesday  '.lower() or day.lower() != 'Thursday  '.lower() or day.lower() != 'Friday  '.lower() or day.lower() != 'Saturday  '.lower() or day.lower() != 'Sunday  '.lower():
                            print('{} is not a valid day'.format(day.title()))
                elif day_filter == 'n':
                    break
                break
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)

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
    if city.lower() == 'new york':
        city = 'new york city'

    df = pd.read_csv(CITY_DATA[city.lower()])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month
    df['Day'] = df['Start Time'].dt.weekday

    #filter month

    if month != '':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month.lower()) + 1
        df = df[df['Month'] == month]
    else:
        df = df
    #filter day
    if day!= '':
        days_of_week = ['monday','tuesday', 'wenesday', 'thursday', 'friday', 'saturday', 'sunday']
        day = days_of_week.index(day.lower())
        df = df[df['Day'] == day]
    else:
        df = df

    return df

def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    if month == '':
        print('\nMost common month: {}, count: {}\n'.format(months[df['Month'].mode()[0] - 1].title(), df['Month'][df['Month'] == df['Month'].mode()[0]].count()))
        print('\nCalculating next statistics...\n')
    # display the most common day of week
    days_of_week = ['monday','tuesday', 'wenesday', 'thursday', 'friday', 'saturday', 'sunday']
    if day == '':
        print('\nMost common day of week: {}, count: {}\n'.format(days_of_week[df['Day'].mode()[0]].title(), df['Day'][df['Day'] == df['Day'].mode()[0]].count()))
        print('\nCalculating next statistics...\n')
    # display the most common start hour

    df['Hour'] = df['Start Time'].dt.hour
    print('\nMost common start hour: {}Hr, count: {}\n'.format(df['Hour'].mode()[0], df['Hour'][df['Hour'] == df['Hour'].mode()[0]].count()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    # display most commonly used start station
    print('\nMost commonly used start station: {}, count: {}\n'.format(df['Start Station'].mode()[0], df['Start Station'][df['Start Station'] == df['Start Station'].mode()[0]].count()))
    print('\nCalculating next statistics...\n')
    # display most commonly used end station
    print('\nMost commonly used End station: {}, count: {}\n'.format(df['End Station'].mode()[0], df['End Station'][df['End Station'] == df['End Station'].mode()[0]].count()))
    print('\nCalculating next statistics...\n')
    # display most frequent combination of start station and end station trip
    df['Start End Stations'] =  'Start Station: ' + df['Start Station'] + '\nEnd Station: ' + df['End Station']
    print('\nMost frequent combination of start station and end station trip:\n\n{},\ncount: {}\n'.format(df['Start End Stations'].mode()[0], df['Start End Stations'][df['Start End Stations'] == df['Start End Stations'].mode()[0]].count()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    # display total travel time
    print('\nTotal travel time: {}\n'.format(dt.timedelta(seconds = float(df['Trip Duration'].count()))))
    print('\nCalculating next statistics...\n')
    # display mean travel time
    print('\nMean travel time: {}\n'.format(dt.timedelta(seconds = float(df['Trip Duration'].mean()))))

    print("\nThis took %s seconds.\n" % (time.time() - start_time))
    print('-'*40)

def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('\nCounts of user types:\n\n{}\n\nCounts of all user types: {}\n'.format(df.groupby(['User Type'])['User Type'].count(), df['User Type'].count()))
    print('\nCalculating next statistics...\n')
    if 'Gender' in df:
        # Display counts of gender
        print('\nCounts of user by gender:\n\n{}\n'.format(df.groupby(['Gender'])['Gender'].count()))
        print('\nCalculating next statistics...\n')
    else:
        print("\n{} don't have gender data\n".format(city).title())
        print('\nCalculating next statistics...\n')

    if 'Birth Year' in df:
        # Display earliest, most recent, and most common year of birth
        print('\nThe earliest year of birth is {}\n'.format(df['Birth Year'].min()))
        print('\nCalculating next statistics...\n')
        print('\nThe most recent year of birth is {}\n'.format(df['Birth Year'].max()))
        print('\nCalculating next statistics...\n')
        print('\nThe most common year of birth is {}\n'.format(df['Birth Year'].mode()[0]))
    else:
        print("\n{} don't have Birth Year data\n".format(city).title())

    print("\nThis took %s seconds.\n" % (time.time() - start_time))
    print('-'*40)

def raw_data(df, city):
#Variable that show raw data.
    pd.set_option('display.max_columns', None)
    if city.lower() == 'new york':
        city = 'new york city'
    df = pd.read_csv(CITY_DATA[city.lower()])
    chucker(df)

    show_raw_data = ''
    cont = ''
    show_raw_data = input ('Do you want to see the raw data? y/n\n')

    if (show_raw_data == 'y' and (cont != 'n' or cont != 'no')) or (show_raw_data == 'yes' and (cont != 'n' or cont != 'no')):
        for lines in chucker(df):
            if cont == 'y' or cont == 'yes' or (cont == '' and (show_raw_data == 'y' or show_raw_data == 'yes')):
                print(lines)
                cont = input ('Do you want to continue to see the raw data? y/n\n')
            elif cont == 'n' or cont == 'no' or show_raw_data == 'n' or show_raw_data == 'no':
                break
            else:
                print("{} isn't a valid awnser".format(cont))
                break
    elif (show_raw_data == 'n' and cont == '') or (show_raw_data == 'no' and cont == ''):
        print('')
    else:
        print("{} isn't a valid awnser".format(show_raw_data))

def show_data (df,city, month, day):
#Filter based on the data that the user wants to see
    data_functions = {'times of travel': 'time_stats(df, month, day)', 'stations': 'station_stats(df)','trip duration': 'trip_duration_stats(df)', 'users': 'user_stats(df, city)'}
    filters = ['times of travel', 'stations', 'trip duration', 'users']
    while True:
        input_filter_data = input ('\nWich data do you want to see? Times of travel, stations, trip duration, users data or all?\n')
        print('-'*40)
        list_inpu, length = pro_input(input_filter_data)
        for i in range(length):
            for filter in chucker(filters):
                if list_inpu[i] in filters:
                    if data_functions[list_inpu[i]] == 'time_stats(df, month, day)':
                        time_stats(df, month, day)
                    elif data_functions[list_inpu[i]] == 'station_stats(df)':
                        station_stats(df)
                    elif data_functions[list_inpu[i]] == 'trip_duration_stats(df)':
                        trip_duration_stats(df)
                    elif data_functions[list_inpu[i]] == 'user_stats(df, city)':
                        user_stats(df, city)
                    break
                elif list_inpu[i] == 'all':
                    time_stats(df, month, day)
                    station_stats(df)
                    trip_duration_stats(df)
                    user_stats(df, city)
                    break
                else:
                    print('\n{} not a valid awnser\n'.format(list_inpu[i]))
                break
        break

def chucker(iterable):
    while True:
        for i in range(0, len(iterable), 5):
            yield iterable[i:i + 5]

def pro_input(raw_input):
#Variable to process de raw input
    raw_input = raw_input.lower()
    string_proc = raw_input.replace(', ', ',')
    string_proc = string_proc.replace(' and ', ',')
    list_inpu = string_proc.rsplit(',')
    length = len(list_inpu)

    return list_inpu, length



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        show_data (df,city, month, day)
        raw_data(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
