from ice.recipe import recipe


async def say_hello():
    hola = await say_hola()
    return f"Hello world! {hola}"

async def say_hola():
    return "Hola mundo!"

recipe.main(say_hello)