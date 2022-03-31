import unreal

@unreal.uclass()
class Gameplay(unreal.GameplayStatics):
    pass

@unreal.uclass()
class MathLib(unreal.MathLibrary):
    pass


gameActors = Gameplay().get_all_actors_of_class(unreal.EditorLevelLibrary.get_game_world(), unreal.StaticMeshActor)


for actor in gameActors:
    if actor.actor_has_tag("manipulate"):
        
        while(MathLib.in_range_float_float((actor.get_actor_location()).z, 20, 500)):
            actor.set_actor_location(actor.get_actor_location()+unreal.Vector(0,0,-20), True, False)
           
        
        
        
        
        #if MathLib.in_range_float_float((actor.get_actor_location()+unreal.Vector(0,0,-10)).z, 100, 500):
        #    actor.set_actor_location(actor.get_actor_location()+unreal.Vector(0,0,-20), True, False)
        



