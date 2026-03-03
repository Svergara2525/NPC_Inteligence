class agente():
    def __init__(self, id, position, action):
        self.id = id
        self.position = position
        self.action = action
    
    def update_position(self, new_position):
        self.position = new_position
        