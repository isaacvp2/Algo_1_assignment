import input_parser
import output_parser
import sys

def verify(n, hospital_prefs, student_prefs, matchings):
    
    matched_hospitals = set()
    matched_students = set()
    
    # student_partner_map[student] -> hospital
    student_partner_map = {} 
    # hospital_partner_map[hospital] -> student
    hospital_partner_map = {}

    if len(matchings) != n:
        return f"INVALID: Matching size is {len(matchings)}, expected {n}"

    for h, s in matchings:
        # Check bounds
        if not (0 <= h < n) or not (0 <= s < n):
             return f"INVALID: indices out of bounds in pair ({h+1}, {s+1})"

        # Check duplicates
        if h in matched_hospitals:
            return f"INVALID: Hospital {h+1} is matched more than once"
        if s in matched_students:
            return f"INVALID: Student {s+1} is matched more than once"
        
        matched_hospitals.add(h)
        matched_students.add(s)
        student_partner_map[s] = h
        hospital_partner_map[h] = s


    # Stability Check
    student_ranks = []
    for s in range(n):

        rank_map = {hospital: rank for rank, hospital in enumerate(student_prefs[s])}
        student_ranks.append(rank_map)

    for h in range(n):
        current_s = hospital_partner_map[h]
        
        for s_candidate in hospital_prefs[h]:
            
            if s_candidate == current_s:
                break 
            
            s_candidate_current_h = student_partner_map[s_candidate]
            
            rank_of_current_h = student_ranks[s_candidate][s_candidate_current_h]
            rank_of_new_h = student_ranks[s_candidate][h]
            
            if rank_of_new_h < rank_of_current_h:
                return f"UNSTABLE: Blocking pair ({h+1}, {s_candidate+1})"

    # If we pass all checks
    return "VALID STABLE"



def main():
    all_lines = sys.stdin.readlines()

    n, hospital_prefs, student_prefs, remaining_lines = input_parser.parse_input(all_lines)
    matchings = output_parser.parse_output(remaining_lines)

    stable_matching = verify(n, hospital_prefs, student_prefs, matchings)
    print(stable_matching)

    


if __name__ == "__main__":
    main()