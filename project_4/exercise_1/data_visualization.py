from pandas import *
from ggplot import *

def plot_weather_data(turnstile_weather):
    '''
    You are passed in a dataframe called turnstile_weather. 
    Use turnstile_weather along with ggplot to make a data visualization
    focused on the MTA and weather data we used in assignment #3.  
    You should feel free to implement something that we discussed in class 
    (e.g., scatterplots, line plots, or histograms) or attempt to implement
    something more advanced if you'd like.  

    Here are some suggestions for things to investigate and illustrate:
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

    '''
    Things I need to convert/create:
        - 

    * Ridership by time of day on weekday vs weekend
        Group EXITSn_hourly into 3-hour bins 


    * Ridership by day of week versus temperature (above/below average) and rain
        Convert dates to days of the week

        Group by greater than average (global average for simplicity?) temperature or by rain
        Sum EXITSn_hourly into days of the week

    '''


    def reformat_subway_dates(date):
        date_formatted = int(datetime.strftime(datetime.strptime(date, "%Y-%m-%d"),'%w'))
        return date_formatted
    
    set_option('chained_assignment', None)
    
    turnstile_weather['day_of_week'] = turnstile_weather['DATEn'].map(reformat_subway_dates)
    
    
    daily_averages = turnstile_weather.groupby(['day_of_week','rain'])['ENTRIESn_hourly'].mean()
    
    #http://stackoverflow.com/questions/10373660/converting-a-pandas-groupby-object-to-dataframe?rq=1
    daily_averages = daily_averages.reset_index()#
    
    plot = ggplot(aes(x='day_of_week',y='ENTRIESn_hourly', color='rain'),data=daily_averages) + \
    geom_point() + \
    geom_line() + \
    ggtitle('Average NYC Subway Ridership by Day and Rain (Blue) vs No Rain (Red)') + \
    xlab('Day of the Week') + \
    ylab('Average Number of Riders') +\
    xlim(-0.1, 6.1) +\
    scale_x_continuous( labels=("","Sun","Mon", "Tue", "Wed", "Thu", "Fri", "Sat"))



    #daygrouping = turnstile_weather.groupby(['day_of_week'])
    #daygrouping_entries  = daygrouping ['ENTRIESn_hourly']
    #daily_averages = daygrouping_entries.mean()


    plot = ggplot(turnstile_weather, aes('day_of_week','EXITSn_hourly')) + geom_bar(stat = "bar")+ \
      ggtitle('NYC Subway Ridership by Hour') + xlab('Hour') + ylab('Number of Riders')

    plot = ggplot(turnstile_weather, aes('Hour','EXITSn_hourly')) + geom_bar(stat = "bar")+ \
      ggtitle('NYC Subway Ridership by Hour') + xlab('Hour') + ylab('Number of Riders')

    return plot


if __name__ == "__main__":
    image = "plot.png"
    with open(image, "wb") as f:
        turnstile_weather = pd.read_csv(input_filename)
        turnstile_weather['datetime'] = turnstile_weather['DATEn'] + ' ' + turnstile_weather['TIMEn']
        gg =  plot_weather_data(turnstile_weather)
        ggsave(f, gg)
