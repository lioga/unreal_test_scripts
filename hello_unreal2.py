import unreal
print("hello unreal!")
obj = unreal.log("deneme")



selectedAssets = unreal.GlobalEditorUtilityBase().get_selected_assets()

for asset in selectedAssets:
    unreal.log(asset.get_fname())

