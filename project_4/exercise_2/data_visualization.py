from pandas import *
from ggplot import *

from pandas import *
from ggplot import *

def plot_weather_data(turnstile_weather):
    ''' 
    Use ggplot to make another data visualization focused on the MTA and weather
    data we used in assignment #3. You should make a type of visualization different
    than you did in exercise #1, and try to use the data in a different way (e.g., if you
    made a lineplot concerning ridership and time of day in exercise #1, maybe look at weather
    and try to make a histogram in exercise #2). 
    
    You should feel free to implement something that we discussed in class
    (e.g., scatterplots, line plots, or histograms) or attempt to implement 
    something more advanced if you'd like.  Here are some suggestions for things
    to investigate and illustrate:
    * Ridership by time of day or day of week
    * How ridership varies based on Subway station
    * Which stations have more exits or entries at different times of day

    If you'd like to learn more about ggplot and its capabilities, take
    a look at the documentation at:
    https://pypi.python.org/pypi/ggplot/
    
    You can check out: 
    https://www.dropbox.com/s/meyki2wl9xfa7yk/turnstile_data_master_with_weather.csv
     
    To see all the columns and data points included in the turnstile_weather 
    dataframe. 
    
    However, due to the limitation of our Amazon EC2 server, we are giving you about 1/3
    of the actual data in the turnstile_weather dataframe
    '''
    def bin_subway_hours(hour):
        hour_formatted = int(hour//3)
        return hour_formatted
    
    def reformat_subway_dates(date):
        date_formatted = int(datetime.strftime(datetime.strptime(date, "%Y-%m-%d"),'%w'))
        return date_formatted

    def weekend_or_weekday_test(day_of_week):
        if (day_of_week == 0 | day_of_week == 6):
            is_weekend = 1
        else:
            is_weekend = 0
        return is_weekend


    set_option('chained_assignment', None)
    turnstile_weather['day_of_week'] = turnstile_weather['DATEn'].map(reformat_subway_dates)

    set_option('chained_assignment', None)
    turnstile_weather['weekend_or_weekday'] = turnstile_weather['day_of_week'].map(weekend_or_weekday_test)

    set_option('chained_assignment', None)
    turnstile_weather['hour_bin'] = turnstile_weather['Hour'].map(bin_subway_hours)

    hourly_averages = turnstile_weather.groupby(['hour_bin', 'weekend_or_weekday'])['ENTRIESn_hourly'].mean()
    hourly_averages = hourly_averages.reset_index()#
    
    #print hourly_averages

    plot = ggplot(aes(x='hour_bin',y='ENTRIESn_hourly', color='weekend_or_weekday'),data=hourly_averages) + \
    geom_point() + \
    geom_line() + \
    ggtitle('Average NYC Subway Ridership by Hour and Weekend (Blue) vs Weekday (Red)') + \
    xlab('Hour of the Day') + \
    ylab('Average Number of Riders') +\
    xlim(-0.1, 7.1) +\
    scale_x_continuous( labels=("","0-2","3-5", "6-8", "9-11", "12-14", "15-17", "18-20","21-23"))

    #plot = ggplot(turnstile_weather, aes('EXITSn_hourly', 'ENTRIESn_hourly')) + stat_smooth(span=.15, color='black', se=True)+ geom_point(color='lightblue') + ggtitle("MTA Entries By The Hour!") + xlab('Exits') + ylab('Entries')
    
    return plot

if __name__ == "__main__":
    image = "plot.png"
    with open(image, "wb") as f:
        turnstile_weather = pd.read_csv(input_filename)
        turnstile_weather['datetime'] = turnstile_weather['DATEn'] + ' ' + turnstile_weather['TIMEn']
        gg =  plot_weather_data(turnstile_weather)
        ggsave(f, gg)