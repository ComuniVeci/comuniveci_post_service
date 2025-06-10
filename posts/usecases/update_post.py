from posts.domain.repositories import PostRepositoryInterface

def update_post(post_id: str, new_data: dict, repository: PostRepositoryInterface) -> dict | None:
    post = repository.find_by_id(post_id)
    if not post:
        return None

    for key in new_data:
        if key in post and key != "_id":  # no permitir modificar el ID
            post[key] = new_data[key]

    return repository.update(post)