from posts.domain.repositories import PostRepositoryInterface

def approve_post(post_id: str, repository: PostRepositoryInterface) -> dict | None:
    post = repository.find_by_id(post_id)
    if not post:
        return None

    post["is_approved"] = True
    repository.update(post)  # reutilizamos save para sobrescribir
    return post