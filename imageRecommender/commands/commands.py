import sys
sys.path.append('../')

from flask import Blueprint
from imageRecommender.models import Galleryimages, Imagerecommendations
from imageRecommender import db 
import os
import pickle
from numpy.testing import assert_almost_equal

global numRec
numRec = 4

def getNames(inputName, similarNames, similarValues):
    images = list(similarNames.loc[inputName, :])
    values = list(similarValues.loc[inputName, :])
    if inputName in images:
        assert_almost_equal(max(values), 1, decimal = 5)
        images.remove(inputName)
        values.remove(max(values))
    return inputName, images[0:numRec], values[0:numRec]


def getImages(inputImage):
    similarNames = pickle.load(open(os.path.join("imageRecommender/static/pickles/similarNames.pkl"), 'rb'))
    similarValues = pickle.load(open(os.path.join("imageRecommender/static/pickles/similarValues.pkl"), 'rb'))
    
    if inputImage in set(similarNames.index):
        return getNames(inputImage, similarNames, similarValues)
    else:
        print("'{}' was not found.".format(inputImage))
        sys.exit(2)

cmd = Blueprint('db', __name__)

@cmd.cli.command('createDB')
def createDB():
    db.create_all()

@cmd.cli.command('dropDB')
def dropDB():
    db.drop_all() 

@cmd.cli.command('importDB')
def importDB():
    images = [
        {
            'name':'buildings0.jpg',
            'caption': 'Lisboa'
        },
        {
            'name': 'camper0.jpg',
            'caption':  'Red camper fruit trees'
        },
        {
            'name': 'trees0.jpg',
            'caption':  'Forrest 1'
        },
        {
            'name':'pyramiden0.jpg',
            'caption': 'Pyramid Chichen Itza'
        },
        {
            'name':'rio0.jpg',
            'caption': 'View Rio de Janeiro'
        },
        {
            'name': 'buildings1.jpg',
            'caption': 'Old building'
        },
        {
            'name': 'donkey0.jpg',
            'caption':  'Grey donkey 1'
        }, 
        {
            'name':'pyramiden1.jpg',
            'caption': 'Pyramids Cairo'
        },
        {
            'name': 'camper2.jpg',
            'caption':  'Red camper on a field'
        },
        {
            'name':'rio1.jpg',
            'caption': 'View Rio de Janeiro 2'
        },
        {
            'name': 'buildings2.jpg',
            'caption':  'Other old building'
        },
        {
            'name': 'camper1.jpg',
            'caption':  'Yellow camper camping'
        },
        {
            'name': 'donkey3.jpg',
            'caption':  'Grey donkey 2'
        }, 
        {
            'name': 'trees2.jpg',
            'caption':  'Forrest 3'
        },
        {
            'name':'pyramiden2.jpg',
            'caption': 'Pyramid Cairo'
        },
        {
            'name':'rio2.jpg',
            'caption': 'View Rio de Janeiro 3'
        },
        {
            'name': 'camper4.jpg',
            'caption':  'Red camper in Fresse'
        },  
        {
            'name': 'donkey1.jpg',
            'caption':  'Brown donkey 1'
        },
        {
            'name': 'buildings3.jpg',
            'caption':  'Palace Madrid'
        },
        {
            'name': 'donkey4.jpg',
            'caption':  'Grey donkey 3'
        }, 
        {
            'name': 'trees1.jpg',
            'caption':  'Forrest 2'
        },
        {
            'name':'pyramiden3.jpg',
            'caption': 'Pyramid Palenque'
        },
        {
            'name':'rio3.jpg',
            'caption': 'View Rio de Janeiro 4'
        },
        {
            'name': 'buildings4.jpg',
            'caption':  'Gate Potsdam'
        },
        {
            'name':'pyramiden4.jpg',
            'caption': 'Pyramid Chichen Itza'
        },
        {
            'name':'rio4.jpg',
            'caption': 'View Rio de Janeiro 5'
        },
        {
            'name': 'buildings5.jpg',
            'caption':  'Two towers'
        },
        {
            'name': 'camper3.jpg',
            'caption':  'Red camper on a goat farm'
        },
        {
            'name': 'donkey2.jpg',
            'caption':  'Brown donkey 2'
        },
        {
            'name': 'trees3.jpg',
            'caption':  'Forrest 4'
        },
        {
            'name': 'trees4.jpg',
            'caption':  'Forrest 5'
        }
    ]

    for image in images:
        img = Galleryimages(imageName=image['name'], imageDescription=image['caption'])
        #print(img)
        db.session.add(img)
        db.session.commit()

        inputImage, images, values = getImages(image['name'])
        recArray = []
        for j in range(0, numRec):
            rec = Imagerecommendations(recommendedID = img.id, recommendedName=images[j], similarityValue=values[j])
            #print(rec)
            db.session.add(rec)

        db.session.commit()
    db.session.close() 

#print('Query all')
#allI=Galleryimages.query.all()
#print(allI)
#print(allI[0].imageName)
#print(allI[0].imageDescription)