from posts.domain.repositories import PostRepositoryInterface

def get_approved_posts(repository: PostRepositoryInterface) -> list[dict]:
    return repository.find_approved()