begin density_topology
    mesh_name mesh.exo
    output_name result.exo
    initial_density_value 0.5
end

begin helmholtz_filter
    filter_radius 8.0
end

begin constraint volume
    active true
    app platoanalyze
    criterion platoanalyze
    input_files analyze_volume.xml
    is_linear true
    constraint_value 68000.0
    constraint_type equal_to
end

begin objective lc1
    active true
    app platoanalyze
    criterion platoanalyze
    input_files analyze_lc1.xml
    aggregation_weight 0.5
    number_of_processors 1
end

begin objective lc2
    active true
    app platoanalyze
    criterion platoanalyze
    input_files analyze_lc2.xml
    aggregation_weight 0.25
    number_of_processors 1
end

begin objective lc3
    active true
    app platoanalyze
    criterion platoanalyze
    input_files analyze_lc3.xml
    aggregation_weight 0.25
    number_of_processors 1
end

begin rol_optimization
    max_iterations 50
end
