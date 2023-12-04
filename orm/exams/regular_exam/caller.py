import os
import django
from django.db.models import Count, Avg

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()


from main_app.models import Author, Article, Review


def get_authors(search_name=None, search_email=None):
	if search_name is None and search_email is None:
		return ""

	if search_name and search_email:
		authors = Author.objects.filter(
			full_name__icontains=search_name,
			email__icontains=search_email
		).order_by("-full_name")

	elif search_email:
		authors = Author.objects.filter(
			email__icontains=search_email
		).order_by("-full_name")

	elif search_name:
		authors = Author.objects.filter(
			full_name__icontains=search_name,
		).order_by("-full_name")

	result = []

	for a in authors:
		result.append(f"Author: {a.full_name}, email: {a.email}, status: {'Banned' if a.is_banned else 'Not Banned'}")

	return "\n".join(result)


def get_top_publisher():
	top_publisher = Author.objects.get_authors_by_article_count().first()

	if not Article.objects.all():
		return ""

	return f"Top Author: {top_publisher.full_name} with {top_publisher.articles_count} published articles."


def get_top_reviewer():
	top_reviewer = Author.objects.annotate(
		num_of_reviews=Count("review_author")
	).order_by(
		"-num_of_reviews",
		"email"
	).first()

	if not Review.objects.all():
		return ""

	return f"Top Reviewer: {top_reviewer.full_name} with {top_reviewer.num_of_reviews} published reviews."


def get_latest_article():
	article = Article.objects.annotate(
		num_reviews=Count("review_article"),
		avg_reviews_rating=Avg("review_article__rating")
	).order_by("published_on").last()

	if not Article.objects.all():
		return ""

	authors = ", ".join(author.full_name for author in article.authors.all().order_by('full_name'))

	return (f"The latest article is: {article.title}. "
			f"Authors: {authors}. Reviewed: {article.num_reviews} times. "
			f"Average Rating: {0 if article.num_reviews == 0 else article.avg_reviews_rating:.2f}.")


def get_top_rated_article():
	article = Article.objects.annotate(
		avg_rating=Avg("review_article__rating"),
		num_reviews=Count("review_article"),
	).order_by(
		"-avg_rating",
		"title"
	).first()

	if not Review.objects.all():
		return ""

	return (f"The top-rated article is: {article.title}, "
			f"with an average rating of {0 if article.num_reviews == 0 else article.avg_rating:.2f}, "
			f"reviewed {article.num_reviews} times.")


def ban_author(email=None):
	author = Author.objects.annotate(
		num_reviews=Count("review_author")
	).filter(
		email__exact=email
	).first()

	if not author or not Author.objects.all() or email is None:
		return "No authors banned."

	author.is_banned = True

	author.save()

	author.review_author.all().delete()

	return f"Author: {author.full_name} is banned! {author.num_reviews} reviews deleted."


print(ban_author('mail1'))