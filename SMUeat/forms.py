from django.forms import ModelForm
from django import forms
from SMUeat.models import Place, Review
from django.utils.translation import gettext_lazy as _

REVIEW_POINT_CHOICES = (
    ('1', 1),  # '1'은 평점 1점
    ('2', 2),  # '2'은 평점 2점
    ('3', 3),  # '3'은 평점 3점
    ('4', 4),  # '4'은 평점 4점
    ('5', 5),  # '5'은 평점 5점
)  # 평점 설정함.
# 앞 값은 DB에 저장되는 값이고 뒷 값은 폼이나 템플릿 등에서 출력하는 값

class PlaceForm(ModelForm):
    class Meta:
        model = Place
        fields = ['name', 'category']
        labels = {
            'name': _('장소 이름'),
            'category': _('카테고리'),
        }
        help_texts = {
            'name': _('장소 이름을 입력해주세요.'),
            'category': _('장소의 카테고리를 선택해주세요.'),
        }
        error_messages = {
            'name': {
                'max_length': _("이름이 너무 깁니다. 줄여주세요."),
            },
        }

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['point', 'menu', 'comment', 'place', 'password']
        labels = {
            'point': _('평점'),
            'menu': _('추천 메뉴'),
            'comment': _('리뷰 설명'),
            'password': _('리뷰 비밀번호'),
        }
        help_texts = {
            'point': _('평점을 1~5점 중에서 골라주세요.'),
            'menu': _('추천 메뉴를 입력해주세요.'),
            'comment': _('리뷰 설명을 입력해주세요.'),
            'password': _('리뷰 수정&삭제시 본인확인을 위해 비밀번호를 입력해주세요.'),
        }
        widgets = {
            'place': forms.HiddenInput(),
            'point': forms.Select(choices=REVIEW_POINT_CHOICES),
            'password': forms.PasswordInput()
        }
        error_messages = {
            'password': {
                'max_length': _("비밀번호가 너무 깁니다. 줄여주세요."),
            },
        }

class UpdateReviewForm(ReviewForm):
    class Meta:
        model = Review
        exclude = ['password']