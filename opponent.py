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
        delayedhookleft_state = OpponentStateDelayedhookleft(self)
        delayedhookright_state = OpponentStatedelayeDhookright(self)
        # left or right hook
        hookleft_state = OpponentStateHookleft(self)
        hookright_state = OpponentStateHookright(self)
        # delayed speed left or right hook
        delayedhookleft_state = OpponentStateDelayedkookleft(self)
        delayedhookright_state = OpponentStateDelayehookright(self)
        # left or right body blow
        bodyblowleft_state = OpponentStateBodyblowleft(self)
        bodyblowright_state = OpponentStateBodyblowright(self)
        # Block a move or Duck out of the way
        block_state = OpponentStateBlock(self)
        duck_state = OpponentStateDuck(self)
        # Uppercut
        uppercut_state = OpponentStateUppercut(self)
        delayeduppercut_state = OpponentStateDelayeduppercut(self)
        #Opponents special move
        special_state = OpponentStateSpecial(self)
        #Opponents quick attack
        quickattack_state = OpponentStateQuickattack(self)
        
        self.brain.add_state(tauntone_state)
        self.brain.add_state(taunttwo_state))
        self.brain.add_state(dodgeleft_state)
        self.brain.add_state(dodgeright_state)
        self.brain.add_state(jableft_state)
        self.brain.add_state(jabright_state)
        self.brain.add_state(delayedhookleft_state)
        self.brain.add_state(delayedhookright_state)
        self.brain.add_state(hookleft_state)
        self.brain.add_state(hookright_state)
        self.brain.add_state(delayedhookleft_state)
        self.brain.add_state(delayedhookright_state)
        self.brain.add_state(bodyblowleft_state)
        self.brain.add_state(bodyblowright_state)
        self.brain.add_state(block_state)
        self.brain.add_state(duck_state)
        self.brain.add_state(uppercut_state)
        self.brain.add_state(delayeduppercut_state)
        self.brain.add_state(special_state)
        self.brain.add_state(quickattack_state)
        
    def render(self, surface):
        
        GameEntity.render(self, surface)
