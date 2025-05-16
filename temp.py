# manim -pql example.py ExampleCalculation

from manim import *

class ExampleCalculation(Scene):
    def construct(self):
        # Define the side length of the square
        side_length = 5

        # Create the square
        square = Square(side_length=side_length)

        # Label the side length
        side_label = MathTex("s = 5")
        side_label.next_to(square, DOWN)

        # Create the area formula
        area_formula = MathTex("A = s \times s")
        area_formula.to_edge(UP)

        # Display the square and side length
        self.play(Create(square), Write(side_label), Write(area_formula))
        self.wait(1)

        # Create the first step of the calculation
        step1 = MathTex("A = 5 \times 5")
        step1.next_to(area_formula, DOWN)

        # Transform the formula into the first step
        self.play(Transform(area_formula, step1))
        self.wait(1)

        # Create the second step of the calculation
        step2 = MathTex("A = 25")
        step2.next_to(area_formula, DOWN)

        # Transform the first step into the second step
        self.play(Transform(area_formula, step2))
        self.wait(1)

        # Create the final answer with units
        answer = MathTex("A = 25 \text{ square units}")
        answer.next_to(area_formula, DOWN)

        # Transform the second step into the final answer
        self.play(Transform(area_formula, answer))
        self.wait(2)
