import numpy as np

def hmm(obv):
    print('Observations: ' + obv)
    trans = np.matrix([[0.9,0.1],[0.1,0.9]])
    em = np.matrix([[0.8,0.2],[0.5,0.5]])
    v = np.zeros((2,len(obv)))
    path = np.zeros((2,len(obv)))

    v[0,0] = 0.5*em[0,int(obv[0])]
    v[1,0] = 0.5*em[1,int(obv[0])]

    for i in range(1,len(obv)):
        x = int(obv[i])
        p00 = v[0,i-1]*trans[0,0]
        p01 = v[0,i-1]*trans[0,1]
        p10 = v[1,i-1]*trans[1,0]
        p11 = v[1,i-1]*trans[1,1]
        v[0,i] = em[0,x]*max(p00, p10)
        v[1,i] = em[1,x]*max(p01, p11)
        if p10>p00:
            path[0,i] = 1
        if p11>p01:
            path[1,i] = 1

    i = len(obv)-1
    j = 0
    ml = []
    if v[:,len(obv)-1][1] > v[:,len(obv)-1][0]:
        j = 1
    while i >= 0:
        ml.append(str(int(j)))
        k = j
        j = path[int(k),int(i)]
        i -= 1

    states = ''.join(ml)[::-1]
    print('States:       ' + states)

    transitions = 0
    for i in range(len(states)-1):
        if states[i+1] != states[i]:
            transitions += 1
    print('Transitions:  ' + str(transitions))

with open('real_observations.txt') as obv_file:
    for line in obv_file:
        hmm(line.strip('\n'))