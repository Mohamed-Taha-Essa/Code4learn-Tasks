'''
10.Build a countdown calculator. Write some code that can take two dates as input, and
then calculate the amount of time between them

'''
import datetime
def calculateDifferenceBetweenTime(dt1 ,dt2):
    # difference between datetime in timedelta
    delta = dt2 - dt1
    print(f'Difference is {delta} ')

if __name__ == '__main__':
    # convert string to datetime
    dt1 = datetime.datetime(2023,9,20,5,16,20)
    dt2 = datetime.datetime(2023,9,25,14,5,20)

    calculateDifferenceBetweenTime(dt1,dt2)
    # can using lambda function
    print((lambda dt1, dt2: dt2 - dt1)(dt1,dt2))
