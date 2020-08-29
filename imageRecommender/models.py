from imageRecommender import db


class Galleryimages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    imageName = db.Column(db.String(50), unique=True, nullable=False)
    imageDescription = db.Column(db.String(150), unique=False, nullable=False, default='n.a.')
    imageRecs =  db.relationship('Imagerecommendations', backref='galleryimages', lazy=True) 

    def __repr__(self):
        return "(%s, %s, %s)" % (self.id, self.imageName, self.imageDescription)


class Imagerecommendations(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    recommendedID = db.Column(db.Integer, db.ForeignKey('galleryimages.id'), nullable=False)
    recommendedName = db.Column(db.String(50), unique=False, nullable=False)
    similarityValue = db.Column(db.Float, unique=False, nullable=False) 

    def __repr__(self):
        return "(%s, %s, %s, %s)" % (self.id, self.recommendedID, self.recommendedName, self.similarityValue)