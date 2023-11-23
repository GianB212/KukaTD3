import numpy as np
import random

class FormiguinhaPCartesiana1_0:
    def __init__(self):
        self.high = 1
        self.low = -1
        self.state_dim = 8
        self.action_dim = 2
        self.name = 'FormiguinhaPCartesiana-v1-0'
        self.posx = 0
        self.posy = 0
        self.x0 = 0
        self.y0 = 0
        self.z0 = 0
        self.vx0 = 0
        self.vy0 = 0
        self.vz0 = 0
        self.targetx, self.targety = self.calculaTarget()
        self.distancia = self.calculaDistancia()
        self.dt = 1
        self.t = 0

    def calculaTarget(self):
        tempo_queda = (self.vz0+np.sqrt(self.vz0**2+2*9.8*self.z0))/9.8
        self.targetx = self.x0 + tempo_queda*self.vx0
        self.targety = self.y0 + tempo_queda*self.vy0
        return self.targetx, self.targety

    def calculaDistancia(self):
        self.distancia = np.sqrt((self.posx-self.targetx)**2 + (self.posy-self.targety)**2)
        return self.distancia

    def calculaReward(self):
        return -self.distancia
    
    def reset(self):
        self.posx = random.uniform(-1.8,1.8)
        self.posy = random.uniform(-1.8,1.8)
        self.x0 = random.uniform(-1.8,1.8)
        self.y0 = random.uniform(-1.8,1.8)
        self.z0 = random.uniform(1, 1.8)
        self.vx0 = random.uniform(-1.5,1.5)
        self.vy0 = random.uniform(-1.5,1.5)
        self.vz0 = random.uniform(-1.5,1.5)
        self.targetx, self.targety = self.calculaTarget()
        self.t = 0
        return (self.posx, self.posy, self.x0, self.y0, self.z0, self.vx0, self.vy0, self.vz0)

    def step(self, action):
        self.posx += 0.3*action[0]
        self.posy += 0.3*action[1]
        self.distancia = self.calculaDistancia()
        self.t += self.dt
        reward = self.calculaReward()
        if self.distancia < 0.2:
            reward += 20
            done = True
        elif self.t >= 50:
            done = True
        else:
            done = False
        return (self.posx, self.posy, self.x0, self.y0, self.z0, self.vx0, self.vy0, self.vz0), reward, done
    
class FormiguinhaPCartesiana1_1:
    def __init__(self):
        self.high = 1
        self.low = -1
        self.state_dim = 8
        self.action_dim = 2
        self.name = 'FormiguinhaPCartesiana-v1-1'
        self.posx = 0
        self.posy = 0
        self.x0 = 0
        self.y0 = 0
        self.z0 = 0
        self.vx0 = 0
        self.vy0 = 0
        self.vz0 = 0
        self.targetx, self.targety = self.calculaTarget()
        self.distancia = self.calculaDistancia()
        self.dt = 1
        self.t = 0

    def calculaTarget(self):
        tempo_queda = (self.vz0+np.sqrt(self.vz0**2+2*9.8*self.z0))/9.8
        self.targetx = self.x0 + tempo_queda*self.vx0
        self.targety = self.y0 + tempo_queda*self.vy0
        return self.targetx, self.targety

    def calculaDistancia(self):
        self.distancia = np.sqrt((self.posx-self.targetx)**2 + (self.posy-self.targety)**2)
        return self.distancia

    def calculaReward(self):
        return -self.distancia-1
    
    def reset(self):
        self.posx = random.uniform(-1.8,1.8)
        self.posy = random.uniform(-1.8,1.8)
        self.x0 = random.uniform(-1.8,1.8)
        self.y0 = random.uniform(-1.8,1.8)
        self.z0 = random.uniform(1, 1.8)
        self.vx0 = random.uniform(-1.5,1.5)
        self.vy0 = random.uniform(-1.5,1.5)
        self.vz0 = random.uniform(-1.5,1.5)
        self.targetx, self.targety = self.calculaTarget()
        self.t = 0
        return (self.posx, self.posy, self.x0, self.y0, self.z0, self.vx0, self.vy0, self.vz0)

    def step(self, action):
        self.posx += 0.3*action[0]
        self.posy += 0.3*action[1]
        self.distancia = self.calculaDistancia()
        self.t += self.dt
        reward = self.calculaReward()
        if self.distancia < 0.1:
            reward += 50
            done = True
        elif self.t >= 50:
            done = True
        else:
            done = False
        return (self.posx, self.posy, self.x0, self.y0, self.z0, self.vx0, self.vy0, self.vz0), reward, done

