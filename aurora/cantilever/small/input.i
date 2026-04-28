begin density_topology
    mesh_name mesh.exo
    output_name result.exo
    initial_density_value 0.5
end

begin helmholtz_filter
    filter_radius 15.0
end

begin constraint volume
    active true
    app platoanalyze
    criterion platoanalyze
    input_files analyze_volume.xml
    is_linear true
    constraint_value 6000.0
    constraint_type equal_to
end

begin objective compliance
    active true
    app platoanalyze
    criterion platoanalyze
    input_files analyze_compliance.xml
    aggregation_weight 1.0
end

begin rol_optimization
    max_iterations 50
end
