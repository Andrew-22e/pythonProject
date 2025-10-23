from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uvicorn
import fastapi_cdn_host
from fastapi.staticfiles import StaticFiles

# 创建 FastAPI 应用
app = FastAPI()
fastapi_cdn_host.patch_docs(app)

# 静态文件
app.mount('../Static',StaticFiles(directory='Static'),name='Static')

# 数据模型
class Item(BaseModel):
    id: Optional[int] = None
    name: str
    price: float

class ItemUpdate(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None

class BatchItems(BaseModel):
    items: List[Item]

# 存储数据的列表（带ID）
items = []
next_id = 1

# GET - 获取所有数据
@app.get("/items")
def get_items():
    return {"items": items}

# GET - 根据ID获取单个数据
@app.get("/items/{item_id}")
def get_item(item_id: int):
    for item in items:
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=404, detail="物品不存在")

# POST - 创建单个数据
@app.post("/items")
def create_item(item: Item):
    global next_id
    new_item = {
        "id": next_id,
        "name": item.name,
        "price": item.price
    }
    items.append(new_item)
    next_id += 1
    return {"message": "创建成功", "item": new_item}

# POST - 批量创建数据
@app.post("/items/batch")
def create_items_batch(batch_items: BatchItems):
    global next_id
    created_items = []
    
    for item in batch_items.items:
        new_item = {
            "id": next_id,
            "name": item.name,
            "price": item.price
        }
        items.append(new_item)
        created_items.append(new_item)
        next_id += 1
    
    return {
        "message": f"批量创建成功，共创建 {len(created_items)} 个物品",
        "items": created_items
    }

# PUT - 修改单个数据
@app.put("/items/{item_id}")
def update_item(item_id: int, item_update: ItemUpdate):
    for i, item in enumerate(items):
        if item["id"] == item_id:
            # 更新字段（只更新提供的字段）
            if item_update.name is not None:
                items[i]["name"] = item_update.name
            if item_update.price is not None:
                items[i]["price"] = item_update.price
            
            return {"message": "更新成功", "item": items[i]}
    
    raise HTTPException(status_code=404, detail="物品不存在")

# DELETE - 删除单个数据
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    for i, item in enumerate(items):
        if item["id"] == item_id:
            deleted_item = items.pop(i)
            return {"message": "删除成功", "item": deleted_item}
    
    raise HTTPException(status_code=404, detail="物品不存在")

# 根路径
@app.get("/")
def root():
    return {
        "message": "欢迎使用简单API", 
        "docs": "访问 /docs 查看API文档",
        "endpoints": {
            "单个创建": "POST /items",
            "批量创建": "POST /items/batch",
            "获取所有": "GET /items",
            "获取单个": "GET /items/{id}",
            "修改": "PUT /items/{id}",
            "删除": "DELETE /items/{id}"
        }
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)