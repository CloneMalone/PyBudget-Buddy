# Import tkinter styling utilities
import tkinter.ttk as ttk

# Class that defines all global color and styling constants for the application
class GlobalStyles:
    # Color scheme - dark background with light text
    background_color = "#2B2B2B"
    text_color = "#F9FAFB"

    # Primary button colors
    button_color = "#7C3AED"
    button_hover = "#6D28D9"
    button_active = "#5B21B6"

    # Info button colors (for neutral / informational actions)
    info_button_color = "#2563EB"
    info_button_hover = "#1D4ED8"
    info_button_active = "#1E40AF"

    # Danger button colors (for destructive actions)
    danger_button_color = "#DC2626"
    danger_button_hover = "#B91C1C"
    danger_button_active = "#991B1B"

    # Secondary button colors (neutral navigation actions)
    secondary_button_color = "#374151"
    secondary_button_hover = "#4B5563"
    secondary_button_active = "#1F2933"


    # Font families and sizes used throughout the app
    display_header_font = ("Century Gothic", 20)
    button_font = ("Century Gothic", 10)

    # TreeView (data table) styling
    treeview_heading_color = "#7C3AED"
    treeview_heading_text_color = "#F9FAFB"
    treeview_heading_hover = "#6D28D9"
    treeview_background_color = "#2B2B2B"
    treeview_field_background_color = "#222121"
    treeview_font = ("Century Gothic", 10)
    treeview_heading_relief = "flat"

    # Loading label styling (italic text for emphasis)
    loading_label_font = ("Century Gothic", 12, "italic")

    # Form label styling (bold for emphasis)
    form_label_font = ("Century Gothic", 10, "bold")

    # Entry field (text input) styling
    entry_font = ("Century Gothic", 10)
    entry_background = "#1F1F1F"
    entry_border_color = "#3F3F46"
    entry_focus_border = "#7C3AED"

    # Category summary (small cards) styling
    category_card_background = "#2563EB"
    category_card_border = "#2B2B2B"
    category_name_font = ("Century Gothic", 12, "bold")
    category_amount_font = ("Century Gothic", 12, "bold")
    category_card_padding = (10, 8)



    # Static method that applies all styles to the entire application
    @staticmethod
    def apply_styles(style: ttk.Style):
        # Use the "clam" theme as the base theme
        style.theme_use("clam")

        # Main app frame styling
        style.configure("App.TFrame", background=GlobalStyles.background_color)

        # Primary button styling
        style.configure(
            "Primary.TButton",
            font=GlobalStyles.button_font,
            padding=10,
            background=GlobalStyles.button_color,
            foreground="white",
            borderwidth=0
        )

        # Primary button hover and active states
        style.map(
            "Primary.TButton",
            background=[
                ("active", GlobalStyles.button_hover),
                ("pressed", GlobalStyles.button_active)
            ]
        )

        # Secondary button styling (neutral navigation buttons)
        style.configure(
            "Secondary.TButton",
            font=GlobalStyles.button_font,
            padding=10,
            background=GlobalStyles.secondary_button_color,
            foreground="white",
            borderwidth=0
        )

        style.map(
            "Secondary.TButton",
            background=[
                ("active", GlobalStyles.secondary_button_hover),
                ("pressed", GlobalStyles.secondary_button_active)
            ]
        )



        # Danger button styling (for delete/destructive actions)
        style.configure(
            "Danger.TButton",
            font=GlobalStyles.button_font,
            padding=10,
            background=GlobalStyles.danger_button_color,
            foreground="white",
            borderwidth=0
        )
        # Danger button hover and active states
        style.map(
            "Danger.TButton",
            background=[
                ("active", GlobalStyles.danger_button_hover),
                ("pressed", GlobalStyles.danger_button_active)
            ]
        )

        # Info button styling (for informational / secondary actions)
        style.configure(
            "Info.TButton",
            font=GlobalStyles.button_font,
            padding=10,
            background=GlobalStyles.info_button_color,
            foreground="white",
            borderwidth=0
        )

        # Info button hover and active states
        style.map(
            "Info.TButton",
            background=[
                ("active", GlobalStyles.info_button_hover),
                ("pressed", GlobalStyles.info_button_active)
            ]
        )


        # Header label styling (large, bold text)
        style.configure(
            "Header.TLabel",
            background=GlobalStyles.background_color,
            foreground=GlobalStyles.text_color,
            font=GlobalStyles.display_header_font
        )

        # Sub-header label styling (used for totals)
        style.configure(
            "SubHeader.TLabel",
            background=GlobalStyles.background_color,
            foreground=GlobalStyles.text_color,
            font=("Century Gothic", 14)
        )


        # Form labels styling (for input field labels)
        style.configure(
            "Form.TLabel",
            background=GlobalStyles.background_color,
            foreground=GlobalStyles.text_color,
            font=GlobalStyles.form_label_font
        )

        # Entry field (text input) styling
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

        # Entry field focus state styling (purple border when focused)
        style.map(
            "Form.TEntry",
            bordercolor=[("focus", GlobalStyles.entry_focus_border)],
            lightcolor=[("focus", GlobalStyles.entry_focus_border)],
            darkcolor=[("focus", GlobalStyles.entry_focus_border)]
        )



        # TreeView (Data Table) styling
        style.configure(
            "Custom.Treeview",
            font=GlobalStyles.treeview_font,
            foreground=GlobalStyles.treeview_heading_text_color,
            background=GlobalStyles.treeview_background_color,
            fieldbackground=GlobalStyles.treeview_field_background_color,
            padding=[10, 10, 10, 10]
        )

        # Configure the TreeView column heading styling
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

        # TreeView heading hover state (changes color on hover)
        style.map("Custom.Treeview.Heading",
            background=[
                ('active', GlobalStyles.treeview_heading_hover)
            ]
        )

        # Loading label styling (italic text for loading messages)
        style.configure(
            "Loading.TLabel",
            background=GlobalStyles.background_color,
            foreground=GlobalStyles.text_color,
            font=GlobalStyles.loading_label_font
        )

        # Category card styling (small summary cards shown above tables)
        style.configure(
            "CategoryCard.TFrame",
            background=GlobalStyles.category_card_background,
            relief="flat",
            borderwidth=1,
            padding=GlobalStyles.category_card_padding
        )

        style.configure(
            "CategoryName.TLabel",
            background=GlobalStyles.category_card_background,
            foreground=GlobalStyles.text_color,
            font=GlobalStyles.category_name_font,
            padding=(2,0)
        )

        style.configure(
            "CategoryAmount.TLabel",
            background=GlobalStyles.category_card_background,
            foreground=GlobalStyles.text_color,
            font=GlobalStyles.category_amount_font,
            padding=(2,0)
        )

