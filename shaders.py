from mathLib import matMatMult


def vertexShader(vertex, **kwargs):
    modelMatrix = kwargs["modelMatrix"]
    viewMatrix = kwargs["viewMatrix"]
    projectionMatrix = kwargs["projectionMatrix"]
    vpMatrix = kwargs["viewMatrix"]

    # Convertir el vértice a una matriz columna 4x1 agregando un valor de 1
    vt = [[vertex[0]], [vertex[1]], [vertex[2]], [1]]
    # Realizar la multiplicación de la matriz del modelo con el vértice
    vt = matMatMult(vpMatrix, matMatMult(projectionMatrix, matMatMult(viewMatrix, matMatMult(modelMatrix, vt))))
    # Convertir la matriz resultado de nuevo a un vértice (lista)
    vt = [vt[0][0],vt[1][0],vt[2][0]]
    return vt


def fragmentShader(**kwargs):
      texCoords = kwargs["texCoords"]
      texture = kwargs["texture"]
      if texture != None:
            color = texture.getColor(texCoords[0], texCoords[1])
      else:
            color = (1,1,1)
      return color

def grayscaleFragmentShader(**kwargs):
    texCoords = kwargs["texCoords"]
    texture = kwargs["texture"]
    if texture != None:
        color = texture.getColor(texCoords[0], texCoords[1])
        grayscale_value = sum(color) / 3  # Convert to grayscale
        color = (grayscale_value, grayscale_value, grayscale_value)
    else:
        color = (1, 1, 1)
    return color

def colorTintFragmentShader(**kwargs):
    texCoords = kwargs["texCoords"]
    texture = kwargs["texture"]
    tint_color = kwargs["tintColor"]
    if texture != None:
        color = texture.getColor(texCoords[0], texCoords[1])
        color = (color[0] * tint_color[0], color[1] * tint_color[1], color[2] * tint_color[2])
    else:
        color = tint_color
    return color

def edgeDetectionFragmentShader(**kwargs):
    texCoords = kwargs["texCoords"]
    texture = kwargs["texture"]
    threshold = kwargs["threshold"]
    if texture != None:
        color = texture.getColor(texCoords[0], texCoords[1])
        grayscale_value = sum(color) / 3
        edge_color = (0, 0, 0) if grayscale_value < threshold else (1, 1, 1)
    else:
        edge_color = (0, 0, 0)
    return edge_color

def sepiaFragmentShader(**kwargs):
    texCoords = kwargs["texCoords"]
    texture = kwargs["texture"]
    if texture != None:
        color = texture.getColor(texCoords[0], texCoords[1])
        sepia_color = (
            min(1, 0.272 * color[0] + 0.534 * color[1] + 0.131 * color[2]),
            min(1, 0.349 * color[0] + 0.686 * color[1] + 0.168 * color[2]),
            min(1, 0.393 * color[0] + 0.769 * color[1] + 0.189 * color[2])
        )
    else:
        sepia_color = (1, 1, 1)
    return sepia_color

