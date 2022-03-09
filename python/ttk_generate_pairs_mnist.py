# trace generated using paraview version 5.6.0
#
# To ensure correct image size when batch processing, please search 
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

import sys

name = sys.argv[1]

full_path = sys.argv[2]

# create a new 'XML Image Data Reader'
imagevti = XMLImageDataReader(FileName=[full_path+'/'+name])
imagevti.PointArrayStatus = ['field']

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1427, 618]

# show data in view
imagevtiDisplay = Show(imagevti, renderView1)

# get color transfer function/color map for 'field'
fieldLUT = GetColorTransferFunction('field')

# get opacity transfer function/opacity map for 'field'
fieldPWF = GetOpacityTransferFunction('field')

# trace defaults for the display properties.
imagevtiDisplay.Representation = 'Slice'
imagevtiDisplay.ColorArrayName = ['POINTS', 'field']
imagevtiDisplay.LookupTable = fieldLUT
imagevtiDisplay.EdgeColor = [0.0, 0.0, 0.0]
imagevtiDisplay.OSPRayScaleArray = 'field'
imagevtiDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
imagevtiDisplay.SelectOrientationVectors = 'None'
imagevtiDisplay.ScaleFactor = 2.7
imagevtiDisplay.SelectScaleArray = 'None'
imagevtiDisplay.GlyphType = 'Arrow'
imagevtiDisplay.GlyphTableIndexArray = 'None'
imagevtiDisplay.GaussianRadius = 0.135
imagevtiDisplay.SetScaleArray = ['POINTS', 'field']
imagevtiDisplay.ScaleTransferFunction = 'PiecewiseFunction'
imagevtiDisplay.OpacityArray = ['POINTS', 'field']
imagevtiDisplay.OpacityTransferFunction = 'PiecewiseFunction'
imagevtiDisplay.DataAxesGrid = 'GridAxesRepresentation'
imagevtiDisplay.SelectionCellLabelFontFile = ''
imagevtiDisplay.SelectionPointLabelFontFile = ''
imagevtiDisplay.PolarAxes = 'PolarAxesRepresentation'
imagevtiDisplay.ScalarOpacityUnitDistance = 4.2426406871192865
imagevtiDisplay.ScalarOpacityFunction = fieldPWF

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
imagevtiDisplay.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
imagevtiDisplay.DataAxesGrid.XTitleFontFile = ''
imagevtiDisplay.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
imagevtiDisplay.DataAxesGrid.YTitleFontFile = ''
imagevtiDisplay.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
imagevtiDisplay.DataAxesGrid.ZTitleFontFile = ''
imagevtiDisplay.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
imagevtiDisplay.DataAxesGrid.XLabelFontFile = ''
imagevtiDisplay.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
imagevtiDisplay.DataAxesGrid.YLabelFontFile = ''
imagevtiDisplay.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]
imagevtiDisplay.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
imagevtiDisplay.PolarAxes.PolarAxisTitleColor = [0.0, 0.0, 0.0]
imagevtiDisplay.PolarAxes.PolarAxisTitleFontFile = ''
imagevtiDisplay.PolarAxes.PolarAxisLabelColor = [0.0, 0.0, 0.0]
imagevtiDisplay.PolarAxes.PolarAxisLabelFontFile = ''
imagevtiDisplay.PolarAxes.LastRadialAxisTextColor = [0.0, 0.0, 0.0]
imagevtiDisplay.PolarAxes.LastRadialAxisTextFontFile = ''
imagevtiDisplay.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 0.0, 0.0]
imagevtiDisplay.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

#changing interaction mode based on data extents
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [13.5, 13.5, 10000.0]
renderView1.CameraFocalPoint = [13.5, 13.5, 0.0]

# show color bar/color legend
imagevtiDisplay.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'TTK FG_PersistentHomology'
tTKFG_PersistentHomology1 = TTKFG_PersistentHomology(Input=imagevti)
tTKFG_PersistentHomology1.ScalarField = 'field'

# show data in view
tTKFG_PersistentHomology1Display = Show(tTKFG_PersistentHomology1, renderView1)

