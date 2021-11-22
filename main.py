from Scripts import *

def gen_all():
    population.gen_population_over_time()
    literacy.gen_literacy_over_time()
    hdi.gen_human_dev_idx_over_time()
    life_ex.gen_life_ex_over_time()
    missing_data.gen_missing_data()
    emissions.gen_share_co2_over_time_by_pop()
    emission_facetgrid.gen_share_emissions_vs_population()
    emission_facetgrid_selective.gen_selected_years_emission_vs_pop()
    print("done")

gen_all()