connections = {}

connections['A'] = [['B', 4], ['C', 2], ['D', 1], ['E', 2]]
connections['B'] = [['A', 4], ['C', 1], ['D', 2], ['E', 3]]
connections['C'] = [['A', 2], ['B', 1], ['D', 3], ['E', 2]]
connections['D'] = [['A', 1], ['B', 2], ['C', 3], ['E', 2]]
connections['E'] = [['A', 2], ['B', 3], ['C', 2], ['D', 2]]

state = ['A','B','C','D','E']


from copy import deepcopy

def evaluate(state, connections):
  num_cities = len(state)
  value = 0
  for i in range(num_cities):
    current_city = state[i]
    next_city = state[(i+1) % num_cities]
    for successor, cost in connections[current_city]:
      if next_city == successor:
        value+=cost
        break
  return value

def generate_successors(state, connections):
  num_cities = len(state)
  successors = []
  for i in range(num_cities-1):
    for j in range(i+1, num_cities):
      new_state = deepcopy(state)
      new_state[i], new_state[j] = new_state[j], new_state[i]
      successors.append((new_state, evaluate(new_state, connections) ,(new_state[i], new_state[j])))
  return sorted(successors, key = lambda x:x[1])

def tabu_test(move, tabu_list):
  a,b = move
  return (a,b) in tabu_list or (b,a) in tabu_list

def tabu_search(state, connections, tabu_tenure, max_iterations):
  current = state
  current_ev = evaluate(current, connections)
  best = current
  best_ev = current_ev
  tabu_list = {}

  for _ in range(max_iterations):
    successors = generate_successors(current, connections)
    non_tabu = [(state, value, move) for state, value, move in successors if not tabu_test(move, tabu_list)]

    if len(non_tabu)==0:
      break

    next, next_ev, move = non_tabu[0]

    if(next_ev < best_ev):
      best = next
      best_ev = next_ev

    current = next
    current_ev = next_ev

    tabu_list = {k:v-1 for k,v in tabu_list.items() if v>1}
    tabu_list[move] = tabu_tenure

  return best+[best[0]], best_ev


tabu_search(state,connections,3,10)