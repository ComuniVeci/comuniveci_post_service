from posts.domain.repositories import PostRepositoryInterface

def delete_post(post_id: str, repository: PostRepositoryInterface) -> bool:
    post = repository.find_by_id(post_id)
    if not post:
        return False

    repository.delete(post_id)
    return True
