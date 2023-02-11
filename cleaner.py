def cleaner(clean: list):
    ''' for removing duplicated elemnts plus the original duplicated element from the list'''

    for i in clean:
        if clean.count(i) != 1:

            for s in range(clean.count(i)):
                clean.remove(i)

    return clean
