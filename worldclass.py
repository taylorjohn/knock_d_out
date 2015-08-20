    
class World(object):
    
    def __init__(self):
        
        self.entities = {}
        self.entity_id = 0        
        self.background = pygame.surface.Surface(SCREEN_SIZE).convert()
        # pick background image change with enemy maybe
        background = pygame.image.load("background_mini.png")

        
    def add_entity(self, entity):
        
        self.entities[self.entity_id] = entity
        entity.id = self.entity_id
        self.entity_id += 1
        
    def remove_entity(self, entity):
        
        del self.entities[entity.id]
                
    def get(self, entity_id):
        
        if entity_id in self.entities:
            return self.entities[entity_id]
        else:
            return None
        
    def process(self, time_passed):
                
        time_passed_seconds = time_passed / 1000.0        
        for entity in list(self.entities.values()):
            entity.process(time_passed_seconds)
            
    def render(self, surface):
        
        surface.blit(self.background, (0, 0))
        for entity in self.entities.values():
            entity.render(surface)
            
            
