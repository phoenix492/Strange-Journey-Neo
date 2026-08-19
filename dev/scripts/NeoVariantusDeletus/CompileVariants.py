from tomlkit.toml_file import TOMLFile
import Typelists


def injectVanillaWoods(templateString):
    outputArray = []
    for woodtype in Typelists.vanilla_woods:
        outputArray.append(templateString.format(wood = woodtype))
    return outputArray

def transform_quark_carpets(variant_id):
    variant_id = variant_id.strip()
    modid,item = variant_id.split(':')
    woodtype = item.removesuffix("_leaf_carpet")
    return f"unique,{modid}:{woodtype}_leaves,{variant_id}"

def transform_quark_hedges(variant_id):
    variant_id = variant_id.strip()
    modid,item = variant_id.split(':')
    woodtype = item.removesuffix("_hedge")
    return f"unique2,{modid}:{woodtype}_leaves,{variant_id}"

def transform_everycomp_carpets(variant_id):
    variant_id = variant_id.strip()
    _, modid, block = variant_id.removeprefix("everycomp:").split('/')
    block = block.removesuffix("_leaf_carpet") 
    return f"unique,{modid}:{block}_leaves,{variant_id}"

def transform_everycomp_hedges(variant_id):
    variant_id = variant_id.strip()
    _, modid, block = variant_id.removeprefix("everycomp:").split('/')
    block = block.removesuffix("_hedge") 
    return f"unique2,{modid}:{block}_leaves,{variant_id}"

def transform_everycomp_hollow_logs(variant_id):
    variant_id = variant_id.strip()
    _, modid, block = variant_id.removeprefix("everycomp:").split('/')
    block = block.removeprefix("hollow_") 
    return f"unique2,{modid}:{block},{variant_id}"

def transform_everycomp_posts(variant_id):
    variant_id = variant_id.strip()
    _, modid, block = variant_id.removeprefix("everycomp:").split('/')
    block = block.removesuffix("_post") 
    return f"unique,{modid}:{block}_log,{variant_id}"

def transform_everycomp_boardwalks(variant_id):
    variant_id = variant_id.strip()
    _, modid, block = variant_id.removeprefix("everycomp:").split('/')
    block = block.removesuffix("_boardwalk") 
    return f"unique3,{modid}:{block}_planks,{variant_id}"

def transform_everycomp_banisters(variant_id):
    variant_id = variant_id.strip()
    _, modid, block = variant_id.removeprefix("everycomp:").split('/')
    block = block.removesuffix("_banister") 
    return f"unique2,{modid}:{block}_planks,{variant_id}"

def transform_everycomp_log_fences(variant_id):
    variant_id = variant_id.strip()
    _, modid, block = variant_id.removeprefix("everycomp:").split('/')
    block = block.removeprefix("fence_log_") 
    return f"fence,{modid}:{block}_log,{variant_id}"

def transform_everycomp_log_walls(variant_id):
    variant_id = variant_id.strip()
    _, modid, block = variant_id.removeprefix("everycomp:").split('/')
    block = block.removeprefix("wall_stripped_").removeprefix("wall_").removesuffix("_log")
    return f"wall,{modid}:{block}_log,{variant_id}"

def transform_everycomp_plank_walls(variant_id):
    variant_id = variant_id.strip()
    _, modid, block = variant_id.removeprefix("everycomp:").split('/')
    block = block.removeprefix("wall_") 
    return f"wall,{modid}:{block},{variant_id}"

def transform_everycomp_supports(variant_id):
    variant_id = variant_id.strip()
    _, modid, block = variant_id.removeprefix("everycomp:").split('/')
    block = block.removesuffix("_support")
    return f"unique4,{modid}:{block}_planks,{variant_id}"

def transform_everycomp_beams(variant_id):
    variant_id = variant_id.strip()
    _, modid, block = variant_id.removeprefix("everycomp:").split('/')
    block = block.removesuffix("_beam")
    return f"unique2,{modid}:stripped_{block}_log,{variant_id}"

