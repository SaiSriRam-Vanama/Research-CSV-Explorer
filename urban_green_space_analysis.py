import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import ipywidgets as widgets
from IPython.display import display, clear_output, HTML
import folium
import numpy as np

sns.set_theme(style="whitegrid")

class CSVAnalyzer:
    def __init__(self):
        self.data = None
        self.create_ui()

    def create_ui(self):
        header = widgets.HTML(
            value='<h1 style="background: linear-gradient(45deg, #00b4db, #0083b0); -webkit-background-clip: text; -webkit-text-fill-color: transparent; text-align:center; font-size:2.5em; font-weight:bold; text-shadow: 0 2px 4px rgba(0,0,0,0.2);">URBAN GREEN SPACE ANALYSIS</h1>'
        )

        self.file_upload = widgets.FileUpload(
            accept='.csv',
            multiple=False,
            description='Upload Dataset',
            button_style='info',
            layout=widgets.Layout(
                width='350px',
                border='2px solid #00b4db',
                border_radius='10px',
                padding='10px',
                background='linear-gradient(135deg, rgba(0,180,219,0.1), rgba(0,131,144,0.1))'
            )
        )
        self.file_upload.layout.display = 'flex'
        self.file_upload.layout.justify_content = 'center'
        self.file_upload.layout.align_items = 'center'

        self.file_upload.observe(self.process_upload, names='value')

        def futuristic_button(description, color='#00b4db'):
            return widgets.Button(
                description=description,
                layout=widgets.Layout(
                    width='200px',
                    margin='5px',
                    border_radius='25px',
                    background=f'linear-gradient(135deg, {color}, {color}80)',
                    color='white',
                    font_weight='bold',
                    border=f'2px solid {color}',
                    box_shadow='0 4px 6px rgba(0,0,0,0.1)'
                )
            )

        self.view_data_button = futuristic_button('View Data', '#00b4db')
        self.stats_button = futuristic_button('Basic Stats', '#0083b0')
        self.histogram_button = futuristic_button('Histogram', '#00bf72')
        self.scatter_button = futuristic_button('Scatter Plot', '#ff6b6b')
        self.heatmap_button = futuristic_button('Correlation Map', '#8946a6')
        self.map_button = futuristic_button('Geo Visualization', '#ff9d6c')

        self.view_data_button.on_click(self.view_data)
        self.stats_button.on_click(self.show_stats)
        self.histogram_button.on_click(self.plot_histogram)
        self.scatter_button.on_click(self.plot_scatter)
        self.heatmap_button.on_click(self.plot_heatmap)
        self.map_button.on_click(self.plot_data_on_map)

        self.output = widgets.Output(
            layout={
                'border': '2px solid #00b4db',
                'border_radius': '10px',
                'padding': '15px',
                'margin': '10px 0px',
                'background': 'linear-gradient(135deg, rgba(0,180,219,0.05), rgba(0,131,144,0.05))'
            }
        )

        buttons = widgets.GridBox(
            children=[
                self.view_data_button,
                self.stats_button,
                self.histogram_button,
                self.scatter_button,
                self.heatmap_button,
                self.map_button
            ],
            layout=widgets.Layout(
                grid_template_columns='repeat(3, 1fr)',
                grid_gap='10px'
            )
        )

        main_layout = widgets.VBox(
            [header, self.file_upload, buttons, self.output],
            layout=widgets.Layout(
                padding='20px',
                background='white',
                border_radius='15px',
                box_shadow='0 10px 25px rgba(0,0,0,0.1)'
            )
        )

        display(main_layout)

    def process_upload(self, change):
        with self.output:
            clear_output()
            try:
                filename = os.path.basename(list(change['new'].keys())[0])
                content = change['new'][filename]['content']

                with open(filename, 'wb') as f:
                    f.write(content)

                self.data = pd.read_csv(filename)
                print(f"Successfully loaded {filename}")
                print(f"Shape: {self.data.shape}")

                if "latitude" not in self.data.columns or "longitude" not in self.data.columns:
                    print("Adding mock latitude and longitude for demo...")
                    self.data["latitude"] = np.random.uniform(8.0, 37.0, len(self.data))
                    self.data["longitude"] = np.random.uniform(68.0, 97.0, len(self.data))

            except Exception as e:
                print(f"Error: {str(e)}")

    def view_data(self, b):
        with self.output:
            clear_output()
            if self.data is None:
                print("Please upload a CSV file first!")
                return

            display(HTML("<h3>First 5 Rows of the Dataset</h3>"))
            display(self.data.head())

    def show_stats(self, b):
        with self.output:
            clear_output()
            if self.data is None:
                print("Please upload a CSV file first!")
                return

            display(HTML("<h3>Basic Statistics</h3>"))
            display(self.data.describe())

    def plot_histogram(self, b):
        with self.output:
            clear_output()
            if self.data is None:
                print("Please upload a CSV file first!")
                return

            col_dropdown = widgets.Dropdown(
                options=list(self.data.columns),
                description='Select Column:',
                style={'description_width': 'initial'}
            )
            plot_button = widgets.Button(description="Generate Histogram", button_style="success")

            def plot_selected_hist(b):
                with self.output:
                    clear_output()
                    col = col_dropdown.value
                    if col:
                        if not pd.api.types.is_numeric_dtype(self.data[col]):
                            print(f"Column '{col}' is not numeric!")
                            return
                        plt.figure(figsize=(8, 6))
                        sns.histplot(self.data[col], kde=True, color='blue')
                        plt.title(f"Histogram of {col}")
                        plt.show()
                    else:
                        print("Please select a column!")

            plot_button.on_click(plot_selected_hist)

            display(widgets.VBox([col_dropdown, plot_button]))

    def plot_scatter(self, b):
        with self.output:
            clear_output()
            if self.data is None:
                print("Please upload a CSV file first!")
                return

            x_dropdown = widgets.Dropdown(
                options=list(self.data.columns),
                description='X-axis:',
                style={'description_width': 'initial'}
            )
            y_dropdown = widgets.Dropdown(
                options=list(self.data.columns),
                description='Y-axis:',
                style={'description_width': 'initial'}
            )
            plot_button = widgets.Button(description="Generate Scatter Plot", button_style="success")

            def plot_scatter_graph(b):
                with self.output:
                    clear_output()
                    x_col = x_dropdown.value
                    y_col = y_dropdown.value
                    if x_col and y_col:
                        if not pd.api.types.is_numeric_dtype(self.data[x_col]):
                            print(f"Column '{x_col}' is not numeric!")
                            return
                        if not pd.api.types.is_numeric_dtype(self.data[y_col]):
                            print(f"Column '{y_col}' is not numeric!")
                            return
                        plt.figure(figsize=(8, 6))
                        sns.scatterplot(data=self.data, x=x_col, y=y_col)
                        plt.title(f"Scatter Plot: {x_col} vs {y_col}")
                        plt.show()
                    else:
                        print("Please select both X and Y columns!")

            plot_button.on_click(plot_scatter_graph)

            display(widgets.VBox([x_dropdown, y_dropdown, plot_button]))

    def plot_heatmap(self, b):
        with self.output:
            clear_output()
            if self.data is None:
                print("Please upload a CSV file first!")
                return

            numeric_data = self.data.select_dtypes(include=[np.number])

            if numeric_data.empty:
                print("No numeric columns found for correlation heatmap!")
                return

            plt.figure(figsize=(10, 8))
            sns.heatmap(numeric_data.corr(), annot=True, cmap="coolwarm", fmt=".2f")
            plt.title("Correlation Heatmap of Numeric Columns")
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()
            plt.show()

    def plot_data_on_map(self, b):
        with self.output:
            clear_output()

            if self.data is None or "latitude" not in self.data.columns or "longitude" not in self.data.columns:
                print("Please ensure the dataset contains latitude and longitude columns!")
                return

            india_map = folium.Map(location=[20.5937, 78.9629], zoom_start=5)

            for _, row in self.data.iterrows():
                popup_text = "No Details"
                if "Title" in row:
                    popup_text = row['Title']
                elif len(row) > 0:
                    popup_text = str(row.iloc[0])

                folium.CircleMarker(
                    location=[row["latitude"], row["longitude"]],
                    radius=5,
                    color="blue",
                    fill=True,
                    fill_color="blue",
                    popup=popup_text,
                ).add_to(india_map)

            display(india_map)

analyzer = CSVAnalyzer()
