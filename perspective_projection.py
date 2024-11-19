import numpy as np


class Projection:
    
    def __init__(self, near, far, D, d):
        self.n = near
        self.f = far
        self.t = d/2
        self.b = -d/2
        self.r = D/2
        self.l = -D/2

    def homogeneous_coord(self, vc):
        n = vc.shape[0]
        vh = np.ones(n + 1)
        
        for i in range(n):
            vh[i] = vc[i]
        
        return vh
    
    def cartesien_coord(self, vh):
        n = vh.shape[0]
        vc = np.empty(n - 1)

        for i in range(n - 1):
            vc[i] = vh[i] / vh[n-1]
        
        return vc   
    
    def GL_projection(self, vertice):
        p_matrix = np.zeros((4, 4))

        p_matrix[0][0] = (2 * self.n) / (self.r - self.l)
        p_matrix[0][2] = (self.r + self.l) / (self.r - self.l)
        p_matrix[1][1] = (2 * self.n) / (self.t - self.b)
        p_matrix[1][2] = (self.t + self.b) / (self.t - self.b)
        p_matrix[2][2] = -((self.f + self.n) / (self.f - self.n))
        p_matrix[2][3] = (-1)*(2 * self.f * self.n) / (self.f - self.n)
        p_matrix[3][2] = -1

        v_eye = self.homogeneous_coord(vertice)
        v_clip = p_matrix @ v_eye
        v_clip = self.cartesien_coord(v_clip)
        return v_clip[:2]

