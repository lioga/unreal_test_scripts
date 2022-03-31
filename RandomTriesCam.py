import unreal
import time

@unreal.uclass()
class Gameplay(unreal.GameplayStatics):
    pass

@unreal.uclass()
class MathLib(unreal.MathLibrary):
    pass

gameActors = Gameplay().get_all_actors_of_class(unreal.EditorLevelLibrary.get_game_world(), unreal.CineCameraActor)


for actor in gameActors:
    if actor.actor_has_tag("manipulate"):
        random_rot = MathLib.random_rotator(False) 
        actor.set_actor_rotation(random_rot, False)
        time.sleep(1)
    







