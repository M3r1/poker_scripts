def _get_flop_as_array(flop):
    raw_flop_array = flop.split(",")
    return [card.strip() for card in raw_flop_array]

def is_monotone(flop):
    flop_array = _get_flop_as_array(flop)
    
    return len(set(card[1] for card in flop_array)) == 1

def is_two_tone(flop):
    flop_array = _get_flop_as_array(flop)

    suits = [card[1] for card in flop_array]
    return len(set(suits)) == 2 and suits.count(suits[0]) == 2

def is_unpaired_two_tone(flop):
    flop_array = _get_flop_as_array(flop)

    ranks = [card[0] for card in flop_array]
    suits = [card[1] for card in flop_array]
    return len(set(suits)) == 2 and len(set(ranks)) == 3

def is_paired_two_tone(flop):
    flop_array = _get_flop_as_array(flop)

    ranks = [card[0] for card in flop_array]
    suits = [card[1] for card in flop_array]
    return len(set(suits)) == 2 and len(set(ranks)) == 2

def is_rainbow(flop):
    flop_array = _get_flop_as_array(flop)

    return len(set(card[1] for card in flop_array)) == 3

def is_unpaired_rainbow(flop):
    flop_array = _get_flop_as_array(flop)

    ranks = [card[0] for card in flop_array]
    suits = [card[1] for card in flop_array]
    return len(set(suits)) == 3 and len(set(ranks)) == 3

def is_paired_rainbow(flop):
    flop_array = _get_flop_as_array(flop)

    ranks = [card[0] for card in flop_array]
    suits = [card[1] for card in flop_array]
    return len(set(suits)) == 3 and len(set(ranks)) == 2

def is_trips(flop):
    flop_array = _get_flop_as_array(flop)

    ranks = [card[0] for card in flop_array]
    return len(set(ranks)) == 1