class FormiguinhaPBraco1_0:
    def __init__(self):
        self.high = 1
        self.low = -1
        self.state_dim = 8
        self.action_dim = 2
        self.name = 'FormiguinhaPBraço-v1-0'
        self.theta1 = 0
        self.theta2 = 0
        self.x0 = 0
        self.y0 = 0
        self.z0 = 0
        self.vx0 = 0
        self.vy0 = 0
        self.vz0 = 0
        self.L1 = 1
        self.L2 = 1
        self.Cx = 0
        self.Cy = 0
        self.posx, self.posy = self.calculaPosicao()
        self.targetx, self.targety = self.calculaTarget()
        self.distancia = self.calculaDistancia()
        self.dt = 1
        self.t = 0

    def calculaPosicao(self):
        self.posx = self.Cx + self.L1*np.cos(self.theta1) + self.L2*np.cos(self.theta1+self.theta2)
        self.posy = self.Cy + self.L1*np.sin(self.theta1) + self.L2*np.sin(self.theta1+self.theta2)
        return self.posx, self.posy

    def calculaTarget(self):
        tempo_queda = (self.vz0+np.sqrt(self.vz0**2+2*9.8*self.z0))/9.8
        self.targetx = self.x0 + tempo_queda*self.vx0
        self.targety = self.y0 + tempo_queda*self.vy0
        return self.targetx, self.targety

    def calculaDistancia(self):
        self.distancia = np.sqrt((self.posx-self.targetx)**2 + (self.posy-self.targety)**2)
        return self.distancia

    def calculaReward(self):
        return -self.distancia
    
    def reset(self):
        self.theta1 = random.uniform(-np.pi,np.pi)
        self.theta2 = random.uniform(-np.pi,np.pi)
        self.posx, self.posy = self.calculaPosicao()
        self.x0 = random.uniform(-0.5,0.5)
        self.y0 = random.uniform(-0.5,0.5)
        self.z0 = random.uniform(1.2, 1.8)
        self.vx0 = random.uniform(-1.5,1.5)
        self.vy0 = random.uniform(-1.5,1.5)
        self.vz0 = random.uniform(-0.2,1)
        self.targetx, self.targety = self.calculaTarget()
        self.t = 0
        return (self.posx, self.posy, self.x0, self.y0, self.z0, self.vx0, self.vy0, self.vz0)

    def step(self, action):
        self.theta1 += 0.3*action[0]
        self.theta2 += 0.3*action[1]
        self.posx, self.posy = self.calculaPosicao()
        self.distancia = self.calculaDistancia()
        self.t += self.dt
        reward = self.calculaReward()
        if self.distancia < 0.2:
            reward += 20
            done = True
        elif self.t >= 50:
            done = True
        else:
            done = False
        return (self.posx, self.posy, self.x0, self.y0, self.z0, self.vx0, self.vy0, self.vz0), reward, done
    
class FormiguinhaPBraco2_0:
    def __init__(self):
        self.high = 1
        self.low = -1
        self.state_dim = 8
        self.action_dim = 2
        self.name = 'FormiguinhaPBraço-v2-0'
        self.theta1 = 0
        self.theta2 = 0
        self.x0 = 0
        self.y0 = 0
        self.z0 = 0
        self.vx0 = 0
        self.vy0 = 0
        self.vz0 = 0
        self.L1 = 1
        self.L2 = 1
        self.Cx = 0
        self.Cy = 0
        self.posx, self.posy = self.calculaPosicao()
        self.targetx, self.targety = self.calculaTarget()
        self.distancia = self.calculaDistancia()
        self.dt = 1
        self.t = 0

    def calculaPosicao(self):
        self.posx = self.Cx + self.L1*np.cos(self.theta1) + self.L2*np.cos(self.theta1+self.theta2)
        self.posy = self.Cy + self.L1*np.sin(self.theta1) + self.L2*np.sin(self.theta1+self.theta2)
        return self.posx, self.posy

    def calculaTarget(self):
        tempo_queda = (self.vz0+np.sqrt(self.vz0**2+2*9.8*self.z0))/9.8
        self.targetx = self.x0 + tempo_queda*self.vx0
        self.targety = self.y0 + tempo_queda*self.vy0
        return self.targetx, self.targety

    def calculaDistancia(self):
        self.distancia = np.sqrt((self.posx-self.targetx)**2 + (self.posy-self.targety)**2)
        return self.distancia

    def calculaReward(self):
        return -self.distancia
    
    def reset(self):
        self.theta1 = random.uniform(-np.pi,np.pi)
        self.theta2 = random.uniform(-np.pi,np.pi)
        self.posx, self.posy = self.calculaPosicao()
        self.x0 = random.uniform(-0.5,0.5)
        self.y0 = random.uniform(-0.5,0.5)
        self.z0 = random.uniform(1.2, 1.8)
        self.vx0 = random.uniform(-1.5,1.5)
        self.vy0 = random.uniform(-1.5,1.5)
        self.vz0 = random.uniform(-0.2,1)
        self.targetx, self.targety = self.calculaTarget()
        self.t = 0
        return (self.theta1, self.theta2, self.x0, self.y0, self.z0, self.vx0, self.vy0, self.vz0)

    def step(self, action):
        self.theta1 += 0.3*action[0]
        self.theta2 += 0.3*action[1]
        self.posx, self.posy = self.calculaPosicao()
        self.distancia = self.calculaDistancia()
        self.t += self.dt
        reward = self.calculaReward()
        if self.distancia < 0.2:
            reward += 20
            done = True
        elif self.t >= 50:
            done = True
        else:
            done = False
        return (self.theta1, self.theta2, self.x0, self.y0, self.z0, self.vx0, self.vy0, self.vz0), reward, done
    