def transform_everycomp_palisades(variant_id):
    variant_id = variant_id.strip()
    _, modid, block = variant_id.removeprefix("everycomp:").split('/')
    block = block.removesuffix("_palisade")
    return f"unique3,{modid}:{block}_log,{variant_id}"

def transform_everycomp_vslabs(variant_id):
    variant_id = variant_id.strip()
    _, modid, block = variant_id.removeprefix("everycomp:").split('/')
    block = block.removesuffix("_vertical_slab")
    return f"vertical_slab,{modid}:{block}_planks,{variant_id}"

def transform_stonezone_vslabs(variant_id):
    variant_id = variant_id.strip()
    _, modid, block = variant_id.removeprefix("everycomp:").split('/')
    block = block.removesuffix("_vertical_slab")
    return f"vertical_slab,{modid}:{block},{variant_id}"

def transform_noop(variant_id):
    variant_id = variant_id.strip()
    return variant_id

def process(filepath, transformation_function):
    with open(filepath, 'r') as file:
        lines = file.readlines()
    transformed_lines = [transformation_function(line) for line in lines]
    transformed_lines = [line for line in transformed_lines if line] 

    return transformed_lines

    

if __name__ == "__main__":
    variants = []
    variants += process("VariantLists/QuarkHedges.txt", transform_quark_hedges)
    variants += process("VariantLists/QuarkCarpets.txt", transform_quark_carpets)
    variants += process("VariantLists/EverycompCarpets.txt", transform_everycomp_carpets)
    variants += process("VariantLists/EverycompHedges.txt", transform_everycomp_hedges)
    variants += process("VariantLists/EverycompQuarkHollowLogs.txt", transform_everycomp_hollow_logs)
    variants += process("VariantLists/EverycompPosts.txt", transform_everycomp_posts)
    variants += process("VariantLists/EverycompBoardwalks.txt", transform_everycomp_boardwalks)
    variants += process("VariantLists/EverycompBanisters.txt", transform_everycomp_banisters)
    variants += process("VariantLists/EverycompBeams.txt", transform_everycomp_beams)
    variants += process("VariantLists/EverycompSupports.txt", transform_everycomp_supports)
    variants += process("VariantLists/EverycompPalisades.txt", transform_everycomp_palisades)
    variants += process("VariantLists/EverycompVerticalSlabs.txt", transform_everycomp_vslabs)
    variants += process("VariantLists/StonezoneVerticalSlabs.txt", transform_stonezone_vslabs)
    variants += injectVanillaWoods("unique,minecraft:{wood}_leaves,quark:{wood}_leaf_carpet")
    variants += injectVanillaWoods("unique,minecraft:{wood}_log,quark:{wood}_post")
    variants += injectVanillaWoods("unique,minecraft:stripped_{wood}_log,quark:stripped_{wood}_post")
    variants += injectVanillaWoods("unique2,minecraft:{wood}_log,quark:hollow_{wood}_log")
    variants += injectVanillaWoods("unique2,minecraft:{wood}_leaves,quark:{wood}_hedge")
    variants += injectVanillaWoods("unique2,minecraft:stripped_{wood}_log,decorative_blocks:{wood}_beam")
    variants += injectVanillaWoods("unique2,minecraft:{wood}_planks,twilightforest:{wood}_banister")
    variants += injectVanillaWoods("unique3,minecraft:{wood}_log,decorative_blocks:{wood}_palisade")
    variants += injectVanillaWoods("unique4,minecraft:{wood}_planks,decorative_blocks:{wood}_support")
    variants += process("ManualVariantEntries.txt", transform_noop)

    quark_config = TOMLFile("../../../config/quark-common.toml")
    quark_config_read = quark_config.read()
    quark_config_read["experimental"]["variant_selector"]["variants"]["Manual Variants"] = variants
    quark_config.write(quark_config_read)
