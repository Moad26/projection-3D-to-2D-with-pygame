import numpy as np

class Rotation:

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
    
    def tr_to_origine(self, center_coor):
        x_c, y_c, z_c = center_coor[0], center_coor[1], center_coor[2]
        
        tr_to_origine_matrix = np.array([
        [1, 0, 0, -x_c],
        [0, 1, 0, -y_c],
        [0, 0, 1, -z_c],
        [0, 0, 0, 1]
    ])
        return tr_to_origine_matrix

    def tr_to_center(self, center_coor):
        x_c, y_c, z_c = center_coor[0], center_coor[1], center_coor[2]
        
        tr_to_center_matrix = np.array([
        [1, 0, 0, x_c],
        [0, 1, 0, y_c],
        [0, 0, 1, z_c],
        [0, 0, 0, 1]
    ])
        return tr_to_center_matrix
    
    def rotate_vertices(self, vertices, angle_x, angle_y, angle_z, center_coor):

        rot_x = np.array([
            [1, 0, 0, 0],
            [0, np.cos(angle_x), -np.sin(angle_x), 0],
            [0, np.sin(angle_x), np.cos(angle_x), 0],
            [0, 0, 0, 1]
        ])
        rot_y = np.array([
            [np.cos(angle_y), 0, np.sin(angle_y), 0],
            [0, 1, 0, 0],
            [-np.sin(angle_y), 0, np.cos(angle_y), 0],
            [0, 0, 0, 1]
        ])
        rot_z = np.array([
            [np.cos(angle_z), -np.sin(angle_z), 0, 0],
            [np.sin(angle_z), np.cos(angle_z), 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ])

        rotation_matrix = rot_z @ rot_y @ rot_x

        tr_to_origine_matrix = self.tr_to_origine(center_coor)
        tr_to_center_matrix = self.tr_to_center(center_coor)

        tr_final = tr_to_center_matrix @ rotation_matrix @ tr_to_origine_matrix

        vertices_h = self.homogeneous_coord(vertices)
        vertices_rot = vertices_h @tr_final


        return vertices_rot[:3]