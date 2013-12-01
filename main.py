from path_util import *
from test_util import *

my_cost_map = make_grid(40,20,1) #default cost of 1
start_pos = generate_random_pos(40,20)
end_pos = generate_random_pos(40,20)

generate_random_cost_map(my_cost_map, -1,3)
replace_in_map(my_cost_map, 0, 1)
replace_in_map(my_cost_map, 2, 1)
replace_in_map(my_cost_map, 3, 1)
start_pos = generate_random_pos(40,20)
end_pos = generate_random_pos(40,20)

my_text_map = create_text_map_from_cost_map(my_cost_map)
my_text_map[start_pos[0]][start_pos[1]] = 'A'
my_text_map[end_pos[0]][end_pos[1]] = 'B'
pretty_print_map(my_text_map)

