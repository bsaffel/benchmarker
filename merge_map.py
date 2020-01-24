import shutil

map_dir = 'Benchmarker - Simulacrum LE.SC2Map'
mod_dir = 'Benchmarker.SC2Mod'

working_dir = 'target/' + map_dir


text_data = 'enUS.SC2Data/'

# Copy in the base map resources
shutil.copytree(map_dir, working_dir)
# Add in the enUS textual data
shutil.copytree(mod_dir + text_data, working_dir + text_data)

# Merge/Update the DocumentInfo xml

# Merge the Preload xml

# Merge the PreloadAssetDB text