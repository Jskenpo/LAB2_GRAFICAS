from gl import Renderer
import shaders

# El tama�o del FrameBuffer
width = 1000
height = 1000

# Se crea el renderizador
rend = Renderer(width, height)

# Le damos los shaders que se utilizar�s
rend.vertexShader = shaders.vertexShader
rend.fragmentShader = shaders.fragmentShader

# Cargamos los modelos que rederizaremos
rend.glLoadModel(filename = "Dragon.obj",
                 textureName = "textures/modelD.bmp",
                 translate = (width/4, height/4, 0),
                 rotate = (10, 0, 0),
                 scale = (50,50,50))


# Se renderiza la escena
rend.glRender()

# Se crea el FrameBuffer con la escena renderizada
rend.glFinish("prueba.bmp")