from flask_wtf.file import FileAllowed, FileField, FileRequired
from flask_wtf.form import FlaskForm
from wtforms.fields.simple import SubmitField


class UploadImageForm(FlaskForm):
    image = FileField(
        validators=[
            FileRequired("画像ファイルを選択してください。"),
            FileAllowed(["jpg", "jpeg", "png"], "サポートされていない画像形式です"),
        ]
    )
    submit = SubmitField("アップロード")
