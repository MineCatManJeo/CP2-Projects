# Gabriel Crozier, Traciong notes

# What is tracing?
# It lets you see what is happening with your functions
# python -m trace --trace random_notes_and_idiotic_stuff/tracingNotes.py
"""
--trace (displays function lines as they are executed)
--count (displays the number of times each funciton is executed)
--listfuncs (displays the functions in the project)
--trackcalls (displays relationships between the functions)
"""
import trace
import sys

tracer = trace.Trace(count=False,trace=True)
def trace_calls(frame,event,arg):
    if event == 'call':
        print(f'Calling function: {frame.f_code.co_name}')
    elif event =='line':
        print(f"Executing line: {frame.f_lineno} in {frame.f_code.co_name}")
    elif event == 'return':
        print(f"{frame.f_code.co_name} returned {arg}")
    elif event == 'exception':
        print(f"Exception in {frame.f_code.co_name}: {arg}")
    return trace_calls

sys.settrace(trace_calls)
"""
Event Types:
call - when the function is called
line - when a new line is executed
return - when the function returns a value
exception - when there is an exception raised
"""
# What are some ways we can debug by tracing?
    # Make a dunction that lets us see how our functions and interacted and running


# How do you access the debugger in VS Code?
    # You press f5 or go to the bug on the side bar
# What is testing?
# What are boundary conditions?
# How do you handle when users give strange inputs?

def sub(numone, numtwo):
    print(numone-numtwo)

def add(numone, numtwo):
    sub(numone,numtwo)
    return numone + numtwo

print(add(1,1))
#tracer.run('sub(8,2)')