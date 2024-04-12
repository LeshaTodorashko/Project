from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
from PyQt5.QtGui import QImage
import random

class MemApp(QWidget):
    def init(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Мем Генератор')

        # Кнопка для відображення випадкового мема
        self.btn_generate = QPushButton('Згенерувати мем', self)
        self.btn_generate.clicked.connect(self.generate_meme)

        # Кнопки категорій мемів
        self.btn_category1 = QPushButton('Категорія 1', self)
        self.btn_category1.clicked.connect(self.choose_category)
        self.btn_category2 = QPushButton('Категорія 2', self)
        self.btn_category2.clicked.connect(self.choose_category)
        self.btn_category3 = QPushButton('Категорія 3', self)
        self.btn_category3.clicked.connect(self.choose_category)

        # Зображення мема
        self.image_label = QLabel(self)
        self.image_label.setFixedSize(300, 300)

        # Розміщення елементів у вікні
        layout = QVBoxLayout(self)
        layout.addWidget(self.btn_generate)
        layout.addWidget(self.btn_category1)
        layout.addWidget(self.btn_category2)
        layout.addWidget(self.btn_category3)
        layout.addWidget(self.image_label)

        self.setLayout(layout)
        self.show()

    def generate_meme(self):
        # Список зображень мемів
        meme_images = {
            'Категорія 1': ['meme1.jpg', 'meme2.jpg', 'meme3.jpg'],
            'Категорія 2': ['meme4.jpg', 'meme5.jpg', 'meme6.jpg'],
            'Категорія 3': ['meme7.jpg', 'meme8.jpg', 'meme9.jpg']
        }
        # Вибір випадкової категорії
        category = random.choice(list(meme_images.keys()))
        # Вибір випадкового мема з обраної категорії
        meme = random.choice(meme_images[category])
        # Відображення нового зображення
        image = QImage(meme)
        self.image_label.setPixmap(image)


if __name__ == '__main':
    app = QApplication([])
    mem_app = MemApp()
    app.exec_()