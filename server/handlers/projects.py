from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from fastapi_sqlalchemy import db
from serialization.project import Project as PydanticProject
from models.project import Project as ModelProject


router = APIRouter()

@router.post("/projects/")
async def create_project(project: PydanticProject):
    try:
        project = ModelProject(
            name=project.name,
            description=project.description,
            owner_id=project.owner_id,
            collaborators=project.collaborators,
            tags=project.tags,
            skills=project.skills,
            status=project.status,
            github=project.github,
            email=project.email
        )
        db.session.add(project)
        db.session.commit()
        return JSONResponse(
            status_code=201, 
            content={"message": "Project created successfully"}
        )
    except BaseException as exception:
        raise HTTPException(status_code=400, detail=exception)

@router.get("/projects/{id}", response_model=PydanticProject)
async def get_project(id: int):
    project = await ModelProject.get(id)
    return project