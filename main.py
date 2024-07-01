"""
Author:       Roberto Chiosa
Copyright:    Roberto Chiosa, © 2024
Email:        roberto.chiosa@pinvision.it

Created:      01/07/24
Script Name:  main.py
Path:         

Script Description:


Notes:
"""
import os

import pandas as pd
from jinja2 import Environment, FileSystemLoader

from utils import plot_static, plot_dynamic

if __name__ == '__main__':
    # Set up variables
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    path_to_templates = os.path.join(cur_dir, 'templates')
    path_to_reports = os.path.join(cur_dir, "output")
    path_to_data = os.path.join(cur_dir, "data")

    # Define the dataset and template
    dataset_name = "data.csv"
    template_name = 'base.html'
    report_name = "example_report.html"

    # Set up the Jinja2 environment for report
    env = Environment(loader=FileSystemLoader(path_to_templates))
    template = env.get_template(template_name)

    # Load data and make plots
    data = pd.read_csv(os.path.join(path_to_data, dataset_name))
    static_plot = plot_static(data)
    dynamic_plot = plot_dynamic(data)

    # prepare input for report

    # static images require path to the asset
    static_img_path = os.path.join(path_to_reports, f'static_img.png')

    # static plots must be saved and then loaded in the html
    static_plot_path = os.path.join(path_to_reports, f'static_{dataset_name}.png')
    static_plot.savefig(static_plot_path)

    # dynamic plots don't need to be saved but can be embedded directly
    dynamic_plot_html = dynamic_plot.to_html(full_html=False)

    # assemble output
    context = {
        'title': 'Fault Detection and Diagnosis report',
        'subtitle': f'Report for the {dataset_name} dataset',
        'description': {
            'title': 'Dataset description',
            'content': 'This is the description of the report'
        },
        'energy': {
            'title': 'Energy section',
            'content': f'The heat pump has a COP of',
            'img_table': static_img_path,
            'cop': static_plot_path,
            'plotly': dynamic_plot_html
        },
        'components': [
            {
                'title': 'Component 1',
                'content': 'This is the description of the report'
            },
            {
                'title': 'Component 2',
                'content': 'This is the description of the report'
            },
            {
                'title': 'Component 3',
                'content': 'This is the description of the report'
            },
        ],
        'footer_text': '© Roberto',
    }

    # Render the template with the data
    html_content = template.render(context)

    # Save the rendered HTML to a file (optional, for inspection)
    with open(os.path.join(path_to_reports, report_name), 'w') as file:
        file.write(html_content)
