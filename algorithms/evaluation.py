import math

from world.game_state import GameState


def base_evaluation_function(state: GameState) -> float:
    """
    Retorna la evaluación base entregada para desarrollar el punto 4.

    Esta función no forma parte del código que debe modificar el estudiante y
    permite probar Minimax antes de desarrollar la heurística del punto 5.
    """
    if state.is_win():
        return 1000.0
    if state.is_lose():
        return -1000.0
    return float(state.get_score())


def evaluation_function(state: GameState) -> float:
    """
    Evalúa un estado desde la perspectiva del defensor MAX.

    Debe conservar las utilidades terminales de la evaluación base y diseñar
    una valoración no trivial para estados de corte. Minimax y alfa-beta usan
    esta misma función al comparar sus decisiones en el punto 5.

    Tips:
    - Los estados terminales ya se resuelven antes del bloque TODO; diseñe allí
      únicamente la valoración de estados no terminales.
    - Consulte state.defender_position, state.intruder_position,
      state.pending_terminals, state.get_score() y state.get_legal_actions(0).
    - state.layout.distance(start, goal) calcula y almacena en caché la distancia
      real por el mapa respetando los muros.
    - Maneje conjuntos vacíos y distancias infinitas, y mantenga todo estado no
      terminal estrictamente entre -1000 y +1000.
    """
    if state.is_win() or state.is_lose():
        return base_evaluation_function(state)

    def_pos = state.defender_position
    intruder_pos = state.intruder_position
    pending_terminals = state.pending_terminals
    score = state.get_score()
    actions = state.get_legal_actions(0)
            
    dist_def_to_intruder = state.layout.distance(def_pos, intruder_pos)
    
    defensor_score = 10*dist_def_to_intruder

    min_dist_to_goal = float('inf')

    if pending_terminals:
      for terminal in pending_terminals:
        dis = state.layout.distance(def_pos, terminal)
        if dis < min_dist_to_goal:
          min_dist_to_goal = dis
    
    dist_to_goal_score = -10*min_dist_to_goal
    
    terminales_score = -20*len(pending_terminals)
        
    eval = score + defensor_score + dist_to_goal_score + terminales_score 

    if eval > 999.0:
      return 990.0
    if eval < -999.0:
      return -999.0

    return float(eval)
