from rest_framework import status, permissions
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from apps.question.models import Question, Quiz
from apps.users.models import User


class SubmitQuiz(CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        user = User.objects.get(email=request.user)
        answers = request.data.get('answers')
        if not answers:
            return Response({"status": status.HTTP_500_INTERNAL_SERVER_ERROR, "details": {"can't read the answers"}})
        right_answers = 0
        wrong_answers = 0
        for question_id in answers.keys():
            answer_number = answers[question_id]
            db_question = Question.objects.get(id=question_id)
            if db_question.answer_number == answer_number:
                right_answers += 1
            else:
                wrong_answers += 1
        quiz = Quiz(user=user, right_answers=right_answers, wrong_answers=wrong_answers)
        quiz.save()
        total = wrong_answers + right_answers
        return Response({
            "status": status.HTTP_200_OK, "details": {"percent": (right_answers / total) * 100}
        })
