from calendar import month_name
import time
import pandas as pd

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
    while True:
        city =input("please show which city that you want to display its data : chicago, new york city, washington: /n").lower()
        cities_names = ('chicago','new york city','washington')         
        if city in cities_names:
          break
        else:
            print("show a correct city")
   
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("please show which month that you want to display its data from january to june, or tybe 'all' to display all months: /n").lower()
        months_names = ['january', 'february', 'mars', 'april', 'may', 'june', 'all']         
        if month in months_names:
            break
        else:
            print("show a correct month")             
    

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
        day = input("please show a day of the week, or tybe 'all' to display all days: /n").lower()
        days_names = ['monday', 'tuseday', 'wednesday', 'thursday', 'friday','saturday', 'sunday','all']        
        if day in days_names:
            break
        else:
            print("show a correct day")
             
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
    months_names = ['january', 'february', 'mars', 'april', 'may', 'june', 'all']
    days_names = ['monday', 'tuseday', 'wednesday', 'thursday', 'friday','saturday', 'sunday','all']

    df = pd.read_csv(CITY_DATA[city])
    df['start time'] = pd.to_datetime(df['start time'])
    df['month'] = df['start time'].dt.the_month_of_the_year
    df['day'] = df['start time'].dt.the_day_of_the_week
    df['hour'] = df['start time'].dt.the_hour_of_the_day
    
    if month != 'all':
        month = months_names.index(month) +1
        df = df[df['month'] == month]
        print(f"Data is filterd according to chosen month : {month}")
    if day != 'all':
        day = days_names.index(day) +1
        df = df[df['day'] == day]
        print(f"Data is filterd according to chosen day : {day}")
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('most common month of travelling is:',popular_month)


    # TO DO: display the most common day of week
    popular_day = df['day'].mode()[0]
    print('most common day of travelling is:',popular_day)


    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('most common hour of travelling is:',popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['start station'].mode()[0]
    print('most common start station is:',start_station)

    # TO DO: display most commonly used end station
    end_station = df['end station'].mode()[0]
    print('most common end station is:',end_station)

    # TO DO: display most frequent combination of start station and end station trip
    combination_station = df['combination station'].mode()[0]
    print('most common combination station is:',combination_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['duration of the trip'].sum()
    print(f"the total time of the travel is : {total_travel_time} mins")


    # TO DO: display mean travel time
    avg_travel_time = df['duration of the trip'].mean()
    print(f"the avg time of the travel is : {avg_travel_time} mins")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_of_the_user_types =df['user type'].value_counts()
    print('count_of_the_user_types is:',count_of_the_user_types)
    
    # TO DO: Display counts of gender
    

    count_of_gender =df['gender'].value_counts()
    print('count_of_the_gender is:',count_of_gender)
    
    if city == 'washington':
        print("i am sorry there is no data available for this month")
    
    
    # TO DO: Display earliest, most recent, and most common year of birth
  
    earliest_year =(df['birth year'].min())
    print('earliest_year is:',earliest_year)
    
    if city == 'washington':
        print("i am sorry there is no data available for this month")
        

    most_recent_year =(df['birth year'].max())
    print('most_recent_year is:',most_recent_year)
    
    if city == 'washington':
        print("i am sorry there is no data available for this month")
        

    most_common_year =(df['birth year'].mode()[0])
    print('most_common_year is:',most_common_year)
    
    if city == 'washington':
        print("i am sorry there is no data available for this month")
        
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


    
def display_raw_data():
    city = input("please show which city that you want to display its data from (chicago, new york city, washington: /n").lower()
    df = pd.read_csv(CITY_DATA[city])
    str_row = 1
    while True:
            answer = input(" do you really want to show 5 lines of raw data? yes / no :").strip().lower()
            if answer == 'yes':
                print(df.iloc[str_row:str_row+5])
                str_row+= 5
            elif answer =='no':
                print("please enter the correct answer")
                
            
        
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_raw_data()
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