# trace defaults for the display properties.
tTKFG_PersistentHomology1Display.Representation = 'Surface'
tTKFG_PersistentHomology1Display.ColorArrayName = [None, '']
tTKFG_PersistentHomology1Display.EdgeColor = [0.0, 0.0, 0.0]
tTKFG_PersistentHomology1Display.OSPRayScaleArray = 'CellDimension'
tTKFG_PersistentHomology1Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKFG_PersistentHomology1Display.SelectOrientationVectors = 'CellDimension'
tTKFG_PersistentHomology1Display.ScaleFactor = 1.7833333492279053
tTKFG_PersistentHomology1Display.SelectScaleArray = 'CellDimension'
tTKFG_PersistentHomology1Display.GlyphType = 'Arrow'
tTKFG_PersistentHomology1Display.GlyphTableIndexArray = 'CellDimension'
tTKFG_PersistentHomology1Display.GaussianRadius = 0.08916666746139526
tTKFG_PersistentHomology1Display.SetScaleArray = ['POINTS', 'CellDimension']
tTKFG_PersistentHomology1Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKFG_PersistentHomology1Display.OpacityArray = ['POINTS', 'CellDimension']
tTKFG_PersistentHomology1Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKFG_PersistentHomology1Display.DataAxesGrid = 'GridAxesRepresentation'
tTKFG_PersistentHomology1Display.SelectionCellLabelFontFile = ''
tTKFG_PersistentHomology1Display.SelectionPointLabelFontFile = ''
tTKFG_PersistentHomology1Display.PolarAxes = 'PolarAxesRepresentation'
tTKFG_PersistentHomology1Display.ScalarOpacityUnitDistance = 7.6966002875928465

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
tTKFG_PersistentHomology1Display.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
tTKFG_PersistentHomology1Display.DataAxesGrid.XTitleFontFile = ''
tTKFG_PersistentHomology1Display.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
tTKFG_PersistentHomology1Display.DataAxesGrid.YTitleFontFile = ''
tTKFG_PersistentHomology1Display.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
tTKFG_PersistentHomology1Display.DataAxesGrid.ZTitleFontFile = ''
tTKFG_PersistentHomology1Display.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
tTKFG_PersistentHomology1Display.DataAxesGrid.XLabelFontFile = ''
tTKFG_PersistentHomology1Display.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
tTKFG_PersistentHomology1Display.DataAxesGrid.YLabelFontFile = ''
tTKFG_PersistentHomology1Display.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]
tTKFG_PersistentHomology1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
tTKFG_PersistentHomology1Display.PolarAxes.PolarAxisTitleColor = [0.0, 0.0, 0.0]
tTKFG_PersistentHomology1Display.PolarAxes.PolarAxisTitleFontFile = ''
tTKFG_PersistentHomology1Display.PolarAxes.PolarAxisLabelColor = [0.0, 0.0, 0.0]
tTKFG_PersistentHomology1Display.PolarAxes.PolarAxisLabelFontFile = ''
tTKFG_PersistentHomology1Display.PolarAxes.LastRadialAxisTextColor = [0.0, 0.0, 0.0]
tTKFG_PersistentHomology1Display.PolarAxes.LastRadialAxisTextFontFile = ''
tTKFG_PersistentHomology1Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 0.0, 0.0]
tTKFG_PersistentHomology1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# hide data in view
Hide(imagevti, renderView1)

# show data in view
tTKFG_PersistentHomology1Display_1 = Show(OutputPort(tTKFG_PersistentHomology1, 1), renderView1)

