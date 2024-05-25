from helpers import flopzilla_helper
from combos import combo_pool

FLOPZILA_RANGE = "[40]AQs[/40],[79]AJs[/79],[91]ATs[/91],[100]A9s[/100],[93]A8s[/93],[72]A7s[/72],[70]A6s[/70],[71]A5s[/71],[64]A4s[/64],[71]A3s[/71],[71]A2s[/71],[21]AKo[/21],[92]KQs[/92],[91]KJs[/91],[100]KTs[/100],[82]K9s[/82],[98]K8s[/98],[67]K7s[/67],[68]K6s[/68],[44]K5s[/44],[34]K4s[/34],[14]K3s[/14],[27]K2s[/27],[100]AQo[/100],[64]KQo[/64],[32]QQ[/32],[79]QJs[/79],[93]QTs[/93],[58]Q9s[/58],[50]Q8s[/50],[9]Q7s[/9],[45]Q6s[/45],[8]Q5s[/8],[94]AJo[/94],[34]KJo[/34],[7]QJo[/7],[92]JJ[/92],[97]JTs[/97],[86]J9s[/86],[79]J8s[/79],[48]ATo[/48],[4]JTo[/4],[99]TT[/99],[89]T9s[/89],[93]T8s[/93],[100]T7s[/100],[100]99[/100],[93]98s[/93],[93]97s[/93],[88]96s[/88],[100]88[/100],[76]87s[/76],[90]86s[/90],[19]85s[/19],[100]77[/100],[72]76s[/72],[79]75s[/79],[97]66[/97],[76]65s[/76],[76]64s[/76],[97]55[/97],[87]54s[/87],[92]53s[/92],[16]52s[/16],[100]44[/100],[96]43s[/96],[6]42s[/6],[100]33[/100],[100]22[/100]"
COMBOS_TO_GENERATE = 10

range_weight_dict = flopzilla_helper.get_range_weight_dict_from_flopzilla_range(FLOPZILA_RANGE)

for combo in combo_pool.get_unique_combos_from_combo_pool(range_weight_dict, COMBOS_TO_GENERATE):
    print(combo)