class FormiguinhaPBraco2_1:
    def __init__(self):
        self.high = 1
        self.low = -1
        self.state_dim = 8
        self.action_dim = 2
        self.name = 'FormiguinhaPBraço-v2-1'
        self.theta1 = 0
        self.theta2 = 0
        self.x0 = 0
        self.y0 = 0
        self.z0 = 0
        self.vx0 = 0
        self.vy0 = 0
        self.vz0 = 0
        self.L1 = 1
        self.L2 = 1
        self.Cx = 0
        self.Cy = 0
        self.posx, self.posy = self.calculaPosicao()
        self.targetx, self.targety = self.calculaTarget()
        self.distancia = self.calculaDistancia()
        self.dt = 1
        self.t = 0

    def calculaPosicao(self):
        self.posx = self.Cx + self.L1*np.cos(self.theta1) + self.L2*np.cos(self.theta1+self.theta2)
        self.posy = self.Cy + self.L1*np.sin(self.theta1) + self.L2*np.sin(self.theta1+self.theta2)
        return self.posx, self.posy

    def calculaTarget(self):
        tempo_queda = (self.vz0+np.sqrt(self.vz0**2+2*9.8*self.z0))/9.8
        self.targetx = self.x0 + tempo_queda*self.vx0
        self.targety = self.y0 + tempo_queda*self.vy0
        return self.targetx, self.targety

    def calculaDistancia(self):
        self.distancia = np.sqrt((self.posx-self.targetx)**2 + (self.posy-self.targety)**2)
        return self.distancia

    def calculaReward(self):
        return -self.distancia -0.1
    
    def reset(self):
        self.theta1 = random.uniform(-np.pi,np.pi)
        self.theta2 = random.uniform(-np.pi,np.pi)
        self.posx, self.posy = self.calculaPosicao()
        self.x0 = random.uniform(-0.5,0.5)
        self.y0 = random.uniform(-0.5,0.5)
        self.z0 = random.uniform(1.2, 1.8)
        self.vx0 = random.uniform(-1.5,1.5)
        self.vy0 = random.uniform(-1.5,1.5)
        self.vz0 = random.uniform(-0.2,1)
        self.targetx, self.targety = self.calculaTarget()
        self.t = 0
        return (self.theta1, self.theta2, self.x0, self.y0, self.z0, self.vx0, self.vy0, self.vz0)

    def step(self, action):
        self.theta1 += 0.3*action[0]
        self.theta2 += 0.3*action[1]
        self.posx, self.posy = self.calculaPosicao()
        self.distancia = self.calculaDistancia()
        self.t += self.dt
        reward = self.calculaReward()
        if self.distancia < 0.2:
            reward += 20
            done = True
        elif self.t >= 50:
            done = True
        else:
            done = False
        return (self.theta1, self.theta2, self.x0, self.y0, self.z0, self.vx0, self.vy0, self.vz0), reward, done

