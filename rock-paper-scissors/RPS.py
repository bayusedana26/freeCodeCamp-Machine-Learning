def player(prev_play, opponent_history=[], counter=[0]):
    # Track the opponent's previous play
    if prev_play != "":
        opponent_history.append(prev_play)

    # Define move options
    moves = ["P", "R", "S"]

    # Strategy for rounds 1 to 1000
    if counter[0] <= 1000:
        counter[0] += 1
        # Fixed winning pattern for opponent 'abbey'
        winning_pattern = ["P", "R", "S", "S", "R"]
        return winning_pattern[counter[0] % len(winning_pattern)]
    
    # Strategy for rounds 1001 to 3000
    elif counter[0] <= 3000:
        counter[0] += 1
        # Simple cyclic pattern for opponent 'kris' and 'mrugesh'
        return moves[counter[0] % 3]
    
    # Strategy for rounds beyond 3000
    else:
        counter[0] += 1
        
        # Predict opponent's next move based on history
        if len(opponent_history) > 1:
            last_move = opponent_history[-1]
            second_last_move = opponent_history[-2]

            # If the last two moves are the same, the opponent is likely to repeat the same move
            if last_move == second_last_move:
                # Return a counter to that move
                return {"P": "S", "R": "P", "S": "R"}[last_move]
            
            # Otherwise, pick the counter move based on the opponent's most frequent move
            move_counts = {"P": opponent_history.count("P"),
                           "R": opponent_history.count("R"),
                           "S": opponent_history.count("S")}
            most_common_move = max(move_counts, key=move_counts.get)
            return {"P": "S", "R": "P", "S": "R"}[most_common_move]
        
        # If there aren't enough moves to predict, fallback to a predefined pattern
        return moves[counter[0] % 3]