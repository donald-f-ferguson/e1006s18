import __main__ as main

def is_interactive():
    import __main__ as main
    return not hasattr(main, '__file__')

print("Is interactive = ", is_interactive())

print("Doc = ", getattr(main, "__doc__"))
print("Name = ", getattr(main, "__name__"))
if (not is_interactive()):
    print("File = ", getattr(main, "__file__"))
else:
    print("No file for me.")