class FormiguinhaPBraco3_0:
    def __init__(self):
        self.high = 1
        self.low = -1
        self.state_dim = 10
        self.action_dim = 2
        self.name = 'FormiguinhaPBraço-v3-0'
        self.theta1 = 0
        self.theta2 = 0
        self.x0 = 0
        self.y0 = 0
        self.z0 = 0
        self.vx0 = 0
        self.vy0 = 0
        self.vz0 = 0
        self.L1 = 1.5
        self.L2 = 1.5
        self.Cx = 0
        self.Cy = 0
        self.posx, self.posy = self.calculaPosicao()
        self.targetx, self.targety = self.calculaTarget()
        self.distancia = self.calculaDistancia()
        self.dt = 1
        self.t = 0

    def calculaPosicao(self):
        self.posx = self.Cx + self.L1*np.cos(self.theta1) + self.L2*np.cos(self.theta1+self.theta2)
        self.posy = self.Cy + self.L1*np.sin(self.theta1) + self.L2*np.sin(self.theta1+self.theta2)
        return self.posx, self.posy

    def calculaTarget(self):
        tempo_queda = (self.vz0+np.sqrt(self.vz0**2+2*9.8*self.z0))/9.8
        self.targetx = self.x0 + tempo_queda*self.vx0
        self.targety = self.y0 + tempo_queda*self.vy0
        return self.targetx, self.targety

    def calculaDistancia(self):
        self.distancia = np.sqrt((self.posx-self.targetx)**2 + (self.posy-self.targety)**2)
        return self.distancia

    def calculaReward(self):
        return -self.distancia-0.8
    
    def reset(self):
        self.theta1 = random.uniform(-np.pi,np.pi)
        self.theta2 = random.uniform(-np.pi,np.pi)
        self.posx, self.posy = self.calculaPosicao()
        self.x0 = random.uniform(-1.8,1.8)
        self.y0 = random.uniform(-1.8,1.8)
        self.z0 = random.uniform(1, 1.8)
        self.vx0 = random.uniform(-1.5,1.5)
        self.vy0 = random.uniform(-1.5,1.5)
        self.vz0 = random.uniform(-1.5,1.5)
        self.targetx, self.targety = self.calculaTarget()
        self.t = 0
        return (self.posx, self.posy, self.theta1, self.theta2, self.x0, self.y0, self.z0, self.vx0, self.vy0, self.vz0)

    def step(self, action):
        self.theta1 += 0.3*action[0]
        self.theta2 += 0.3*action[1]
        self.posx, self.posy = self.calculaPosicao()
        self.distancia = self.calculaDistancia()
        self.t += self.dt
        reward = self.calculaReward()
        if self.distancia < 0.2:
            reward += 50
            done = True
        elif self.t >= 50:
            done = True
        else:
            done = False
        return (self.posx, self.posy, self.theta1, self.theta2, self.x0, self.y0, self.z0, self.vx0, self.vy0, self.vz0), reward, done

class FormiguinhaPBraco3_1:
    def __init__(self):
        self.high = 1
        self.low = -1
        self.state_dim = 10
        self.action_dim = 2
        self.name = 'FormiguinhaPBraço-v3-1'
        self.theta1 = 0
        self.theta2 = 0
        self.x0 = 0
        self.y0 = 0
        self.z0 = 0
        self.vx0 = 0
        self.vy0 = 0
        self.vz0 = 0
        self.L1 = 1
        self.L2 = 1
        self.Cx = 0
        self.Cy = 0
        self.posx, self.posy = self.calculaPosicao()
        self.targetx, self.targety = self.calculaTarget()
        self.distancia = self.calculaDistancia()
        self.dt = 1
        self.t = 0

    def calculaPosicao(self):
        self.posx = self.Cx + self.L1*np.cos(self.theta1) + self.L2*np.cos(self.theta1+self.theta2)
        self.posy = self.Cy + self.L1*np.sin(self.theta1) + self.L2*np.sin(self.theta1+self.theta2)
        return self.posx, self.posy

    def calculaTarget(self):
        tempo_queda = (self.vz0+np.sqrt(self.vz0**2+2*9.8*self.z0))/9.8
        self.targetx = self.x0 + tempo_queda*self.vx0
        self.targety = self.y0 + tempo_queda*self.vy0
        return self.targetx, self.targety

    def calculaDistancia(self):
        self.distancia = np.sqrt((self.posx-self.targetx)**2 + (self.posy-self.targety)**2)
        return self.distancia

    def calculaReward(self):
        return -self.distancia-0.1
    
    def reset(self):
        self.theta1 = random.uniform(-np.pi,np.pi)
        self.theta2 = random.uniform(-np.pi,np.pi)
        self.posx, self.posy = self.calculaPosicao()
        self.x0 = random.uniform(-0.5,0.5)
        self.y0 = random.uniform(-0.5,0.5)
        self.z0 = random.uniform(1.2, 1.8)
        self.vx0 = random.uniform(-1.5,1.5)
        self.vy0 = random.uniform(-1.5,1.5)
        self.vz0 = random.uniform(-0.2,1)
        self.targetx, self.targety = self.calculaTarget()
        self.t = 0
        return (self.posx, self.posy, self.theta1, self.theta2, self.x0, self.y0, self.z0, self.vx0, self.vy0, self.vz0)

    def step(self, action):
        self.theta1 += 0.3*action[0]
        self.theta2 += 0.3*action[1]
        self.posx, self.posy = self.calculaPosicao()
        self.distancia = self.calculaDistancia()
        self.t += self.dt
        reward = self.calculaReward()
        if self.distancia < 0.2:
            reward += 20
            done = True
        elif self.t >= 50:
            done = True
        else:
            done = False
        return (self.posx, self.posy, self.theta1, self.theta2, self.x0, self.y0, self.z0, self.vx0, self.vy0, self.vz0), reward, done
    
