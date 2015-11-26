# FSM Simulation

edges = {(1, 'a') : 2,
         (2, 'a') : 2,
         (2, '1') : 3,
         (3, '1') : 3}

accepting = [3]

def fsmsim(string, current, edges, accepting):
    if string == "":
        return current in accepting
    else:
        letter = string[0]
        if(current,letter) in edges:
            destination=edges[(current,letter)]
            string_rem=string[1:]
            return fsmsim(string_rem,destination,edges,accepting)
        else: 
            return False
        
