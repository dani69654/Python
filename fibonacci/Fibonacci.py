def fibonacci (_numberOfTimes):
    old = 0;
    new = 1;
    result = 0;

    counter = 0;

    print(result);

    while(counter < _numberOfTimes):

        result = old + new;
        print (result);

        old = new;
        new = result;
        counter = counter +1;



fibonacci(10); #Set how deep you want to go
