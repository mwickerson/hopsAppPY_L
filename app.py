"""Hops flask middleware example"""
from flask import Flask
import ghhops_server as hs
import rhino3dm


# register hops app as middleware
app = Flask(__name__)
hops: hs.HopsFlask = hs.Hops(app)


# flask app can be used for other stuff drectly
@app.route("/help")
def help():
    return "Welcome to Grashopper Hops for CPython!"



#GPT-4
#Hops can be used to create a flask app that can be used to serve a GPT-4 model
#The model can be used to generate text from a prompt

#getting started
import numpy as np
import matplotlib.pyplot as plt
import math

def face_profile(z):
    return 10 + 20j - 10*np.exp(1j*z) - 5*np.exp(2j*z) - 3*np.exp(3j*z)

x = np.linspace(-np.pi, np.pi, 500)
y = face_profile(x)

plt.plot(y.real, y.imag, color='black')
plt.axis('equal')
plt.show()



import numpy as np
import matplotlib.pyplot as plt

def face_profile(t, a0, a1, b1, a2, b2, a3, b3, c1, c2, c3):
    # Evaluate the complex trigonometric polynomial at t
    return (a0 + a1 * np.exp(1j * t) + b1 * np.exp(-1j * t)
            + a2 * np.exp(2j * t) + b2 * np.exp(-2j * t)
            + a3 * np.exp(3j * t) + b3 * np.exp(-3j * t)
            + c1 * np.cos(t) + c2 * np.cos(2 * t) + c3 * np.cos(3 * t))

# Define the parameters for the face profile
a0 = 0.5
a1 = 0.3
b1 = 0.1
a2 = -0.1
b2 = 0.05
a3 = 0.05
b3 = 0.025
c1 = 0.05
c2 = -0.01
c3 = 0.005

# Generate the range of t values
t = np.linspace(0, 2 * np.pi, 1000)

# Evaluate the face profile at t
z = face_profile(t, a0, a1, b1, a2, b2, a3, b3, c1, c2, c3)

# Plot the real part of the face profile as a curve
plt.plot(t, np.real(z), color='black')

# Add labels and title
plt.xlabel('t')
plt.ylabel('Real part of f(t)')
plt.title('Face profile')

# Show the plot
plt.show()

@hops.component(
    "/binmult",
    inputs=[hs.HopsNumber("A"), hs.HopsNumber("B")],
    outputs=[hs.HopsNumber("Multiply")],
)
def BinaryMultiply(a: float, b: float):
    return a * b

@hops.component(
    "/add",
    name="Add",
    nickname="Add",
    description="Add numbers with CPython",
    inputs=[
        hs.HopsNumber("A", "A", "First number"),
        hs.HopsNumber("B", "B", "Second number"),
    ],
    outputs=[hs.HopsNumber("Sum", "S", "A + B")]
)
def add(a: float, b: float):
    return a + b


@hops.component(
    "/pointat",
    name="PointAt",
    nickname="PtAt",
    description="Get point along curve",
    icon="pointat.png",
    inputs=[
        hs.HopsCurve("Curve", "C", "Curve to evaluate"),
        hs.HopsNumber("t", "t", "Parameter on Curve to evaluate")
    ],
    outputs=[hs.HopsPoint("P", "P", "Point on curve at t")]
)
def pointat(curve: rhino3dm.Curve, t=0.0):
    return curve.PointAt(t)


@hops.component(
    "/srf4pt",
    name="4Point Surface",
    nickname="Srf4Pt",
    description="Create ruled surface from four points",
    inputs=[
        hs.HopsPoint("Corner A", "A", "First corner"),
        hs.HopsPoint("Corner B", "B", "Second corner"),
        hs.HopsPoint("Corner C", "C", "Third corner"),
        hs.HopsPoint("Corner D", "D", "Fourth corner")
    ],
    outputs=[hs.HopsSurface("Surface", "S", "Resulting surface")]
)
def ruled_surface(a: rhino3dm.Point3d,
                  b: rhino3dm.Point3d,
                  c: rhino3dm.Point3d,
                  d: rhino3dm.Point3d):
    edge1 = rhino3dm.LineCurve(a, b)
    edge2 = rhino3dm.LineCurve(c, d)
    return rhino3dm.NurbsSurface.CreateRuledSurface(edge1, edge2)

# write a @hops.component function that creates complex numbers
# and returns them as a list of points
@hops.component(
    "/complex",
    name="Complex Numbers",
    nickname="Complex",
    description="Create complex numbers",
    inputs=[
        hs.HopsNumber("Real", "R", "Real part of complex number"),
        hs.HopsNumber("Imaginary", "I", "Imaginary part of complex number")
    ],
    outputs=[hs.HopsPoint("Complex", "C", "Complex number")]
)
def complex(r: float, i: float):
    return rhino3dm.Point3d(r, i, 0)

# write a @hops.component function that creates complex numbers
# and returns them as a list of points with a z component of something inputed and randomly altered
@hops.component(
    "/complex2",
    name="Complex Numbers",
    nickname="Complex",
    description="Create complex numbers",
    inputs=[
        hs.HopsNumber("Real", "R", "Real part of complex number"),
        hs.HopsNumber("Imaginary", "I", "Imaginary part of complex number"),
        hs.HopsNumber("Z", "Z", "Z component of complex number")
    ],
    outputs=[hs.HopsPoint("Complex", "C", "Complex number")]
)
def complex(r: float, i: float, z: float):
    import math
    import random
    return rhino3dm.Point3d(r, i, z + random.uniform(-3, 3))








if __name__ == "__main__":
    app.run(debug=True)