class FormiguinhaPBraco3_2:
    def __init__(self):
        self.high = 1
        self.low = -1
        self.state_dim = 10
        self.action_dim = 2
        self.name = 'FormiguinhaPBraço-v3-2'
        self.theta1 = 0
        self.theta2 = 0
        self.x0 = 0
        self.y0 = 0
        self.z0 = 0
        self.vx0 = 0
        self.vy0 = 0
        self.vz0 = 0
        self.L1 = 1
        self.L2 = 1
        self.Cx = 0
        self.Cy = 0
        self.posx, self.posy = self.calculaPosicao()
        self.targetx, self.targety = self.calculaTarget()
        self.distancia = self.calculaDistancia()
        self.dt = 1
        self.t = 0

    def calculaPosicao(self):
        self.posx = self.Cx + self.L1*np.cos(self.theta1) + self.L2*np.cos(self.theta1+self.theta2)
        self.posy = self.Cy + self.L1*np.sin(self.theta1) + self.L2*np.sin(self.theta1+self.theta2)
        return self.posx, self.posy

    def calculaTarget(self):
        tempo_queda = (self.vz0+np.sqrt(self.vz0**2+2*9.8*self.z0))/9.8
        self.targetx = self.x0 + tempo_queda*self.vx0
        self.targety = self.y0 + tempo_queda*self.vy0
        return self.targetx, self.targety

    def calculaDistancia(self):
        self.distancia = np.sqrt((self.posx-self.targetx)**2 + (self.posy-self.targety)**2)
        return self.distancia

    def calculaReward(self):
        return min(0.2/self.distancia,1) - 5.1*self.distancia
    
    def reset(self):
        self.theta1 = random.uniform(-np.pi,np.pi)
        self.theta2 = random.uniform(-np.pi,np.pi)
        self.posx, self.posy = self.calculaPosicao()
        self.x0 = random.uniform(-0.5,0.5)
        self.y0 = random.uniform(-0.5,0.5)
        self.z0 = random.uniform(1.2, 1.8)
        self.vx0 = random.uniform(-1.5,1.5)
        self.vy0 = random.uniform(-1.5,1.5)
        self.vz0 = random.uniform(-0.2,1)
        self.targetx, self.targety = self.calculaTarget()
        self.t = 0
        return (self.posx, self.posy, self.theta1, self.theta2, self.x0, self.y0, self.z0, self.vx0, self.vy0, self.vz0)

    def step(self, action):
        self.theta1 += 0.3*action[0]
        self.theta2 += 0.3*action[1]
        self.posx, self.posy = self.calculaPosicao()
        self.distancia = self.calculaDistancia()
        self.t += self.dt
        reward = self.calculaReward()
        if self.distancia < 0.2:
            reward += 50
            done = True
        elif self.t >= 50:
            done = True
        else:
            done = False
        return (self.posx, self.posy, self.theta1, self.theta2, self.x0, self.y0, self.z0, self.vx0, self.vy0, self.vz0), reward, done

