app = angular.module('TimelineApp');

function initInst(inst, fields, attrs) {
	for (field in fields) {
		if (attrs && field in attrs) {
			inst[field] = attrs[field];
		} else {
			inst[field] = fields[field];
		}
	}
}


app.factory('Photo', ['FileUpload', '$http', function(FileUpload, $http) {
	var fields = {'imageFile': null, 'url': '', 'width': '150px', 'height': '150px', 'title': '', 'comment': '', 'owner': ''};
	
	var UPLOAD_URL = '/photos/';
	var SAVE_URL = '/photos/';
	
	var constructor = function(attrs) {
		initInst(this, fields, attrs);
	}

	constructor.prototype = {
		loadImage: function(imageFile, endcallback) {
			this.imageFile = imageFile;
			var reader = new FileReader();
			reader.onloadend = (function(photo){ return function(e){
				photo.url = e.target.result;
				image = new Image();
				image.onload = function() {
					photo.width = image.width;
					photo.height = image.height;
					endcallback();
				};
				image.src = e.target.result;
			}})(this);
				
			reader.readAsDataURL(imageFile);
		},

		save: function(success, error) {
			var fd = new FormData();
			fd.append('image_file', this.imageFile);
			fd.append('image_height', this.height);
			fd.append('image_width', this.width);
			fd.append('title', this.title);
			fd.append('comment', this.comment);
			if (this.owner != '') {
				fd.append('owner', this.owner);
			}

			$http.post(
				SAVE_URL,
				fd,
				{
					transformRequest: angular.identity,
					headers: {'Content-Type': undefined}
				}
			).success(function(data){
				if (success) {
					success(data);
				}
			}).error(function(){
				if (error) {
					error();
				}
			});
		}
	}

	return constructor;
}]);