# trace defaults for the display properties.
tTKFG_PersistentHomology1Display_1.Representation = 'Surface'
tTKFG_PersistentHomology1Display_1.ColorArrayName = [None, '']
tTKFG_PersistentHomology1Display_1.EdgeColor = [0.0, 0.0, 0.0]
tTKFG_PersistentHomology1Display_1.OSPRayScaleArray = 'Filtration'
tTKFG_PersistentHomology1Display_1.OSPRayScaleFunction = 'PiecewiseFunction'
tTKFG_PersistentHomology1Display_1.SelectOrientationVectors = 'Filtration'
tTKFG_PersistentHomology1Display_1.ScaleFactor = 0.1
tTKFG_PersistentHomology1Display_1.SelectScaleArray = 'Filtration'
tTKFG_PersistentHomology1Display_1.GlyphType = 'Arrow'
tTKFG_PersistentHomology1Display_1.GlyphTableIndexArray = 'Filtration'
tTKFG_PersistentHomology1Display_1.GaussianRadius = 0.005
tTKFG_PersistentHomology1Display_1.SetScaleArray = ['POINTS', 'Filtration']
tTKFG_PersistentHomology1Display_1.ScaleTransferFunction = 'PiecewiseFunction'
tTKFG_PersistentHomology1Display_1.OpacityArray = ['POINTS', 'Filtration']
tTKFG_PersistentHomology1Display_1.OpacityTransferFunction = 'PiecewiseFunction'
tTKFG_PersistentHomology1Display_1.DataAxesGrid = 'GridAxesRepresentation'
tTKFG_PersistentHomology1Display_1.SelectionCellLabelFontFile = ''
tTKFG_PersistentHomology1Display_1.SelectionPointLabelFontFile = ''
tTKFG_PersistentHomology1Display_1.PolarAxes = 'PolarAxesRepresentation'
tTKFG_PersistentHomology1Display_1.ScalarOpacityUnitDistance = 1.4142135623730951

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
tTKFG_PersistentHomology1Display_1.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
tTKFG_PersistentHomology1Display_1.DataAxesGrid.XTitleFontFile = ''
tTKFG_PersistentHomology1Display_1.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
tTKFG_PersistentHomology1Display_1.DataAxesGrid.YTitleFontFile = ''
tTKFG_PersistentHomology1Display_1.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
tTKFG_PersistentHomology1Display_1.DataAxesGrid.ZTitleFontFile = ''
tTKFG_PersistentHomology1Display_1.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
tTKFG_PersistentHomology1Display_1.DataAxesGrid.XLabelFontFile = ''
tTKFG_PersistentHomology1Display_1.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
tTKFG_PersistentHomology1Display_1.DataAxesGrid.YLabelFontFile = ''
tTKFG_PersistentHomology1Display_1.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]
tTKFG_PersistentHomology1Display_1.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
tTKFG_PersistentHomology1Display_1.PolarAxes.PolarAxisTitleColor = [0.0, 0.0, 0.0]
tTKFG_PersistentHomology1Display_1.PolarAxes.PolarAxisTitleFontFile = ''
tTKFG_PersistentHomology1Display_1.PolarAxes.PolarAxisLabelColor = [0.0, 0.0, 0.0]
tTKFG_PersistentHomology1Display_1.PolarAxes.PolarAxisLabelFontFile = ''
tTKFG_PersistentHomology1Display_1.PolarAxes.LastRadialAxisTextColor = [0.0, 0.0, 0.0]
tTKFG_PersistentHomology1Display_1.PolarAxes.LastRadialAxisTextFontFile = ''
tTKFG_PersistentHomology1Display_1.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 0.0, 0.0]
tTKFG_PersistentHomology1Display_1.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# hide data in view
Hide(imagevti, renderView1)

# show data in view
tTKFG_PersistentHomology1Display_2 = Show(OutputPort(tTKFG_PersistentHomology1, 2), renderView1)