class FormiguinhaPCartesiana2_1:
    def __init__(self):
        self.high = 1
        self.low = -1
        self.state_dim = 8
        self.action_dim = 2
        self.name = 'FormiguinhaPCartesiana-v2-1'
        self.posx = 0
        self.posy = 0
        self.x0 = 0
        self.y0 = 0
        self.z0 = 0
        self.vx0 = 0
        self.vy0 = 0
        self.vz0 = 0
        self.targetx, self.targety = self.calculaTarget()
        self.distancia = self.calculaDistancia()
        self.dt = 1
        self.t = 0

    def calculaTarget(self):
        tempo_queda = (self.vz0+np.sqrt(self.vz0**2+2*9.8*self.z0))/9.8
        self.targetx = self.x0 + tempo_queda*self.vx0
        self.targety = self.y0 + tempo_queda*self.vy0
        return self.targetx, self.targety

    def calculaDistancia(self):
        self.distancia = np.sqrt((self.posx-self.targetx)**2 + (self.posy-self.targety)**2)
        return self.distancia

    def calculaReward(self):
        return -self.distancia-1
    
    def reset(self):
        self.posx = random.uniform(-1.8,1.8)
        self.posy = random.uniform(-1.8,1.8)
        self.x0 = random.uniform(-1.8,1.8)
        self.y0 = random.uniform(-1.8,1.8)
        self.z0 = random.uniform(1, 1.8)
        self.vx0 = random.uniform(-1.5,1.5)
        self.vy0 = random.uniform(-1.5,1.5)
        self.vz0 = random.uniform(-1.5,1.5)
        self.targetx, self.targety = self.calculaTarget()
        self.t = 0
        return (self.posx, self.posy, self.x0, self.y0, self.z0, self.vx0, self.vy0, self.vz0)

    def step(self, action):
        max = np.sqrt(1+(np.min([action[1]/action[0],action[0]/action[1]]))**2)
        self.posx += 0.3*action[0]/max
        self.posy += 0.3*action[1]/max
        self.distancia = self.calculaDistancia()
        self.t += self.dt
        reward = self.calculaReward()
        if self.distancia < 0.1:
            reward += 50
            done = True
        elif self.t >= 50:
            done = True
        else:
            done = False
        return (self.posx, self.posy, self.x0, self.y0, self.z0, self.vx0, self.vy0, self.vz0), reward, done

class FormiguinhaPCartesiana4_1:
    def __init__(self):
        self.high = 1
        self.low = -1
        self.state_dim = 8
        self.action_dim = 2
        self.name = 'FormiguinhaPCartesiana-v4-1'
        self.posx = 0
        self.posy = 0
        self.x0 = 0
        self.y0 = 0
        self.z0 = 0
        self.vx0 = 0
        self.vy0 = 0
        self.vz0 = 0
        self.targetx, self.targety = self.calculaTarget()
        self.distancia = self.calculaDistancia()
        self.dt = 1
        self.t = 0

    def calculaTarget(self):
        tempo_queda = (self.vz0+np.sqrt(self.vz0**2+2*9.8*self.z0))/9.8
        self.targetx = self.x0 + tempo_queda*self.vx0
        self.targety = self.y0 + tempo_queda*self.vy0
        return self.targetx, self.targety

    def calculaDistancia(self):
        self.distancia = np.sqrt((self.posx-self.targetx)**2 + (self.posy-self.targety)**2)
        return self.distancia

    def calculaReward(self):
        return -self.distancia-0.8
    
    def reset(self):
        self.posx = random.uniform(-1.8,1.8)
        self.posy = random.uniform(-1.8,1.8)
        self.x0 = random.uniform(-1.8,1.8)
        self.y0 = random.uniform(-1.8,1.8)
        self.z0 = random.uniform(1, 1.8)
        self.vx0 = random.uniform(-1.5,1.5)
        self.vy0 = random.uniform(-1.5,1.5)
        self.vz0 = random.uniform(-1.5,1.5)
        self.targetx, self.targety = self.calculaTarget()
        self.t = 0
        return (self.posx, self.posy, self.x0, self.y0, self.z0, self.vx0, self.vy0, self.vz0)

    def step(self, action):
        max = np.sqrt(1+(np.min([action[1]/action[0],action[0]/action[1]]))**2)
        self.posx += 0.3*action[0]/max
        self.posy += 0.3*action[1]/max
        self.distancia = self.calculaDistancia()
        self.t += self.dt
        reward = self.calculaReward()
        if self.distancia < 0.1:
            reward += 50
            done = True
        elif self.t >= 50:
            done = True
        else:
            done = False
        return (self.posx, self.posy, self.x0, self.y0, self.z0, self.vx0, self.vy0, self.vz0), reward, done

