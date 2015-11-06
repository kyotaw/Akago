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


app.factory('Photo', ['$http', function($http) {
	var fields = {'id': '', 'title': '', 'imageFile': null, 'image': '', 'audio': '', 'movie': '', 'date': '', 'age': '', 'comment': '', 'owner': '', 'stamp': '', 'footer': '', 'motion': ''};
	
	var PHOTOS_URL = '/photos/';
	
	var constructor = function(attrs) {
		initInst(this, fields, attrs);
	}

	constructor.query = function(child_id, success, error) {
		var url = PHOTOS_URL + child_id;
		$http.get(
			url
		).success(function(data, status) {
			if (success) {
				success(data);
			}
		}).error(function(data) {
			if (error) {
				error(data);
			}
		});
	}

	constructor.prototype = {
		loadImage: function(imageFile, endcallback) {
			this.imageFile = imageFile;
			var reader = new FileReader();
			reader.onloadend = (function(photo){ return function(e){
				photo.image = e.target.result;
				image = new Image();
				image.onload = function() {
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
				PHOTOS_URL,
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
		},

		convert: function(effect, success, error) {
			var fd = new FormData();
			fd.append('effect', effect);

			$http.post(
				PHOTOS_URL + 'convert/' + this.id,
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