# trace defaults for the display properties.
tTKFG_PersistentHomology1Display_2.Representation = 'Surface'
tTKFG_PersistentHomology1Display_2.ColorArrayName = [None, '']
tTKFG_PersistentHomology1Display_2.EdgeColor = [0.0, 0.0, 0.0]
tTKFG_PersistentHomology1Display_2.OSPRayScaleArray = 'CellDimension'
tTKFG_PersistentHomology1Display_2.OSPRayScaleFunction = 'PiecewiseFunction'
tTKFG_PersistentHomology1Display_2.SelectOrientationVectors = 'CellDimension'
tTKFG_PersistentHomology1Display_2.ScaleFactor = 0.1
tTKFG_PersistentHomology1Display_2.SelectScaleArray = 'CellDimension'
tTKFG_PersistentHomology1Display_2.GlyphType = 'Arrow'
tTKFG_PersistentHomology1Display_2.GlyphTableIndexArray = 'CellDimension'
tTKFG_PersistentHomology1Display_2.GaussianRadius = 0.005
tTKFG_PersistentHomology1Display_2.SetScaleArray = ['POINTS', 'CellDimension']
tTKFG_PersistentHomology1Display_2.ScaleTransferFunction = 'PiecewiseFunction'
tTKFG_PersistentHomology1Display_2.OpacityArray = ['POINTS', 'CellDimension']
tTKFG_PersistentHomology1Display_2.OpacityTransferFunction = 'PiecewiseFunction'
tTKFG_PersistentHomology1Display_2.DataAxesGrid = 'GridAxesRepresentation'
tTKFG_PersistentHomology1Display_2.SelectionCellLabelFontFile = ''
tTKFG_PersistentHomology1Display_2.SelectionPointLabelFontFile = ''
tTKFG_PersistentHomology1Display_2.PolarAxes = 'PolarAxesRepresentation'
tTKFG_PersistentHomology1Display_2.ScalarOpacityUnitDistance = 0.0

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
tTKFG_PersistentHomology1Display_2.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
tTKFG_PersistentHomology1Display_2.DataAxesGrid.XTitleFontFile = ''
tTKFG_PersistentHomology1Display_2.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
tTKFG_PersistentHomology1Display_2.DataAxesGrid.YTitleFontFile = ''
tTKFG_PersistentHomology1Display_2.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
tTKFG_PersistentHomology1Display_2.DataAxesGrid.ZTitleFontFile = ''
tTKFG_PersistentHomology1Display_2.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
tTKFG_PersistentHomology1Display_2.DataAxesGrid.XLabelFontFile = ''
tTKFG_PersistentHomology1Display_2.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
tTKFG_PersistentHomology1Display_2.DataAxesGrid.YLabelFontFile = ''
tTKFG_PersistentHomology1Display_2.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]
tTKFG_PersistentHomology1Display_2.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
tTKFG_PersistentHomology1Display_2.PolarAxes.PolarAxisTitleColor = [0.0, 0.0, 0.0]
tTKFG_PersistentHomology1Display_2.PolarAxes.PolarAxisTitleFontFile = ''
tTKFG_PersistentHomology1Display_2.PolarAxes.PolarAxisLabelColor = [0.0, 0.0, 0.0]
tTKFG_PersistentHomology1Display_2.PolarAxes.PolarAxisLabelFontFile = ''
tTKFG_PersistentHomology1Display_2.PolarAxes.LastRadialAxisTextColor = [0.0, 0.0, 0.0]
tTKFG_PersistentHomology1Display_2.PolarAxes.LastRadialAxisTextFontFile = ''
tTKFG_PersistentHomology1Display_2.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 0.0, 0.0]
tTKFG_PersistentHomology1Display_2.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# hide data in view
Hide(imagevti, renderView1)

# show data in view
tTKFG_PersistentHomology1Display_3 = Show(OutputPort(tTKFG_PersistentHomology1, 3), renderView1)

# trace defaults for the display properties.
tTKFG_PersistentHomology1Display_3.Representation = 'Surface'
tTKFG_PersistentHomology1Display_3.ColorArrayName = [None, '']
tTKFG_PersistentHomology1Display_3.EdgeColor = [0.0, 0.0, 0.0]
tTKFG_PersistentHomology1Display_3.OSPRayScaleFunction = 'PiecewiseFunction'
tTKFG_PersistentHomology1Display_3.SelectOrientationVectors = 'None'
tTKFG_PersistentHomology1Display_3.ScaleFactor = -2.0000000000000002e+298
tTKFG_PersistentHomology1Display_3.SelectScaleArray = 'None'
tTKFG_PersistentHomology1Display_3.GlyphType = 'Arrow'
tTKFG_PersistentHomology1Display_3.GlyphTableIndexArray = 'None'
tTKFG_PersistentHomology1Display_3.GaussianRadius = -1e+297
tTKFG_PersistentHomology1Display_3.SetScaleArray = [None, '']
tTKFG_PersistentHomology1Display_3.ScaleTransferFunction = 'PiecewiseFunction'
tTKFG_PersistentHomology1Display_3.OpacityArray = [None, '']
tTKFG_PersistentHomology1Display_3.OpacityTransferFunction = 'PiecewiseFunction'
tTKFG_PersistentHomology1Display_3.DataAxesGrid = 'GridAxesRepresentation'
tTKFG_PersistentHomology1Display_3.SelectionCellLabelFontFile = ''
tTKFG_PersistentHomology1Display_3.SelectionPointLabelFontFile = ''
tTKFG_PersistentHomology1Display_3.PolarAxes = 'PolarAxesRepresentation'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
tTKFG_PersistentHomology1Display_3.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
tTKFG_PersistentHomology1Display_3.DataAxesGrid.XTitleFontFile = ''
tTKFG_PersistentHomology1Display_3.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
tTKFG_PersistentHomology1Display_3.DataAxesGrid.YTitleFontFile = ''
tTKFG_PersistentHomology1Display_3.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
tTKFG_PersistentHomology1Display_3.DataAxesGrid.ZTitleFontFile = ''
tTKFG_PersistentHomology1Display_3.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
tTKFG_PersistentHomology1Display_3.DataAxesGrid.XLabelFontFile = ''
tTKFG_PersistentHomology1Display_3.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
tTKFG_PersistentHomology1Display_3.DataAxesGrid.YLabelFontFile = ''
tTKFG_PersistentHomology1Display_3.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]
tTKFG_PersistentHomology1Display_3.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
tTKFG_PersistentHomology1Display_3.PolarAxes.PolarAxisTitleColor = [0.0, 0.0, 0.0]
tTKFG_PersistentHomology1Display_3.PolarAxes.PolarAxisTitleFontFile = ''
tTKFG_PersistentHomology1Display_3.PolarAxes.PolarAxisLabelColor = [0.0, 0.0, 0.0]
tTKFG_PersistentHomology1Display_3.PolarAxes.PolarAxisLabelFontFile = ''
tTKFG_PersistentHomology1Display_3.PolarAxes.LastRadialAxisTextColor = [0.0, 0.0, 0.0]
tTKFG_PersistentHomology1Display_3.PolarAxes.LastRadialAxisTextFontFile = ''
tTKFG_PersistentHomology1Display_3.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 0.0, 0.0]
tTKFG_PersistentHomology1Display_3.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# hide data in view
Hide(imagevti, renderView1)