class FormiguinhaPBraco5_0:
    def __init__(self):
        self.high = 1
        self.low = -1
        self.state_dim = 10
        self.action_dim = 2
        self.name = 'FormiguinhaPBraço-v5-0'
        self.theta1 = 0
        self.theta2 = 0
        self.omega1 = 0
        self.omega2 = 0
        self.x0 = 0
        self.y0 = 0
        self.z0 = 0
        self.vx0 = 0
        self.vy0 = 0
        self.vz0 = 0
        self.L = 1.5
        self.Cx = 0
        self.Cy = 0
        self.posx, self.posy = self.calculaPosicao()
        self.targetx, self.targety = self.calculaTarget()
        self.distancia = self.calculaDistancia()
        self.dt = 1
        self.t = 0

    def calculaPosicao(self):
        self.posx = self.Cx + 2*self.L*np.cos(self.theta2)*np.cos(self.theta1)
        self.posy = self.Cy + 2*self.L*np.cos(self.theta2)*np.sin(self.theta1)
        return self.posx, self.posy

    def calculaTarget(self):
        tempo_queda = (self.vz0+np.sqrt(self.vz0**2+2*9.8*self.z0))/9.8
        self.targetx = self.x0 + tempo_queda*self.vx0
        self.targety = self.y0 + tempo_queda*self.vy0
        return self.targetx, self.targety

    def calculaDistancia(self):
        self.distancia = np.sqrt((self.posx-self.targetx)**2 + (self.posy-self.targety)**2)
        return self.distancia

    def calculaReward(self):
        return -self.distancia -0.5
    
    def reset(self):
        self.theta1 = random.uniform(-np.pi,np.pi)
        self.theta2 = random.uniform(0,np.pi/2)
        self.omega1 = 0
        self.omega2 = 0
        self.posx, self.posy = self.calculaPosicao()
        self.x0 = random.uniform(-1.5,1.5)
        self.y0 = random.uniform(-1.5,1.5)
        self.z0 = random.uniform(0, 2)
        self.vx0 = random.uniform(-1.5,1.5)
        self.vy0 = random.uniform(-1.5,1.5)
        self.vz0 = random.uniform(-1.5,1.5)
        self.targetx, self.targety = self.calculaTarget()
        self.t = 0
        return (self.theta1, self.theta2, self.omega1, self.omega2, self.x0, self.y0, self.z0, self.vx0, self.vy0, self.vz0)

    def step(self, action):
        done = False
        self.theta1 += 0.3*action[0]
        self.theta2 += 0.3*action[1]
        self.posx, self.posy = self.calculaPosicao()
        self.distancia = self.calculaDistancia()
        self.t += self.dt
        reward = self.calculaReward()
        reward -= (self.omega1 - 0.3*action[0])**2 + (self.omega2 - 0.3*action[1])**2
        self.omega1, self.omega2 = action[0], action[1]
        if self.theta1 <= -np.pi*19/18 or self.theta1 >= np.pi*19/18:
            reward -= 200
            done = True
        if self.theta2 <= 0 or self.theta2 >= np.pi/2:
            reward -= 200
            done = True
        if self.distancia < 0.2:
            reward += 100
            done = True
        elif self.t >= 50:
            done = True
        return (self.theta1, self.theta2, self.omega1, self.omega2, self.x0, self.y0, self.z0, self.vx0, self.vy0, self.vz0), reward, done
    
