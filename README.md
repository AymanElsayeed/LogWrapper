# Log Wrapper 

## Description
This is a simple log wrapper for python.

## Motivation
    I wanted to log when a function execution started and execution ended, and set the logging level dynamicly.
 
    but exclude helper function logging as info level.

    E.X:

    Function B which called by function A, function A's logging level is set to INFO, but function B's logging level is Debug.