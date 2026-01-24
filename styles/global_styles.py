import tkinter.ttk as ttk

class GlobalStyles:
    background_color = "#2B2B2B"
    text_color = "#F9FAFB"

    button_color = "#7C3AED"
    button_hover = "#6D28D9"
    button_active = "#5B21B6"

    danger_button_color = "#DC2626"
    danger_button_hover = "#B91C1C"
    danger_button_active = "#991B1B"

    display_header_font = ("Century Gothic", 20)
    button_font = ("Century Gothic", 10)

    treeview_heading_color = "#7C3AED"
    treeview_heading_text_color = "#F9FAFB"
    treeview_heading_hover = "#6D28D9"
    treeview_background_color = "#2B2B2B"
    treeview_field_background_color = "#222121"
    treeview_font = ("Century Gothic", 10)
    treeview_heading_relief = "flat"

    loading_label_font = ("Century Gothic", 12, "italic")

    form_label_font = ("Century Gothic", 10, "bold")

    entry_font = ("Century Gothic", 10)
    entry_background = "#1F1F1F"
    entry_border_color = "#3F3F46"
    entry_focus_border = "#7C3AED"



    @staticmethod
    def apply_styles(style: ttk.Style):
        style.theme_use("clam")

        # Main frame
        style.configure("App.TFrame", background=GlobalStyles.background_color)

        # Primary button
        style.configure(
            "Primary.TButton",
            font=GlobalStyles.button_font,
            padding=10,
            background=GlobalStyles.button_color,
            foreground="white",
            borderwidth=0
        )

        style.map(
            "Primary.TButton",
            background=[
                ("active", GlobalStyles.button_hover),
                ("pressed", GlobalStyles.button_active)
            ]
        )

        # Danger button
        style.configure(
            "Danger.TButton",
            font=GlobalStyles.button_font,
            padding=10,
            background=GlobalStyles.danger_button_color,
            foreground="white",
            borderwidth=0
        )
        style.map(
            "Danger.TButton",
            background=[
                ("active", GlobalStyles.danger_button_hover),
                ("pressed", GlobalStyles.danger_button_active)
            ]
        )

        # Header label style
        style.configure(
            "Header.TLabel",
            background=GlobalStyles.background_color,
            foreground=GlobalStyles.text_color,
            font=GlobalStyles.display_header_font
        )

        # Form labels (for Entry fields)
        style.configure(
            "Form.TLabel",
            background=GlobalStyles.background_color,
            foreground=GlobalStyles.text_color,
            font=GlobalStyles.form_label_font
        )

        # Entry fields
        style.configure(
            "Form.TEntry",
            font=GlobalStyles.entry_font,
            foreground=GlobalStyles.text_color,
            fieldbackground=GlobalStyles.entry_background,
            background=GlobalStyles.entry_background,
            bordercolor=GlobalStyles.entry_border_color,
            lightcolor=GlobalStyles.entry_border_color,
            darkcolor=GlobalStyles.entry_border_color,
            padding=8,
            relief="flat"
        )

        style.map(
            "Form.TEntry",
            bordercolor=[("focus", GlobalStyles.entry_focus_border)],
            lightcolor=[("focus", GlobalStyles.entry_focus_border)],
            darkcolor=[("focus", GlobalStyles.entry_focus_border)]
        )



        # TreeView (Data Table)
        style.configure(
            "Custom.Treeview",
            font=GlobalStyles.treeview_font,
            foreground=GlobalStyles.treeview_heading_text_color,
            background=GlobalStyles.treeview_background_color,
            fieldbackground=GlobalStyles.treeview_field_background_color,
            padding=[10, 10, 10, 10]
        )

        # Configure the Treeview heading style
        style.configure("Custom.Treeview.Heading",
            background=GlobalStyles.treeview_heading_color,
            foreground="white",
            font=GlobalStyles.treeview_font,
            relief=GlobalStyles.treeview_heading_relief
        )

        # Map the selection color for selected rows in TreeView
        style.map("Custom.Treeview", 
            background=[('selected', 'blue')],
            foreground=[('selected', 'white')]
        )

        style.map("Custom.Treeview.Heading",
            background=[
                ('active', GlobalStyles.treeview_heading_hover)
            ]
        )

        # Loading label
        style.configure(
            "Loading.TLabel",
            background=GlobalStyles.background_color,
            foreground=GlobalStyles.text_color,
            font=GlobalStyles.loading_label_font
        )