# show data in view
tTKFG_PersistentHomology1Display_4 = Show(OutputPort(tTKFG_PersistentHomology1, 4), renderView1)

# trace defaults for the display properties.
tTKFG_PersistentHomology1Display_4.Representation = 'Surface'
tTKFG_PersistentHomology1Display_4.ColorArrayName = [None, '']
tTKFG_PersistentHomology1Display_4.EdgeColor = [0.0, 0.0, 0.0]
tTKFG_PersistentHomology1Display_4.OSPRayScaleFunction = 'PiecewiseFunction'
tTKFG_PersistentHomology1Display_4.SelectOrientationVectors = 'None'
tTKFG_PersistentHomology1Display_4.ScaleFactor = -2.0000000000000002e+298
tTKFG_PersistentHomology1Display_4.SelectScaleArray = 'None'
tTKFG_PersistentHomology1Display_4.GlyphType = 'Arrow'
tTKFG_PersistentHomology1Display_4.GlyphTableIndexArray = 'None'
tTKFG_PersistentHomology1Display_4.GaussianRadius = -1e+297
tTKFG_PersistentHomology1Display_4.SetScaleArray = [None, '']
tTKFG_PersistentHomology1Display_4.ScaleTransferFunction = 'PiecewiseFunction'
tTKFG_PersistentHomology1Display_4.OpacityArray = [None, '']
tTKFG_PersistentHomology1Display_4.OpacityTransferFunction = 'PiecewiseFunction'
tTKFG_PersistentHomology1Display_4.DataAxesGrid = 'GridAxesRepresentation'
tTKFG_PersistentHomology1Display_4.SelectionCellLabelFontFile = ''
tTKFG_PersistentHomology1Display_4.SelectionPointLabelFontFile = ''
tTKFG_PersistentHomology1Display_4.PolarAxes = 'PolarAxesRepresentation'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
tTKFG_PersistentHomology1Display_4.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
tTKFG_PersistentHomology1Display_4.DataAxesGrid.XTitleFontFile = ''
tTKFG_PersistentHomology1Display_4.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
tTKFG_PersistentHomology1Display_4.DataAxesGrid.YTitleFontFile = ''
tTKFG_PersistentHomology1Display_4.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
tTKFG_PersistentHomology1Display_4.DataAxesGrid.ZTitleFontFile = ''
tTKFG_PersistentHomology1Display_4.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
tTKFG_PersistentHomology1Display_4.DataAxesGrid.XLabelFontFile = ''
tTKFG_PersistentHomology1Display_4.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
tTKFG_PersistentHomology1Display_4.DataAxesGrid.YLabelFontFile = ''
tTKFG_PersistentHomology1Display_4.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]
tTKFG_PersistentHomology1Display_4.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
tTKFG_PersistentHomology1Display_4.PolarAxes.PolarAxisTitleColor = [0.0, 0.0, 0.0]
tTKFG_PersistentHomology1Display_4.PolarAxes.PolarAxisTitleFontFile = ''
tTKFG_PersistentHomology1Display_4.PolarAxes.PolarAxisLabelColor = [0.0, 0.0, 0.0]
tTKFG_PersistentHomology1Display_4.PolarAxes.PolarAxisLabelFontFile = ''
tTKFG_PersistentHomology1Display_4.PolarAxes.LastRadialAxisTextColor = [0.0, 0.0, 0.0]
tTKFG_PersistentHomology1Display_4.PolarAxes.LastRadialAxisTextFontFile = ''
tTKFG_PersistentHomology1Display_4.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 0.0, 0.0]
tTKFG_PersistentHomology1Display_4.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# hide data in view
Hide(imagevti, renderView1)

