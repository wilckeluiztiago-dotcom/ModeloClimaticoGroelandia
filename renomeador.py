
import os
import shutil

base_path = "GRESM"

# Mapping: English -> Portuguese
translation = {
    "core_dynamics": {
        "stokes_solver": "solvedor_stokes",
        "rheology_glen": "reologia_glen",
        "viscosity_calculator": "calculadora_viscosidade",
        "mass_conservation": "conservacao_massa",
        "basal_friction": "friccao_basal",
        "thermal_solver": "solvedor_termico",
        "enthalpy_solver": "solvedor_entalpia",
        "calving_law": "lei_calving",
        "grounding_line": "linha_base",
        "damage_mechanics": "mecanica_dano",
        "anisotropy_evolution": "evolucao_anisotropia",
        "moving_mesh": "malha_movel",
        "stress_tensor": "tensor_tensao",
        "inversion_control": "controle_inversao",
        "time_integrator_dynamics": "integrador_temporal_dinamica"
    },
    "surface_processes": {
        "smb_accumulation": "smb_acumulo",
        "smb_ablation": "smb_ablacao",
        "snowpack_evolution": "evolucao_pacote_neve",
        "albedo_dynamic": "albedo_dinamico",
        "supra_hydrology": "hidrologia_supraglacial",
        "englacial_hydrology": "hidrologia_englacial",
        "sub_hydrology_channel": "hidrologia_sub_canal",
        "sub_hydrology_cavity": "hidrologia_sub_cavidade",
        "refreezing": "recongelamento",
        "runoff_router": "roteador_escoamento"
    },
    "boundary_conditions": {
        "atmos_coupler": "acoplador_atmosfera",
        "ocean_coupler": "acoplador_oceano",
        "submarine_melt": "derretimento_submarino",
        "sea_level_forcing": "forcante_nivel_mar",
        "geothermal_flux": "fluxo_geotermico",
        "solar_radiation": "radiacao_solar",
        "temperature_lapse": "taxa_gradiente_temp",
        "precipitation_downscaling": "downscaling_precipitacao",
        "ocean_salinity": "salinidade_oceano",
        "topography_reader": "leitor_topografia"
    },
    "geosphere_postglacial": {
        "gia_viscoelastic": "gia_viscoelastico",
        "elastic_rebound": "rebote_elastico",
        "relative_sea_level": "nivel_mar_relativo",
        "sediment_transport": "transporte_sedimento",
        "lithosphere_thermal": "termica_litosfera",
        "pedogenesis": "pedogenese",
        "vegetation_colonization": "colonizacao_vegetacao",
        "isostasy_coupler": "acoplador_isostasia"
    },
    "infrastructure": {
        "main_driver": "driver_principal",
        "config_parser": "leitor_config",
        "io_netcdf": "io_netcdf",
        "logger_system": "sistema_logger",
        "parallel_communicator": "comunicador_paralelo",
        "error_handler": "tratador_erro",
        "unit_testing_suite": "suite_testes"
    }
}

folder_translation = {
    "core_dynamics": "dinamica_central",
    "surface_processes": "processos_superficie",
    "boundary_conditions": "condicoes_contorno",
    "geosphere_postglacial": "geosfera_posglacial",
    "infrastructure": "infraestrutura"
}

def rename_all():
    # 1. Rename files inside folders
    for folder, files in translation.items():
        folder_path = os.path.join(base_path, folder)
        if not os.path.exists(folder_path):
            continue
            
        for eng, pt in files.items():
            old = os.path.join(folder_path, f"{eng}.py")
            new = os.path.join(folder_path, f"{pt}.py")
            if os.path.exists(old):
                try:
                    os.rename(old, new)
                    print(f"Renamed {old} -> {new}")
                except Exception as e:
                    print(f"Error renaming {old}: {e}")
    
    # 2. Rename folders
    for eng_folder, pt_folder in folder_translation.items():
        old_path = os.path.join(base_path, eng_folder)
        new_path = os.path.join(base_path, pt_folder)
        if os.path.exists(old_path):
            try:
                os.rename(old_path, new_path)
                print(f"Renamed folder {old_path} -> {new_path}")
            except Exception as e:
                print(f"Error renaming folder {old_path}: {e}")

if __name__ == "__main__":
    rename_all()
