import re
from typing import Optional
from fastapi import Query, HTTPException, status

from models.product_model import Product

from uuid import UUID

from models.user_model import Usuario
from schemas.product_schema import ProductCreate, ProductUpdate


class ProductService:

    @staticmethod
    async def get_all_products(product_name: Optional[str] = Query(None),
                               category: Optional[str] = Query(None),
                               price: Optional[str] = Query(None),
                               brand: Optional[str] = Query(None),
                               seller: Optional[Usuario] = Query(None),
                               ) -> list[Product]:
        filter_query = {
            key: value.lower() if value is not None else None
            for key, value in {
                "product_name": product_name,
                "category": category,
                "price": price,
                "brand": brand,
            }.items()
        }

        filter_conditions = [Product.seller == seller.id if seller else None]

        for key, value in filter_query.items():
            if value is not None:
                regex_pattern = f".*{re.escape(value)}.*"  # Convert the value to a regex pattern
                filter_conditions.append({key: {"$regex": regex_pattern, "$options": "i"}})

        result = await Product.find({"$and": filter_conditions}).to_list()

        if not result:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Pets not found"
            )
        return result

    @staticmethod
    async def get_product_by_id(product_id: UUID, seller: Optional[Usuario] = Query(None)) -> Product:
        result = await Product.find_one(Product.product_id == product_id,
                                        Product.seller == seller.id if seller else None)
        if not result:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Product not found"
            )
        return result

    @staticmethod
    async def create_product(data: ProductCreate, seller: Optional[Usuario]) -> Product:
        result = Product(**data.dict(), seller=seller.id)
        if not result:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Can't create product"
            )
        await result.insert()
        return result

    @staticmethod
    async def update_product(product_id: UUID, data: ProductUpdate) -> Product:
        result = await ProductService.get_product_by_id(product_id)
        if not result:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Product not found"
            )
        await result.update({"$set": data.dict(exclude_unset=True)})
        return result

    @staticmethod
    async def delete_product(product_id: UUID):
        result = await ProductService.get_product_by_id(product_id)
        if not result:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Product not found"
            )
        await result.delete()
        return result
