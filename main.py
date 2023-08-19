from gl import Renderer
import shaders

# Tamaño del FrameBuffer
width = 1500
height = 1000

# Crear el renderizador
rend = Renderer(width, height)

# Asignar los shaders que se utilizarán
rend.vertexShader = shaders.vertexShader

# Asignar el fragment shader: Cambia esto según el shader que desees usar
#rend.fragmentShader = shaders.fragmentShader

#rend.fragmentShader = shaders.grayscaleFragmentShader
# O
#tint_color = (0.5, 0.5, 1.0)  # Cambia esto a tu color deseado
#rend.fragmentShader = lambda **kwargs: shaders.colorTintFragmentShader(tintColor=tint_color, **kwargs)

# O
#threshold_value = 0.5  # Cambia esto al valor de umbral deseado
#rend.fragmentShader = lambda **kwargs: shaders.edgeDetectionFragmentShader(threshold=threshold_value, **kwargs)

# O
rend.fragmentShader = shaders.sepiaFragmentShader

# Cargar los modelos que se renderizarán
rend.glLoadModel(filename="Dragon.obj",
                 textureName="textures/modelD.bmp",
                 translate=(600, height/4, 0),
                 rotate=(30, 0, 0),
                 scale=(10, 10, 10))

# Renderizar la escena
rend.glRender()

# Crear el FrameBuffer con la escena renderizada
rend.glFinish("sepia.bmp")
