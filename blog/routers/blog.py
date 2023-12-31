from fastapi import APIRouter, Depends, status, Response

from sqlalchemy.orm import Session

from typing import List

from .. import schemas, oauth2

from ..database import get_db

from ..repository import blog


router = APIRouter(
    prefix="/blog",
tags=['blogs']
)

@router.get('/', response_model=List[schemas.ShowBlog])
def getblog(db : Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_all(db)

@router.post('/', status_code=status.HTTP_201_CREATED, )
def create(request: schemas.Blog, db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.create(db, request)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete(id, db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.destroy(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schemas.Blog, db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.show(id, request, db)

@router.get('/{id}', status_code=200,response_model=schemas.ShowBlog)
def show(id,response: Response, db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.getid(db,id)