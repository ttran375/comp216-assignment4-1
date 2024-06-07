# Lab 4 – Using threads.

This lab is a warm-up for the next assignment. We will learn to build a
multi-threaded application. You will write a function that will simulate
a long task. You will call the first method a number of times
sequentially and record the time it takes to complete. They will call
the first method again but in a threaded manner and time the execution
and then compare the two times.

## Description

Create three functions:

1.  Create a function to the following:

    1.  Take a string argument (name).

    2.  Create a loop that will run for 100_000 time. In this loop, the
        program will sleep 0.000_1 seconds.

    3.  After the completion of the loop, prints its name and a brief
        message.

2.  Create a second function to do the following:

    1.  Takes a number argument (times to execute the loop).

    2.  Store the current time.

    3.  Call the function in step 1 the required number of times
        (sequentially).

    4.  Check the elapse time after the above calls complete.

    5.  Print the results as well as a brief message.

3.  Create a third function to do the following:

    1.  Takes a number argument (times to execute the loop).

    2.  Store the current time.

    3.  Call the function in step 1 the required number of times (as
        threads).

    4.  Check the elapse time after the above calls complete

    5.  Print the results as well as a brief message

4.  Write the statements

    1.  To call the function in step 2 ten times

    2.  To call the function in step 3 ten times

#### Submission

1.  Your code file will be named «your_first_name».py \[*Do not zip your
    file*\]

2.  Must be uploaded to course dropbox before the deadline.

3.  See schedule for due date.