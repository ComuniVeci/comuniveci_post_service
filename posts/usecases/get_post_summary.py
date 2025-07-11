from posts.domain.repositories import PostRepositoryInterface

def get_post_summary(repository: PostRepositoryInterface) -> dict:
    approved = repository.find_approved()
    pending = repository.find_pending()
    return {
        "approved": len(approved),
        "pending": len(pending),
        "total": len(approved) + len(pending)
    }