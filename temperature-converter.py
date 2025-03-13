# from nicegui import ui

# ui.colors(
#       primary='#2fa7c4',
#       secondary='#787576',
#       accent='#d67b27',
#       positive='#12a635',
#       negative='#bd0f23',
#       info='#708e94',
#       warning='#32452d'
# )

# def convert():
#     try: 
#         temp = float(input_field.value)
#         if conversion_type.value == "Celsius to Fahrenheit":
#             result_label.set_text(f"{temp}°C = {temp * 9/5 + 32:.2f}°F")
#         else:
#             result_label.set_text(f"{temp}°F = {(temp - 32) * 5/9:.2f}°C")
#         result_label.classes("text-lg font-semibold text-positive mt-4")
#         # text-positive: applies the positive color from ui.colors to the text
#     except ValueError:
#         result_label.set_text("Please enter a valid number.")
#         result_label.classes("text-lg font-semibold !text-negative mt-4")
#         # text-negative: applies the negative color from ui.colors to the text

# def convert_slider():
#     try: 
#         temp = float(slider.value)
#         if conversion_type.value == "Celsius to Fahrenheit":
#             result.set_text(f"{temp}°C = {temp * 9/5 + 32:.2f}°F")
#         else:
#             result.set_text(f"{temp}°F = {(temp - 32) * 5/9:.2f}°C")
#             result.classes("text-lg font-semibold text-positive mt-4")
#         # text-positive: applies the positive color from ui.colors to the text
#     except ValueError:
#         result.set_text("Please enter a valid number.")
#         result.classes("text-lg font-semibold !text-negative mt-4")
#         # text-negative: applies the negative color from ui.colors to the text

# with ui.row().classes("mx-auto"): 
#     with ui.card().classes("w-[400px] p-6 shadow-xl mx-auto mt-10 rounded-xl bg-white border border-gray-200"):
#         # w-100: Set element width to be fixed at 100
#         # p-6: Adds a padding of 1.5rem
#         # shadow-xl: Applies an extra large shadow. Element stands out
#         # mx-auto: sets right and left margin to auto, center element horizontally
#         # mt-10: Adds top margin of 2.5rem
#         # rounded-xl: XL border-radius for the rounded corners
#         ui.label("Temperature Converter").classes("text-2xl font-bold text-accent mb-4 tracking-wide")
#         # text-2xl: Sets Font size to 1.5rem (2xl)
#         # font-bold: Bolds the text
#         # text-accent:applies the accent color from ui.colors to the text
#         # mb-4: adds a bottom margin of 1rem
#         input_field = ui.input("Enter Temperature").props('type="number"').classes("w-full mb-4 p-2 text-lg border rounded")
#         # w-full: 100% of container is taken up of the input field 
#         # border: adds a default border 
#         # rounded: rounded adds a small border radius for the slightly rounded corners
#         conversion_type = ui.radio(["Celsius to Fahrenheit", "Fahrenheit to Celsius"], value="Celsius to Fahrenheit").classes("mb-4")
#         convert_button = ui.button("Convert", on_click=convert).classes("text-white font-bold py-2 px-4 rounded")

#         # text-white: Sets text color to white
#         # py-2: adds padding of 0.5 rem to top and bottom of text (vertical padding)
#         # px-4: Adds padding of 1 rem to the right and left (horizontal padding)
#         result_label = ui.label("").classes("text-lg mt-4 font-medium bg-gray-100 p-3 rounded-lg shadow-sm text-center")

#     with ui.card().classes("w-[400px] p-6 shadow-xl mx-auto mt-10 rounded-xl bg-white border border-gray-200"):
#         ui.label("Slider Temperature Converter").classes("text-2xl font-bold text-accent mb-4 tracking-wide text-center")
#         conversion_type = ui.radio(["Celsius to Fahrenheit", "Fahrenheit to Celsius"], value="Celsius to Fahrenheit").classes("mb-4")
        
#         slider = ui.slider(min=-50, max=150, value=50)
        
#         ui.label().bind_text_from(slider, 'value').classes("text-2xl font-bold text-accent mb-4 tracking-wide")
#         convert_button = ui.button("Convert", on_click=convert_slider).classes("text-white font-bold py-2 px-4 rounded")
#         result = ui.label("").classes("text-lg mt-4 font-medium bg-gray-100 p-3 rounded-lg shadow-sm text-center")


# ui.run()