# show data in view
tTKFG_PersistentHomology1Display_5 = Show(OutputPort(tTKFG_PersistentHomology1, 5), renderView1)

# trace defaults for the display properties.
tTKFG_PersistentHomology1Display_5.Representation = 'Surface'
tTKFG_PersistentHomology1Display_5.ColorArrayName = [None, '']
tTKFG_PersistentHomology1Display_5.EdgeColor = [0.0, 0.0, 0.0]
tTKFG_PersistentHomology1Display_5.OSPRayScaleFunction = 'PiecewiseFunction'
tTKFG_PersistentHomology1Display_5.SelectOrientationVectors = 'None'
tTKFG_PersistentHomology1Display_5.ScaleFactor = -2.0000000000000002e+298
tTKFG_PersistentHomology1Display_5.SelectScaleArray = 'None'
tTKFG_PersistentHomology1Display_5.GlyphType = 'Arrow'
tTKFG_PersistentHomology1Display_5.GlyphTableIndexArray = 'None'
tTKFG_PersistentHomology1Display_5.GaussianRadius = -1e+297
tTKFG_PersistentHomology1Display_5.SetScaleArray = [None, '']
tTKFG_PersistentHomology1Display_5.ScaleTransferFunction = 'PiecewiseFunction'
tTKFG_PersistentHomology1Display_5.OpacityArray = [None, '']
tTKFG_PersistentHomology1Display_5.OpacityTransferFunction = 'PiecewiseFunction'
tTKFG_PersistentHomology1Display_5.DataAxesGrid = 'GridAxesRepresentation'
tTKFG_PersistentHomology1Display_5.SelectionCellLabelFontFile = ''
tTKFG_PersistentHomology1Display_5.SelectionPointLabelFontFile = ''
tTKFG_PersistentHomology1Display_5.PolarAxes = 'PolarAxesRepresentation'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
tTKFG_PersistentHomology1Display_5.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
tTKFG_PersistentHomology1Display_5.DataAxesGrid.XTitleFontFile = ''
tTKFG_PersistentHomology1Display_5.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
tTKFG_PersistentHomology1Display_5.DataAxesGrid.YTitleFontFile = ''
tTKFG_PersistentHomology1Display_5.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
tTKFG_PersistentHomology1Display_5.DataAxesGrid.ZTitleFontFile = ''
tTKFG_PersistentHomology1Display_5.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
tTKFG_PersistentHomology1Display_5.DataAxesGrid.XLabelFontFile = ''
tTKFG_PersistentHomology1Display_5.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
tTKFG_PersistentHomology1Display_5.DataAxesGrid.YLabelFontFile = ''
tTKFG_PersistentHomology1Display_5.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]
tTKFG_PersistentHomology1Display_5.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
tTKFG_PersistentHomology1Display_5.PolarAxes.PolarAxisTitleColor = [0.0, 0.0, 0.0]
tTKFG_PersistentHomology1Display_5.PolarAxes.PolarAxisTitleFontFile = ''
tTKFG_PersistentHomology1Display_5.PolarAxes.PolarAxisLabelColor = [0.0, 0.0, 0.0]
tTKFG_PersistentHomology1Display_5.PolarAxes.PolarAxisLabelFontFile = ''
tTKFG_PersistentHomology1Display_5.PolarAxes.LastRadialAxisTextColor = [0.0, 0.0, 0.0]
tTKFG_PersistentHomology1Display_5.PolarAxes.LastRadialAxisTextFontFile = ''
tTKFG_PersistentHomology1Display_5.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 0.0, 0.0]
tTKFG_PersistentHomology1Display_5.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# hide data in view
Hide(imagevti, renderView1)

