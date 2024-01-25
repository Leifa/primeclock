from manim import *
from main import Clock

config.frame_width = 24

class ClockMobject(Mobject):
    def __init__(self, n, color, x, y, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.n = n
        self.color = color
        self.counter = 0
        self.x = x
        self.y = y

        # Init clock
        self.clock = Clock(n)
        self.clock.set(self.counter)

        # Init markers
        self.markers = []
        for i in range(len(self.clock.rows)):
            marker = Rectangle(
                    width=1,
                    height=1,
                    stroke_width=0)
            marker.set_fill(self.color, opacity=1)
            marker.set_x(x+self.clock.rows[i])
            marker.set_y(y-i)
            self.add(marker)
            self.markers.append(marker)

        # Init rects
        self.rects = []
        for i in range(self.n):
            for j in range(len(self.clock.rows)):
                rect = Rectangle(
                       width=1,
                       height=1)
                rect.set_x(x + i)
                rect.set_y(y-j)
                self.add(rect)
                self.rects.append(rect)

    def add_new_row(self):
        self.new_elements = []
        # Add a new marker
        marker = Rectangle(
                width=1,
                height=1,
                stroke_width=0)
        marker.set_fill(self.color, opacity=0.4)
        marker.set_x(self.x)
        marker.set_y(self.y+1-len(self.clock.rows))
        self.new_elements.append(marker)
        self.markers.append(marker)
        # Add a new row of rectangles at the bottom
        for i in range(self.n):
            rect = Rectangle(width=1, height=1)
            rect.set_x(self.x+i)
            rect.set_y(self.y+1-len(self.clock.rows))
            self.new_elements.append(rect)
            self.rects.append(rect)

class StepAnimation(Animation):
    def __init__(self, mobject, **kwargs):
        super().__init__(mobject, **kwargs)

    def begin(self):
        on_first_column = True
        for i in range(len(self.mobject.clock.rows)):
            if self.mobject.clock.rows[i] > 0:
                on_first_column = False
            if on_first_column:
                opacity = 1
            else:
                opacity = 0.4
            self.mobject.markers[i].generate_target()
            self.mobject.markers[i].target.set_opacity(opacity)
            self.mobject.markers[i].target.move_to((self.mobject.x+self.mobject.clock.rows[i], self.mobject.y-i, 0))
        
    def interpolate_mobject(self, alpha):
        for marker in self.mobject.markers:
            marker.interpolate(marker, marker.target, alpha)

class NewRowAnimation(AnimationGroup):
    def __init__(self, mobject, **kwargs):
        animations = [Create(element) for element in mobject.new_elements]
        super().__init__(*animations, **kwargs)

primes = [2, 3, 5, 7]
colors = [PINK, ORANGE, GREEN, BLUE]

class MyScene(Scene):

    def make_counter(self, counter):
        text = Text(str(counter), font="Ubuntu Mono", font_size=144)
        text.set_y(5)
        return text

    def make_tex(self, number, prime_factors):
        if number == 0 or number == 1:
            tex_string = f"{number} = {number}"
        else:
            tex_string = str(number) + " = {{" + str(prime_factors[0]) + "}}"
            for p in prime_factors[1:]:
                tex_string += r" \times {{" + str(p) + "}}"
        tex = MathTex(tex_string)
        for i in range(len(primes)):
            tex.set_color_by_tex(str(primes[i]), colors[i], substring=False)
        tex.font_size = 120
        tex.set_y(5)
        return tex

    def construct(self):
        # Add the equation to the scene
        equation = self.make_tex(0, [])
        self.add(equation)

        counter = 0
        #text = self.make_counter(counter)
        #self.add(text)

        clock2 = ClockMobject(2, PINK, -9, 2)
        clock3 = ClockMobject(3, ORANGE, -6, 2)
        clock5 = ClockMobject(5, GREEN, -2, 2)
        clock7 = ClockMobject(7, BLUE, 4, 2)

        clocks = [clock2, clock3, clock5, clock7]

        for clock in clocks:
            self.add(clock)
        self.wait(2)

        for i in range(120):
            counter += 1
            for clock in clocks:
                clock.clock.step()

            for clock in clocks:
                if len(clock.clock.rows) > len(clock.markers):
                    clock.add_new_row()
                    self.play(NewRowAnimation(clock))

            # Compute prime factorization
            multiplicities = [clock.clock.get_multiplicity() for clock in clocks]
            prime_factors = []
            for i in range(len(multiplicities)):
                prime_factors.extend([primes[i]]*multiplicities[i])
            rest = counter
            for d in prime_factors:
                rest //= d
            if rest > 1:
                prime_factors.append(rest)
            new_tex = self.make_tex(counter, prime_factors)

            anims = [StepAnimation(clock) for clock in clocks]
            #anims.append(Transform(text, self.make_counter(counter)))
            anims.append(Transform(equation, new_tex))
            self.play(*anims)
            self.wait(2)

