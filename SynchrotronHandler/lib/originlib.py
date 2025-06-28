# -*- coding: utf-8 -*-
'''
Library of helper functions for interacting with OriginPro,
including data upload and graph creation.
'''


import pandas as pd
import originpro as op
import os

def uploadData(tth, intensity, error, tempres):    
    # Create DataFrame
    df = pd.DataFrame({
        'TTh': tth,
        'Intensity': intensity,
        'Error': error,
        'T/P': tempres    
    })

    # Create a new worksheet and load the data
    wks = op.new_sheet()
    wks.from_df(df)


def contourFill():
    graph_name = "ContourGraph"

    # Select the active worksheet
    wks = op.find_sheet()

    # Set column layout as XYZ
    wks.cols_axis('xyz')

    # Create a Contour graph with X axis: col 0, Y axis: col 3, Z axis: col 1
    graph = op.new_graph(template='TriContour', lname=graph_name)
    plot = graph[0].add_plot(wks, colx=0, coly=3, colz=1, type=243)
    plot.colormap = 'Maple.pal'
    graph[0].rescale()