# show data in view
tTKFG_PersistentHomology1Display_6 = Show(OutputPort(tTKFG_PersistentHomology1, 6), renderView1)

# trace defaults for the display properties.
tTKFG_PersistentHomology1Display_6.Representation = 'Surface'
tTKFG_PersistentHomology1Display_6.ColorArrayName = [None, '']
tTKFG_PersistentHomology1Display_6.EdgeColor = [0.0, 0.0, 0.0]
tTKFG_PersistentHomology1Display_6.OSPRayScaleFunction = 'PiecewiseFunction'
tTKFG_PersistentHomology1Display_6.SelectOrientationVectors = 'None'
tTKFG_PersistentHomology1Display_6.ScaleFactor = -2.0000000000000002e+298
tTKFG_PersistentHomology1Display_6.SelectScaleArray = 'None'
tTKFG_PersistentHomology1Display_6.GlyphType = 'Arrow'
tTKFG_PersistentHomology1Display_6.GlyphTableIndexArray = 'None'
tTKFG_PersistentHomology1Display_6.GaussianRadius = -1e+297
tTKFG_PersistentHomology1Display_6.SetScaleArray = [None, '']
tTKFG_PersistentHomology1Display_6.ScaleTransferFunction = 'PiecewiseFunction'
tTKFG_PersistentHomology1Display_6.OpacityArray = [None, '']
tTKFG_PersistentHomology1Display_6.OpacityTransferFunction = 'PiecewiseFunction'
tTKFG_PersistentHomology1Display_6.DataAxesGrid = 'GridAxesRepresentation'
tTKFG_PersistentHomology1Display_6.SelectionCellLabelFontFile = ''
tTKFG_PersistentHomology1Display_6.SelectionPointLabelFontFile = ''
tTKFG_PersistentHomology1Display_6.PolarAxes = 'PolarAxesRepresentation'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
tTKFG_PersistentHomology1Display_6.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
tTKFG_PersistentHomology1Display_6.DataAxesGrid.XTitleFontFile = ''
tTKFG_PersistentHomology1Display_6.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
tTKFG_PersistentHomology1Display_6.DataAxesGrid.YTitleFontFile = ''
tTKFG_PersistentHomology1Display_6.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
tTKFG_PersistentHomology1Display_6.DataAxesGrid.ZTitleFontFile = ''
tTKFG_PersistentHomology1Display_6.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
tTKFG_PersistentHomology1Display_6.DataAxesGrid.XLabelFontFile = ''
tTKFG_PersistentHomology1Display_6.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
tTKFG_PersistentHomology1Display_6.DataAxesGrid.YLabelFontFile = ''
tTKFG_PersistentHomology1Display_6.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]
tTKFG_PersistentHomology1Display_6.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
tTKFG_PersistentHomology1Display_6.PolarAxes.PolarAxisTitleColor = [0.0, 0.0, 0.0]
tTKFG_PersistentHomology1Display_6.PolarAxes.PolarAxisTitleFontFile = ''
tTKFG_PersistentHomology1Display_6.PolarAxes.PolarAxisLabelColor = [0.0, 0.0, 0.0]
tTKFG_PersistentHomology1Display_6.PolarAxes.PolarAxisLabelFontFile = ''
tTKFG_PersistentHomology1Display_6.PolarAxes.LastRadialAxisTextColor = [0.0, 0.0, 0.0]
tTKFG_PersistentHomology1Display_6.PolarAxes.LastRadialAxisTextFontFile = ''
tTKFG_PersistentHomology1Display_6.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 0.0, 0.0]
tTKFG_PersistentHomology1Display_6.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# hide data in view
Hide(imagevti, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on tTKFG_PersistentHomology1
tTKFG_PersistentHomology1.Extract1cycles = 1

# update the view to ensure updated data information
renderView1.Update()



number = sys.argv[3]

id = sys.argv[4]



# set active source
SetActiveSource(tTKFG_PersistentHomology1)

# save data
SaveData(full_path+'/data/mnist/'+number+'/'+id+'_pd.vtk', proxy=tTKFG_PersistentHomology1)

# set active source
SetActiveSource(tTKFG_PersistentHomology1)

# get active source.
tTKFG_PersistentHomology1_1 = GetActiveSource()

# save data
SaveData(full_path+'/data/mnist/'+number+'/'+id+'_cycles.vtk', proxy=OutputPort(tTKFG_PersistentHomology1_1, 3))
