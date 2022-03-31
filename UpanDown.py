import unreal

@unreal.uclass()
class Gameplay(unreal.GameplayStatics):
    pass

gameActors = Gameplay().get_all_actors_of_class(unreal.EditorLevelLibrary.get_game_world(), unreal.StaticMeshActor)
Gameplay.get_accurate_real_time()

for actor in gameActors:
    if actor.actor_has_tag("manipulate"):
        unreal.log(actor)
        
        if actor.get_actor_location().z > 200:
            actor.set_actor_relative_location(actor.get_actor_location()+unreal.Vector(0,0,-50), True, False)
        elif actor.get_actor_location().z < 100.0:
            actor.set_actor_location(actor.get_actor_location()+unreal.Vector(0,0, 10), False, False)
