class Opponent(GameEntity):
    
    def __init__(self, world, image):
        
        GameEntity.__init__(self, world, "opponent", image)
        
        # Taunt
        tauntone_state = OpponentStateTauntone(self)
        taunttwo_state = OpponentStateTaunttwo(self)
        # Dodge a move left or right
        dodgeleft_state = OpponentStateDodgeleft(self)
        dodgeright_state = OpponentStateDodgeright(self)
        # left or right jab
        jableft_state = OpponentStateJableft(self)
        jabright_state = OpponentStateJabright(self)
        # delayed speed left or right jab
        delayedhookleft_state = OpponentStateDelayedkookleft(self)
        delayedhookright_state = OpponentStatedelayeDhookright(self)
        # left or right hook
        hookleft_state = OpponentStateHookleft(self)
        hookright_state = OpponentStateHookright(self)
        # delayed speed left or right hook
        delayedhookleft_state = OpponentStateDelayedkookleft(self)
        delayedhookright_state = OpponentStateDelayehookright(self)

        bodyblowleft_state = OpponentStateBodyblowleft(self)
        bodyblowright_state = OpponentStateBodyblowright(self)

        block_state = OpponentStateBlock(self)
        duck_state = OpponentStateDuck(self)

        uppercut_state = OpponentStateUppercut(self)
        delayeduppercut_state = OpponentStateDelayeduppercut(self)
        #Opponents special move
        special_state = OpponentStateSpecial(self)

        quickattack_state = OpponentStateQuickattack(self)
        
        self.brain.add_state(exploring_state)
        self.brain.add_state(seeking_state)
        self.brain.add_state(leveling_state)
        self.brain.add_state(delivering_state)
        self.brain.add_state(hunting_state)
        
    def render(self, surface):
        
        GameEntity.render(self, surface)
