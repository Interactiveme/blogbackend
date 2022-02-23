from .views import CategoryList, PostList
from rest_framework.routers import DefaultRouter

app_name = 'blog'

router = DefaultRouter()
router.register('post', PostList, basename='post')
router.register('categories', CategoryList, basename='categories')
router.register('post/bycategory', PostList, basename='postbycategory')

urlpatterns = router.urls

""" urlpatterns = [
    path('<int:pk>/', PostDetail.as_view(), name="detailcreate"),
    path('', PostList.as_view(), name='listcreate')
] """