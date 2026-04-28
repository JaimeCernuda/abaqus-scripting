"""Render topology optimization results using VTK (headless, no ParaView).

Reads result.exo via netCDF4, creates VTK mesh, renders to PNG.
"""
import numpy as np
import netCDF4
import os

def exodus_to_vtk_and_render(exo_file, output_prefix="topology"):
    """Read Exodus file and render density field to PNG using VTK."""
    import vtk

    # Read Exodus data
    ds = netCDF4.Dataset(exo_file, "r")
    x = ds.variables["coordx"][:]
    y = ds.variables["coordy"][:]
    z = ds.variables["coordz"][:]
    conn = ds.variables["connect1"][:] - 1  # 0-based
    density = ds.variables["vals_nod_var1"][-1, :]  # last timestep
    ds.close()

    n_nodes = len(x)
    n_cells = len(conn)
    print(f"Loaded: {n_nodes} nodes, {n_cells} tets")
    print(f"Density range: [{density.min():.4f}, {density.max():.4f}]")

    # Create VTK unstructured grid
    points = vtk.vtkPoints()
    for i in range(n_nodes):
        points.InsertNextPoint(x[i], y[i], z[i])

    grid = vtk.vtkUnstructuredGrid()
    grid.SetPoints(points)

    for cell in conn:
        tet = vtk.vtkTetra()
        for j in range(4):
            tet.GetPointIds().SetId(j, int(cell[j]))
        grid.InsertNextCell(tet.GetCellType(), tet.GetPointIds())

    # Add density as point data
    density_arr = vtk.vtkDoubleArray()
    density_arr.SetName("Density")
    density_arr.SetNumberOfTuples(n_nodes)
    for i in range(n_nodes):
        density_arr.SetValue(i, density[i])
    grid.GetPointData().AddArray(density_arr)
    grid.GetPointData().SetActiveScalars("Density")

    # ============================================================
    # Render 1: Full density field (isometric view)
    # ============================================================
    mapper = vtk.vtkDataSetMapper()
    mapper.SetInputData(grid)
    mapper.SetScalarRange(0.0, 1.0)
    mapper.SetScalarModeToUsePointData()

    lut = vtk.vtkLookupTable()
    lut.SetHueRange(0.667, 0.0)  # blue to red
    lut.SetNumberOfColors(256)
    lut.Build()
    mapper.SetLookupTable(lut)

    actor = vtk.vtkActor()
    actor.SetMapper(mapper)

    renderer = vtk.vtkRenderer()
    renderer.AddActor(actor)
    renderer.SetBackground(1, 1, 1)

    # Scalar bar
    scalar_bar = vtk.vtkScalarBarActor()
    scalar_bar.SetLookupTable(lut)
    scalar_bar.SetTitle("Density")
    scalar_bar.SetNumberOfLabels(5)
    renderer.AddActor2D(scalar_bar)

    # Camera
    renderer.ResetCamera()
    camera = renderer.GetActiveCamera()
    camera.Elevation(20)
    camera.Azimuth(30)
    renderer.ResetCamera()

    # Offscreen render
    renWin = vtk.vtkRenderWindow()
    renWin.SetOffScreenRendering(1)
    renWin.SetSize(1600, 900)
    renWin.AddRenderer(renderer)
    renWin.Render()

    writer = vtk.vtkPNGWriter()
    w2i = vtk.vtkWindowToImageFilter()
    w2i.SetInput(renWin)
    w2i.Update()
    writer.SetInputConnection(w2i.GetOutputPort())
    writer.SetFileName(f"{output_prefix}_density.png")
    writer.Write()
    print(f"Saved: {output_prefix}_density.png")

    # ============================================================
    # Render 2: Thresholded (solid regions only)
    # ============================================================
    threshold = vtk.vtkThreshold()
    threshold.SetInputData(grid)
    threshold.SetInputArrayToProcess(0, 0, 0, vtk.vtkDataObject.FIELD_ASSOCIATION_POINTS, "Density")
    threshold.SetLowerThreshold(0.3)
    threshold.SetUpperThreshold(1.0)
    threshold.Update()

    mapper2 = vtk.vtkDataSetMapper()
    mapper2.SetInputConnection(threshold.GetOutputPort())
    mapper2.ScalarVisibilityOff()

    actor2 = vtk.vtkActor()
    actor2.SetMapper(mapper2)
    actor2.GetProperty().SetColor(0.7, 0.7, 0.85)

    renderer2 = vtk.vtkRenderer()
    renderer2.AddActor(actor2)
    renderer2.SetBackground(1, 1, 1)
    renderer2.ResetCamera()
    camera2 = renderer2.GetActiveCamera()
    camera2.Elevation(20)
    camera2.Azimuth(30)
    renderer2.ResetCamera()

    renWin2 = vtk.vtkRenderWindow()
    renWin2.SetOffScreenRendering(1)
    renWin2.SetSize(1600, 900)
    renWin2.AddRenderer(renderer2)
    renWin2.Render()

    w2i2 = vtk.vtkWindowToImageFilter()
    w2i2.SetInput(renWin2)
    w2i2.Update()
    writer2 = vtk.vtkPNGWriter()
    writer2.SetInputConnection(w2i2.GetOutputPort())
    writer2.SetFileName(f"{output_prefix}_shape.png")
    writer2.Write()
    print(f"Saved: {output_prefix}_shape.png")

    # ============================================================
    # Render 3: Side view (XY plane)
    # ============================================================
    camera2.SetPosition(50, 10, 100)
    camera2.SetFocalPoint(50, 10, 5)
    camera2.SetViewUp(0, 1, 0)
    renderer2.ResetCamera()
    renWin2.Render()

    w2i3 = vtk.vtkWindowToImageFilter()
    w2i3.SetInput(renWin2)
    w2i3.Update()
    writer3 = vtk.vtkPNGWriter()
    writer3.SetInputConnection(w2i3.GetOutputPort())
    writer3.SetFileName(f"{output_prefix}_side.png")
    writer3.Write()
    print(f"Saved: {output_prefix}_side.png")


if __name__ == "__main__":
    if os.path.exists("result.exo"):
        exodus_to_vtk_and_render("result.exo", "topology")
    else:
        print("result.exo not found")
