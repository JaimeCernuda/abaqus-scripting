# Field Troubleshooting

| Error | Cause | Solution |
|-------|-------|----------|
| "Field not defined" | Region doesn't match | Check region covers all nodes |
| "Cannot read ODB" | Wrong path or step name | Verify ODB exists and step name matches |
| "Incompatible mesh" | ODB mesh differs | Use same mesh or interpolation |
| "Temperature undefined" | Nodes without field value | Extend region or use default |

## Thermal-Structural Coupling
1. Run thermal analysis first -> saves .odb
2. In structural model: import temperature field from ODB
3. Use CoupledTempDisplacementStep for simultaneous coupling
