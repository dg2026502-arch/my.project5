s = sphere(pos=vec(0, 0, 0), radius=2, color=color.yellow)
left_eye = sphere(pos=vector(-0.7,0.5,1.7), radius=0.2, color=color.black)
right_eye = sphere(pos=vector(0.7,0.5,1.7), radius=0.2, color=color.black)
ear1 = ellipsoid(pos=vec(-0.5, 2.3, 0), length=1, height=2.5, width=1, color=color.yellow)
ear2 = ellipsoid(pos=vec(0.5, 2.3, 0), length=1, height=2.5, width=1, color=color.yellow)
eyebrow1 = curve(pos=[vector(-1.0,1.2,1.25), vector(-0.6,1.35,1.45)], color=color.black,radius=0.05)
eyebrow2 = curve(pos=[vector(1.0,1.2,1.25), vector(0.6,1.35,1.45)],color=color.black,radius=0.05)
mouth1 = curve(pos=[ vector(-0.18, -0.12, 1.93),vector(-0.08, -0.22, 1.95),vector(0.0, -0.16, 1.96),vector(0.08, -0.22, 1.95),vector(0.18, -0.12, 1.93)],color=color.black,radius=0.05)
mouth2 = curve(pos=[ vector(0.0, -0.28, 1.94),vector(0.03, -0.33, 1.94)],color=color.black,radius=0.04)
cheek1 = sphere(pos=vector(-1.1,-0.3,1.5),radius=0.28,color=vector(1,0.7,0.8),opacity=0.7)
cheek2 = sphere(pos=vector(1.1,-0.3,1.5),radius=0.28,color=vector(1,0.7,0.8),opacity=0.7)
b = compound([s, left_eye, right_eye,
         ear1, ear2,
         cheek1, cheek2])
while True:
    rate(100)
    k = keysdown()

    if ' ' in k :
        b.pos = vec(0,0,0)
    if 'd' in k :
        b.pos.x = b.pos.x + 0.1
    if 'a' in k :
        b.pos.x = b.pos.x - 0.1
    if 'w' in k :
        b.pos.y = b.pos.y + 0.1
    if 's' in k :
        b.pos.y = b.pos.y - 0.1
    
