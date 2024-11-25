connections = {}

connections['A'] = [['B', 4], ['C', 2], ['D', 1], ['E', 2]]
connections['B'] = [['A', 4], ['C', 1], ['D', 2], ['E', 3]]
connections['C'] = [['A', 2], ['B', 1], ['D', 3], ['E', 2]]
connections['D'] = [['A', 1], ['B', 2], ['C', 3], ['E', 2]]
connections['E'] = [['A', 2], ['B', 3], ['C', 2], ['D', 2]]

state = ['A','B','C','D','E']

from copy import deepcopy  

# Funzione per calcolare il costo di un percorso
def evaluate(state, connections):
    num_cities = len(state)  # Numero totale di città nel percorso.
    value = 0  
    
    # Itera su tutte le città del percorso, includendo il ritorno alla città iniziale.
    for i in range(num_cities):
        current_city = state[i]  # Città corrente.
        next_city = state[(i+1) % num_cities]  # Città successiva (con ritorno alla prima città).
        
        # Trova il costo della connessione tra current_city e next_city.
        for successor, cost in connections[current_city]:
            if next_city == successor:
                value += cost  # Aggiungi il costo al totale.
                break    
    return value  

# Funzione per generare tutti i successori scambiando due città
def generate_successors(state, connections):
    num_cities = len(state)  # Numero totale di città.
    successors = [] 
    
    # Per ogni coppia di città, scambia le posizioni per creare un nuovo percorso.
    for i in range(num_cities - 1):
        for j in range(i + 1, num_cities):
            new_state = deepcopy(state)  # Crea una copia del percorso corrente.
            new_state[i], new_state[j] = new_state[j], new_state[i]  # Scambia due città.
            # Aggiungi il nuovo percorso, il suo costo e la mossa (coppia di città scambiate).
            successors.append((new_state, evaluate(new_state, connections), (new_state[i], new_state[j])))
    
    # Ordina i successori in base al costo, dal più basso al più alto.
    return sorted(successors, key=lambda x: x[1])

# Funzione per verificare se una mossa è nella tabu list
def tabu_test(move, tabu_list):
    a, b = move  # Estrai le città dalla mossa.
    # Controlla se la mossa o il suo inverso è nella tabu list.
    return (a, b) in tabu_list or (b, a) in tabu_list

def tabu_search(state, connections, tabu_tenure, max_iterations):
    current = state  
    current_ev = evaluate(current, connections)  
    best = current  
    best_ev = current_ev  
    tabu_list = {}  
    
    for _ in range(max_iterations):
        # Genera i successori del percorso corrente.
        successors = generate_successors(current, connections)
        # Filtra i successori escludendo quelli vietati dalla tabu list.
        non_tabu = [(state, value, move) for state, value, move in successors if not tabu_test(move, tabu_list)]
        
        # Se non ci sono successori validi, interrompi l'algoritmo.
        if len(non_tabu) == 0:
            break
        
        # Seleziona il successore con il costo più basso tra quelli validi.
        next, next_ev, move = non_tabu[0]
        
        # Aggiorna il miglior percorso trovato se il successore è migliore.
        if next_ev < best_ev:
            best = next
            best_ev = next_ev
        
        # Aggiorna il percorso corrente con il successore selezionato.
        current = next
        current_ev = next_ev
        
        # Aggiorna la tabu list decrementando la durata di ogni mossa e aggiungendo la nuova mossa.
        tabu_list = {key: value - 1 for key, value in tabu_list.items() if value > 1}  # Riduci la durata delle mosse.
        tabu_list[move] = tabu_tenure  # Aggiungi la nuova mossa alla tabu list.
    
    # Ritorna il miglior percorso trovato (chiuso con ritorno alla città iniziale) e il suo costo.
    return (best + [best[0]], best_ev)



tabu_search(state,connections,3,10)