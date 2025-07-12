from posts.domain.repositories import PostRepositoryInterface

def get_posts_by_email(repository: PostRepositoryInterface, email: str) -> list[dict]:
    return repository.find_by_email(email)