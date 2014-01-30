#import vector

class Boid(object):
    """Birdlike object for flocking simulations"""
    def __init__(self,ident,r,v,a,vmax):
        self.ident = ident
        self.r = r
        self.v = v
        self.a = a
        self.vmax = vmax
    
    def __str__(self):
        s = 'Boid: %i ' % self.ident       
        return s

    def checkvel(self):
        """ Limits boid speed to some vmax"""
        if self.v.mag() > self.vmax:
            self.v = self.v.scalarmult(self.vmax/self.v.mag())

    def approach_COM(self, COM,strength):
        """ Tells boid to approach centre of mass, given by vector COM"""
        sep = self.r.subtract(COM)
        if sep.mag() > 0.0:
            sep = sep.scalarmult(1.0/sep.mag())
        self.v = self.v.subtract(sep.scalarmult(strength))
        self.checkvel()

    def avoid_collisions(self,obstacle,strength):
        """Boid moves away from position vector named obstacle"""
        sep = self.r.subtract(obstacle)
        if sep.mag() > 0.0:
            sep = sep.scalarmult(1.0/sep.mag())
        self.v = self.v.add(sep.scalarmult(strength))
        self.checkvel()

    def match_velocities(self, velocity,strength):
        """Boid will match input velocity vector"""
        if velocity.mag() > 0.0:
            sep = velocity.scalarmult(velocity.mag())
        self.v = self.v.add(sep.scalarmult(strength))
        self.checkvel()

    def move(self,dt):
        """ Updates a boid's position """
        self.r = self.r.add(self.v.scalarmult(dt))    

    
    

    