class FormiguinhaPBraco3_t:
    def __init__(self):
        self.high = 1
        self.low = -1
        self.state_dim = 8
        self.action_dim = 2
        self.name = 'FormiguinhaPBraço-v3-t'
        self.theta1 = 0
        self.theta2 = 0
        self.x0 = 0
        self.y0 = 0
        self.z0 = 0
        self.vx0 = 0
        self.vy0 = 0
        self.vz0 = 0
        self.L1 = 1.5
        self.L2 = 1.5
        self.Cx = 0
        self.Cy = 0
        self.posx, self.posy = self.calculaPosicao()
        self.targetx, self.targety = self.calculaTarget()
        self.distancia = self.calculaDistancia()
        self.dt = 1
        self.t = 0

    def calculaPosicao(self):
        self.posx = self.Cx + self.L1*np.cos(self.theta1) + self.L2*np.cos(self.theta1+self.theta2)
        self.posy = self.Cy + self.L1*np.sin(self.theta1) + self.L2*np.sin(self.theta1+self.theta2)
        return self.posx, self.posy

    def calculaTarget(self):
        tempo_queda = (self.vz0+np.sqrt(self.vz0**2+2*9.8*self.z0))/9.8
        self.targetx = self.x0 + tempo_queda*self.vx0
        self.targety = self.y0 + tempo_queda*self.vy0
        return self.targetx, self.targety

    def calculaDistancia(self):
        self.distancia = np.sqrt((self.posx-self.targetx)**2 + (self.posy-self.targety)**2)
        return self.distancia

    def calculaReward(self):
        return -self.distancia-0.8
    
    def reset(self):
        self.theta1 = random.uniform(-np.pi,np.pi)
        self.theta2 = random.uniform(-np.pi,np.pi)
        self.posx, self.posy = self.calculaPosicao()
        self.x0 = random.uniform(-1.8,1.8)
        self.y0 = random.uniform(-1.8,1.8)
        self.z0 = random.uniform(1, 1.8)
        self.vx0 = random.uniform(-1.5,1.5)
        self.vy0 = random.uniform(-1.5,1.5)
        self.vz0 = random.uniform(-1.5,1.5)
        self.targetx, self.targety = self.calculaTarget()
        self.t = 0
        return (self.posx, self.posy, self.x0, self.y0, self.z0, self.vx0, self.vy0, self.vz0)

    def step(self, action):
        omega1 = 0.3*action[0]
        omega2 = 0.3*action[1]
        if self.theta2 <= 0.01:
            omega2 = max(omega2,0)
        if self.theta2 >= 3.13:
            omega2 = min(omega2,0)
        self.theta1 += omega1
        self.theta2 += omega2
        if self.theta2 < 0:
            self.theta2 = 0
        if self.theta2 > 3.14:
            self.theta2 = 3.14
        self.posx, self.posy = self.calculaPosicao()
        self.distancia = self.calculaDistancia()
        self.t += self.dt
        reward = self.calculaReward()
        if self.distancia < 0.2:
            reward += 100
            done = True
        elif self.t >= 50:
            done = True
        else:
            done = False
        return (self.posx, self.posy, self.x0, self.y0, self.z0, self.vx0, self.vy0, self.vz0), reward, done
    
class FormiguinhaPBraco3_t2:
    def __init__(self):
        self.high = 1
        self.low = -1
        self.state_dim = 4
        self.action_dim = 2
        self.name = 'FormiguinhaPBraço-v3-t'
        self.theta1 = 0
        self.theta2 = 0
        self.L1 = 1.5
        self.L2 = 1.5
        self.Cx = 0
        self.Cy = 0
        self.posx, self.posy = self.calculaPosicao()
        self.targetx = 0
        self.targety = 0
        self.distancia = self.calculaDistancia()
        self.dt = 1
        self.t = 0

    def calculaPosicao(self):
        self.posx = self.Cx + self.L1*np.cos(self.theta1) + self.L2*np.cos(self.theta1+self.theta2)
        self.posy = self.Cy + self.L1*np.sin(self.theta1) + self.L2*np.sin(self.theta1+self.theta2)
        return self.posx, self.posy

    def calculaDistancia(self):
        self.distancia = np.sqrt((self.posx-self.targetx)**2 + (self.posy-self.targety)**2)
        return self.distancia

    def calculaReward(self):
        return -self.distancia-0.8
    
    def reset(self):
        self.theta1 = random.uniform(-np.pi,np.pi)
        self.theta2 = random.uniform(-np.pi,np.pi)
        self.posx, self.posy = self.calculaPosicao()
        self.targetx = random.uniform(-2.5,2.5)
        self.targety = random.uniform(-2.5,2.5)
        self.t = 0
        return (self.posx, self.posy, self.targetx, self.targety)

    def step(self, action):
        omega1 = 0.3*action[0]
        omega2 = 0.3*action[1]
        if self.theta2 <= 0.01:
            omega2 = max(omega2,0)
        if self.theta2 >= 3.13:
            omega2 = min(omega2,0)
        self.theta1 += omega1
        self.theta2 += omega2
        if self.theta2 < 0:
            self.theta2 = 0
        if self.theta2 > 3.14:
            self.theta2 = 3.14
        self.posx, self.posy = self.calculaPosicao()
        self.distancia = self.calculaDistancia()
        self.t += self.dt
        reward = self.calculaReward()
        if self.distancia < 0.2:
            reward += 100
            done = True
        elif self.t >= 50:
            done = True
        else:
            done = False
        return (self.posx, self.posy, self.targetx, self.targety), reward, done

