from manim import *
from main import Clock

class ClockAnimation(Scene):

    def make_counter(self, counter):
        text = Text(str(counter), font="Ubuntu Mono", font_size=144)
        text.set_x(-4)
        return text

    def construct(self):

        counter = 0

        # Init clock
        clock = Clock(3)
        clock.set(counter)

        # Init text
        text = self.make_counter(counter)
        self.add(text)

        # Init rects
        rects = []
        for i in range(clock.n):
            for j in range(len(clock.rows)):
                rect = Rectangle(
                       width=1,
                       height=1)
                rect.set_x(-0.5*(clock.n-1)+i)
                rect.set_y((len(clock.rows)-1)*0.5-j)
                self.add(rect)
                rects.append(rect)

        # Init markers
        markers = []
        for i in range(len(clock.rows)):
            marker = Rectangle(
                    width=1,
                    height=1,
                    stroke_width=0)
            marker.set_fill(PINK, opacity=0.8)
            marker.set_x(-0.5*(clock.n-1) + clock.rows[i])
            marker.set_y((len(clock.rows)-1)*0.5-i)
            self.add(marker)
            markers.append(marker)
        self.wait(2)

        # Animate
        for i in range(100):
            clock.step()
            counter += 1
            # If the clock needs to grow...
            if len(clock.rows) > len(markers):
                # Add a new row of rectangles at the bottom
                for i in range(clock.n):
                    rect = Rectangle(width=1, height=1)
                    rect.set_x(-0.5*(clock.n-1)+i)
                    rect.set_y(-(len(clock.rows)-1)*0.5-0.5)
                    self.add(rect)
                    rects.append(rect)
                # Move everything up by 0.5 units
                anims=[]
                for rect in rects:
                    rect.generate_target()
                    rect.target.shift(UP*0.5)
                    anims.append(MoveToTarget(rect))
                for marker in markers:
                    marker.generate_target()
                    marker.target.shift(UP*0.5)
                    anims.append(MoveToTarget(marker))
                self.play(*anims)
                # Add a new marker
                marker = Rectangle(
                        width=1,
                        height=1,
                        stroke_width=0)
                marker.set_fill(PINK, opacity=0.8)
                marker.set_x(-0.5*(clock.n-1) + clock.rows[-1])
                marker.set_y((len(clock.rows)-1)*0.5-len(clock.rows)+1)
                self.add(marker)
                markers.append(marker)

            anims=[]
            for i in range(len(clock.rows)):
                markers[i].generate_target()
                markers[i].target.move_to((-0.5*(clock.n-1)+clock.rows[i], (len(clock.rows)-1)*0.5-i, 0))
                anims.append(MoveToTarget(markers[i]))
            anims.append(Transform(text, self.make_counter(counter)))
            self.play(*anims)
            self.wait(2)

