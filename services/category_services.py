import re
from typing import Optional
from uuid import UUID
from models.category_model import Category
from fastapi import HTTPException, Query
from schemas.category_schema import CategoryCreate, CategoryUpdate


class CategoryService:

    @staticmethod
    async def get_all_categories(category_name: Optional[str] = Query(None)) -> list[Category]:
        filter_query = {
            key: value
            for key, value in {
                "category_name": category_name
            }.items() if value is not None
        }

        filter_conditions = []

        for key, value in filter_query.items():
            if value is not None:
                regex_pattern = f".*{re.escape(value)}.*"  # Convert the value to a regex pattern
                filter_conditions.append({key: {"$regex": regex_pattern, "$options": "i"}})

        result = await Category.find({"$and": filter_conditions}).to_list()

        if not result:
            raise HTTPException(status_code=404, detail="No categories found")
        return result

    @staticmethod
    async def get_category(category_id: UUID) -> Category:
        result = await Category.find_one(Category.category_id == category_id)
        if not result:
            raise HTTPException(status_code=404, detail="Category not found")
        return result

    @staticmethod
    async def create_category(data: CategoryCreate) -> Category:
        result = await Category(**data.dict())
        if not result:
            raise HTTPException(status_code=400, detail="Category not created")
        await result.insert()
        return result

    @staticmethod
    async def update_category(category_id: UUID, data: CategoryUpdate) -> Category:
        result = await CategoryService.get_category(category_id)
        if not result:
            raise HTTPException(status_code=404, detail="Category not found")
        await result.update({"$set": data.dict(exclude_unset=True)})
        return result

    @staticmethod
    async def delete_category(category_id: UUID) -> Category:
        result = await CategoryService.get_category(category_id)
        if not result:
            raise HTTPException(status_code=404, detail="Category not found")
        await result.delete()
        return result
