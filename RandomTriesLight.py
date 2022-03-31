import unreal
import time

@unreal.uclass()
class Gameplay(unreal.GameplayStatics):
    pass

@unreal.uclass()
class MathLib(unreal.MathLibrary):
    pass

gameActors = Gameplay().get_all_actors_of_class(unreal.EditorLevelLibrary.get_game_world(), unreal.PointLight)


for actor in gameActors:
    if actor.actor_has_tag("manipulate"):
        random_transform = MathLib.random_float_in_range(-100,100)
        actor.set_actor_relative_location((0,0,random_transform), False, True)
        time.sleep(1)
