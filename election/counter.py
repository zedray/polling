def count_squares(grid):
    results = [0] * grid.no_of_parties
    for x in range(0, len(grid.squares)):
        for y in range(0, len(grid.squares[x])):
            s = grid.squares[x][y]
            results[s.party] += 1

    # Print the status
    print 'Raw election results'
    for i in range(0, len(results)):
        print 'Party ' + repr(i) + ' total:' + repr(results[i])
