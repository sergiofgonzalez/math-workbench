import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import matplotlib.cm
from my_vectors import *
from my_matrices import *
from my_transformations import polygon_map
from math import *
import sys



blues = matplotlib.cm.get_cmap('Blues')

# added in chapter 4 (get_matrix)
def draw_model(faces, color_map=blues, light=(1,2,3), display_axes=True, get_matrix=None):
    def normal(face):
        return (cross(subtract(face[1], face[0]), subtract(face[2], face[0])))

    def shade(face, color_map=blues, light=(1, 2, 3)):
        return color_map(1 - dot(unit(normal(face)), unit(light)))

    def draw_axes():
        axes =  [
            [(-1000,0,0),(1000,0,0)],
            [(0,-1000,0),(0,1000,0)],
            [(0,0,-1000),(0,0,1000)]
        ]
        glBegin(GL_LINES)
        for axis in axes:
            for vertex in axis:
                glColor3fv((1,1,1))
                glVertex3fv(vertex)
        glEnd()

    def do_matrix_transform(v):
        if get_matrix:
            m = get_matrix(pygame.time.get_ticks())
            return multiply_matrix_vector(m, v)
        else:
            return v

    # switched from pygame.display() as this works better when cleaning up
    pygame.display.init()
    display = (400, 400)
    window = pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    # Set our perspective when looking at the the 3D scene
    # 45 is the viewing angle
    # 1 is the aspect ratio
    # 0.1 and 50 put limist on the z coordinates that are rendered:
    #   no objects further than 50 units or closer than 0.1 will be rendered
    gluPerspective(45, 1, 0.1, 50.0)

    # Observe the scene from 5 units up the z axis
    # (-5 means move the scene down by (0, 0, -5))
    glTranslatef(0.0, 0.0, -5)

    # hide polygons not visible from our perspective
    glEnable(GL_CULL_FACE)

    # render polygons closer to us on top of those further from us
    glEnable(GL_DEPTH_TEST)

    # hide polygons facing us but located behind other polygons
    glCullFace(GL_BACK)

    clock = pygame.time.Clock()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                sys.exit(0)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        if display_axes:
            draw_axes()

        glBegin(GL_TRIANGLES)

        transformed_faces = polygon_map(do_matrix_transform, faces)

        for face in transformed_faces:
            color = shade(face, blues, light)
            for vertex in face:
                glColor3fv((color[0], color[1], color[2]))
                glVertex3fv(vertex)
        glEnd()
        pygame.display.flip()