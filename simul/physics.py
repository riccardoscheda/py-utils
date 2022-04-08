def phi(q,p,omega = 1.5):
    """
    The vectorial field which generates the evolution in the pase space
    Parameters:
    ---------------------------------
    q : the generalized coordinate, float
    p : the generalized momenta, float
    omega : frequency, float

    Return the derivative of the potential with respect to q.
    """
    
##################HARMONIC OSCILLATOR
#    return p , -(q-2)*omega**2  
################# DOUBLE WELL POTENTIAL
    a = 1.7
    b = 0.7
    return p, -q


def simplettic(q,p,dt,gamma=0,omega=0.5):
    """
    Simplettic integration method to obtain the evolution of the system
    Parameters:
    ------------------------------------------
    q : the generalized coordinate, float
    dt : the evolution time step, float
    eps : constant which scale the intensity of the white noise csi
    gamma : damping constant (?)

    Returns the evolution of the coordinates q and p

    """

    #evolution of the coordinates q and p
    evoq = q + phi(q,p + dt*phi(q, p)[1])[0]*dt
    evop = p -gamma*p*dt + phi(q,p)[1]*dt 
    return evoq, evop