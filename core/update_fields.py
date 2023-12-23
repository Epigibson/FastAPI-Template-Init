import asyncio

from models.pet_model import Pet


async def does_field_exist(model, field):
    field_exists: bool = True
    async for document in model.find({}, {field: 1}):
        if not document.get(field):
            field_exists = False
            return field_exists
        field_exists = True
    return field_exists


async def update_fields():
    # pass
    await Pet.update_all({}, {"$set": {"avatar_image": None, "sterilized": True}})


async def main():
    await update_fields()


if __name__ == "__main__":
    asyncio.run(main())
