from posts.domain.repositories import PostRepositoryInterface

def get_pending_posts(repository: PostRepositoryInterface) -> list[dict]:
    return repository.find_pending()
