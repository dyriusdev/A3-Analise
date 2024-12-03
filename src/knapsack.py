class Object:

    def __init__(self, name : str, value : int, weight : float, priority : int) -> None:
        self.name : str = name
        self.value : int = value
        self.weight : float = weight
        self.priority : int = priority
        pass
    
    def __repr__(self) -> str:
        return f"Nome : {self.name}, Valor : {self.value}, Peso : {self.weight}, Prioridade : {self.priority}"
    
class Knapsack:

    def __init__(self) -> None:
        pass
    
    def sack(self, n : int, objects : list[Object], space : int) -> tuple[int, list[Object]]:
        def dynamic_programming(i : int, remaining_space : int) -> tuple[int, list[Object]]:
            if i == n or remaining_space == 0:
                return 0, []
            
            current_cargo : Object = objects[i]
            dont_take_value, dont_take_objects = dynamic_programming(i + 1, remaining_space)
            take_value : int = 0
            take_objects : list[Object] = []
            
            if current_cargo.weight <= remaining_space:
                take_value, take_objects = dynamic_programming(i + 1, remaining_space - current_cargo.weight)
                take_value += current_cargo.value + current_cargo.priority
                take_objects = [current_cargo] + take_objects
            
            if take_value > dont_take_value:
                return take_value, take_objects
            return dont_take_value, dont_take_objects
        return dynamic_programming(0, space)
    
    def calculate_weight(self, objects : list[Object], capacity : int) -> tuple[int, list[Object]]:
        n = len(objects)
        pd = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

        for i in range(1, n + 1):
            for c in range(1, capacity + 1):
                if objects[i - 1].weight <= c:
                    pd[i][c] = max(pd[i - 1][c],  pd[i - 1][c - objects[i - 1].weight] + objects[i - 1].value)
                else:
                    pd[i][c] = pd[i - 1][c]
                
        c = capacity
        selected_items : list[Object] = []
        for i in range(n, 0, -1):
            if pd[i][c] != pd[i - 1][c]:
                selected_items.append(objects[i - 1])
                c -= objects[i - 1].weight
        
        return pd[n][capacity], selected_items