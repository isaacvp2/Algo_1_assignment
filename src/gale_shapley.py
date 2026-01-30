import sys
import input_parser
import output_writer


def gale_shapley(n, hospital_prefs, student_prefs):
    
    # Initialize each student and hospital to be free
    free_hospitals = list(range(n))
    student_partners = [-1] * n  # -1 means free/unmatched

    next_proposal = [0] * n
    
    student_ranks = []
    for s in range(n):
        ranks = {}
        for rank, h in enumerate(student_prefs[s]):
            ranks[h] = rank
        student_ranks.append(ranks)
    
    # while hospital is free and hasn't been matched
    while free_hospitals:
        # choose hospital h
        h = free_hospitals.pop(0)
        
        # check if h has proposed to everyone
        if next_proposal[h] >= n:
            continue
        
        # a = 1st applicant on h list 
        a = hospital_prefs[h][next_proposal[h]]
        next_proposal[h] += 1
        
        # If a is free
        if student_partners[a] == -1:
            # Assign h and a
            student_partners[a] = h
        else:
            h_prime = student_partners[a]

            # a prefers h over h'
            if student_ranks[a][h] < student_ranks[a][h_prime]:
                student_partners[a] = h
                free_hospitals.append(h_prime)
            else:
                # a rejects h
                free_hospitals.append(h)
    
    return student_partners


def main():
    try:
        raw_lines = sys.stdin.readlines()
        n, hospital_prefs, student_prefs, _ = input_parser.parse_input(raw_lines)

        if n == None and hospital_prefs == None and student_prefs == None:
            print("Program stopped because of invalid input.")
            return
        

        student_partners = gale_shapley(n, hospital_prefs, student_prefs)
        
        hospital_partners = [-1] * n
        for s, h in enumerate(student_partners):
            if h != -1:
                hospital_partners[h] = s
        
        matchings = []
        for h, s in enumerate(hospital_partners):
            if s != -1:
                matchings.append([h + 1, s + 1])
        
        output_writer.write_output(matchings)
            
    except Exception as e:
        sys.stderr.write(f"Error: {e}\n")


if __name__ == "__main__":
    main()