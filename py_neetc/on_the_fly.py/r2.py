

def get_pattern(string):
    
    str_len = len(string)   
    splits = [[string[i-rep_length: i] for i in range(str_len, 0, -rep_length)] for rep_length in range(1, str_len//2)]
    reps = [[window == split[0] for window in split].index(False) for split in splits]
    max_reps = max(reps)
    best_index = reps.index(max_reps)
    best_rep_length = best_index + 1
    window = string[-best_rep_length:]
    prefix = string[0:str_len - max_reps*best_rep_length]
    return f'{prefix}({window})' if max_reps > 1 else None


if __name__=='__main__':
    print ("Start")

    p = get_pattern('AAAABDBDBDBDBDBDBDBDBDBDBDBDBDBDBDBDV')
    print (p)

    print ("END")
