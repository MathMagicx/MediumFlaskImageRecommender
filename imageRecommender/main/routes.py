from flask import render_template, request, Blueprint
from imageRecommender.models import Galleryimages

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    gImages = Galleryimages.query.paginate(page=page, per_page=8)
    return render_template('home.html', images = gImages)

@main.route("/recommend")
def recommend():
    selectedImage = request.args.get('selectedImage')
    imageEntry = Galleryimages.query.filter_by(imageName=selectedImage) 
    if imageEntry:
        images = []
        values = []
        for image in imageEntry:
            print(image.imageName)
            for recommendation in image.imageRecs:
                images.append(recommendation.recommendedName)
                values.append(recommendation.similarityValue)

        return render_template('recommend.html', title='Recommendations', customstyle='recommend.css', inputImage=selectedImage, similarImages=images, similarityValues = values)
    else:
        print('Inconsistency!')    

if __name__ == '__main__':
    app.run(debug=True)