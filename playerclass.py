class Player(GameEntity):
    
    def __init__(self, world, image):
        
        GameEntity.__init__(self, world, "player", image)
        
        exploring_state = PlayerStateExploring(self)
        seeking_state = PlayerStateSeeking(self)
        leveling_state = PlayerStateLeveling(self)
        delivering_state = PlayerStateDelivering(self)
        hunting_state = PlayerStateHunting(self)
        
        self.brain.add_state(exploring_state)
        self.brain.add_state(seeking_state)
        self.brain.add_state(leveling_state)
        self.brain.add_state(delivering_state)
        self.brain.add_state(hunting_state)
        
    def render(self, surface):
        
        GameEntity.render(self, surface)
