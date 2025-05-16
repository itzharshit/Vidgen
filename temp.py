from manim import *

class NumericalExample(Scene):
    def construct(self):
        # Define the side length of the square
        side_length = 5

        # Create a square with the specified side length
        square = Square(side_length=side_length)

        # Create the equation for the area calculation
        area_formula = MathTex("A = 5^2 = 25")

        # Position the equation below the square
        area_formula.next_to(square, DOWN)

        # Create a brace to highlight the side length of the square
        side_brace = Brace(square, LEFT, buff=0) # Create a brace on the left side of the square
        side_label = side_brace.get_text("5") # Label the brace with the side length

        # Display the square, equation, and label
        self.play(Create(square), Write(area_formula), Create(side_brace), Write(side_label))

        # Highlight the side length '5' on the square and in the equation simultaneously
        self.play(Indicate(side_label), Indicate(area_formula[0][2])) # Indicate the second element (index 1) which is the first '5'

        # State that the area of the square is 25 square units
        area_text = Tex("The area of the square is 25 square units.")
        area_text.next_to(area_formula, DOWN)

        # Display the area text
        self.play(Write(area_text))

        # Keep the scene on the screen for a short time
        self.wait(3)
