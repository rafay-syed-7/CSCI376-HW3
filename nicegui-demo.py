from nicegui import ui

with ui.row().classes("mx-auto"):
    with ui.card():
        input_field = ui.input(on_change = lambda e: result.set_text(e.value.lower()))
        result = ui.label()

    with ui.card():
         ui.label("Temperature Converter").classes("text-2xl font-bold text-accent mb-4")
    # text-2xl: 
ui.run()