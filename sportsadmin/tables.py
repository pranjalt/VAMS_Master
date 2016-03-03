'''
Created on 14-Jan-2016

@author: Administrator
'''
from sportsList.models import PlayerOnboarding,CoachOnboarding,AcademyOnboarding
from table import Table
from table.columns import Column
from Carousel.models import *


class PlayerTable(Table):
    player_id = Column(field='player_id',header=' PLAYERID')
    first_name = Column(field='first_name',header='FIRST NAME')
    last_name = Column(field='last_name',header='LAST NAME')
    contactNo=Column(field="contact_no",header=' CONTACTNO')
    email_id=Column(field="email_id",header=' EMAILID')
    DOB = Column(field='date_of_birth',header='DOB')
    edit = Column(field='edit',header='',attrs = {'class':'fa fa-edit','id':'edit'})
    view = Column(field='view',header='',attrs = {'class':'fa fa-file-text','id':'view',})
    trash = Column(field='trash',header='',attrs= {'class':'fa fa-trash-o','id':'trash',
                                                   'data-toggle':'modal','data-target':'#deletePlayerModal'})
    
    class Meta:
        model = PlayerOnboarding
		
class CoachTable(Table):
    coach_id = Column(field='coach_id',header=' COACHID')
    first_name = Column(field='first_name',header='FIRST NAME')
    last_name = Column(field='last_name',header='LAST NAME')
    contactNo=Column(field="contact_no",header=' CONTACTNO')
    email_id=Column(field="email_id",header=' EMAILID')
    DOB = Column(field='date_of_birth',header='DOB')
    edit = Column(field='edit',header='',attrs = {'class':'fa fa-edit','id':'edit'})
    view = Column(field='view',header='',attrs = {'class':'fa fa-file-text','id':'view',})
    trash = Column(field='trash',header='',attrs= {'class':'fa fa-trash-o','id':'trash',
                                                   'data-toggle':'modal','data-target':'#deleteCoachModal'})
    
    class Meta:
        model = CoachOnboarding
		
class AcademyTable(Table):
    coach_id = Column(field='acd_reg_id',header=' ACADEMY_ID')
    name = Column(field='name',header='ACADEMY NAME')
    
    contactNo=Column(field="contact_no",header=' CONTACTNO')
   
    website=Column(field="website",header='WEBSITE')
    edit = Column(field='edit',header='',attrs = {'class':'fa fa-edit','id':'edit'})
    view = Column(field='view',header='',attrs = {'class':'fa fa-file-text','id':'view',})
    trash = Column(field='trash',header='',attrs= {'class':'fa fa-trash-o','id':'trash',
                                                   'data-toggle':'modal','data-target':'#deleteAcademyModal'})
    
    class Meta:
        model = AcademyOnboarding
        

class CarouselVideoTable(Table):
    video_id = Column(field='video_id',header=' VIDEO_ID')
    movie_url = Column(field='movie_url',header='MOVIE_URL')
    width = Column(field='width',header='WIDTH')
    height=Column(field="height",header=' HEIGHT')
    edit = Column(field='edit',header='',attrs = {'class':'fa fa-edit','id':'edit'})
    view = Column(field='view',header='',attrs = {'class':'fa fa-file-text','id':'view',})
    trash = Column(field='trash',header='',attrs= {'class':'fa fa-trash-o','id':'trash',
                                                   'data-toggle':'modal','data-target':'#deleteVideoModal'})
    
    class Meta:
        model = Carousel_video_video 
		
class CarouselPictureTable(Table):
    picture_id = Column(field='picture_id',header=' PICTURE_ID')
    image = Column(field='image',header='IMAGE')
    url = Column(field='url',header='URL')
    alt=Column(field="alt",header=' ALT')
    edit = Column(field='edit',header='',attrs = {'class':'fa fa-edit','id':'edit'})
    view = Column(field='view',header='',attrs = {'class':'fa fa-file-text','id':'view',})
    trash = Column(field='trash',header='',attrs= {'class':'fa fa-trash-o','id':'trash',
                                                   'data-toggle':'modal','data-target':'#deletePhotoModal'})
    
    class Meta:
        model = Carousel_Picture 
		
