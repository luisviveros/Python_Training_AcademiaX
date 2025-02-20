class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
        
    def __add__(self, otro):
        return Vector2D(self.x + otro.x, self.y + otro.y)
    
v1 = Vector2D(1, 1)
v2 = Vector2D(3, 4)
v3 = v1 + v2
print(v3.x, v3.y)

print([1,2]+ [3,4])

#Ejercicio ahora lo mismo pero con vector 3D

class vector3D :
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def __add__(self, otro) :
        return vector3D(self.x + otro.x, self.y + otro.y, self.z + otro.z)

vec1 = vector3D(3,2,1)
vec2 = vector3D(4,1,2)
vec3 = vector3D(3,5,3)
vec4 = vec1 + vec2 +vec3
print (vec1.x, vec2.y,vec3.z)