import numpy as np
from scipy.stats import qmc
sampler = qmc.LatinHypercube(d=2)



def resources():
    # food, luxury, strategic
    n_resources = [11, 12, 9]  # one of each
    n_resources = [33, 12, 20]  # 65 total

    #              min_x, min_y
    continents = [[47, 39],  # cw from top-left
                  [85, 39],
                  [48, 6],
                  [85, 5]]

    for count in n_resources:    
        for x,y in continents:
            l_bounds = [x, y]
            u_bounds = [x + 25, y + 25]
            
            raw_points = sampler.random(n=count)
            adjusted = np.array(qmc.scale(raw_points, l_bounds, u_bounds), dtype=int)
            
            print('\n'.join(f"{r:d},{c:d}" for r,c in adjusted))
        
        print('\n\n')



def goody_huts():
    l_bounds = [0, 0]
    u_bounds = [12, 12]
    
    offsets = np.array([[ 0,  0],
                        [13,  0],
                        [ 0, 13],
                        [13, 13]])
    results = []
    
    for off in offsets:
        raw_points = sampler.random(n=5)
        adjusted = np.array(qmc.scale(raw_points, l_bounds, u_bounds), dtype=int)
        adjusted += off
        
        results.append(adjusted)
    
    results = np.vstack(results)
    
    print_goodies(results, u_bounds + offsets[-1])
    
    return



def print_goodies(points, shape):
    board = np.full(shape, "_")

    for p in points:
        idx = tuple(p)
        board[idx] = "T"

    print('\n'.join((','.join(row) for row in board)).replace('T', 'True'))