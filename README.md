MADE_Targeted_Image_Generation_with_Latent_Diffusion_Models
==============================

# Тематическая генерация изображений с помощью библиотеки Stable Diffusion. 
Немного про библиотеку Stable Diffusion: она создает изображение и имеет дату релиза 22 августа 2022, у нее есть 2 версии text2image и image2image.

В данной работе используется версия image2image: на вход подается изображение и описание изображения сгенерированное с помощью модели LAVIS; на базе исходного изображения и текста генерируется новое изображение.
### Поставленные задачи: 
1) собрать датасет разнообразных изображений, на которых будет проверяться генерация изображений (для понимания, на чем лучше работает)
2) выяснить на каких стилях лучше работает  SD,  понять за счет чего можно улучшить результат SD
3) разработать метрику для определения лучших стилей
4) разработать модель удобную для пользователя
5) при этом модель должна быть быстрой и легковесной для реализации.

### Результаты по задачам:
1) Было разработано 2 датасета: 12 изображений и 250 изображений (с людьми, животными, персонажами из фильмов и мультфильмов, пейзажами и натюрмортами)
2) Для сравнения использовались стили: изменение фона (Диснейленд); эмоции (радость, грусть); маска панда; стили художников (Бэнкси, Робер Делоне, Казимир Малевич и Винсент Ван Гог). 

    Было проверено 2 архитектуры: по изображению пользователя генерируется описание и по этому описанию + стиль создается новое изображение; во второй модели еще используется изображение пользователя  + его описание + стиль. 
    Вторая модель показала результаты более приближенные к исходному изображению, но не всегда стабильные. Для выбора стилей была разработана метрика.

3) При выборе стилей для генерации разработана метрика. С помощью модели LAVIS определяется соответствует ли данное изображение стилю (за ответ да 1, за нет 0), данные ответы суммируются и делятся на количество изображений. Построен график на датасете. Лучшие результаты показали стили художников.
4) Архитектура полученной модели. По изображению создается ее описание в модели LAVIS. Далее описание и выбранный пользователем стиль передаются в Stable Diffusion. Пользователь на вход подает изображение и получает 4 сгенерированных изображения в стилях художников: Бэнкси, Робер Делоне, Казимир Малевич и Винсент Ван Гог
5) Модель весит 10Гб и на 12 Гб считает около 2-3 минут



Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
