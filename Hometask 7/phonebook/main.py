import ph_numbers_data as ph_n
import record_phonebook as r_p

my_ph = ph_n.last_names()

r_p.rec_data('phonebook.txt', my_ph)
