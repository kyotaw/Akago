app = angular.module('TimelineApp');

app.controller('TimelineController', ['$scope', '$timeout', '$location', '$dragon', 'Photo', 'Util', function($scope, $timeout, $location, $dragon, Photo, Util) {
	$scope.new_photo = new Photo();

	$scope.childId = $('#internal-childid-token').text();
	$scope.photoList = [];

	$scope.channel = 'photos';
	$dragon.onReady(function() {
		$dragon.subscribe('photo-router', $scope.channel, { owner_id: $scope.childId }).then(function(response) {
			$scope.dataMapper = new DataMapper(response.data);
		});
		$dragon.getList('photo-router', { owner_id: $scope.childId }).then(function(response) {
			$scope.photoList = response.data
		});
	});

	$dragon.onChannelMessage(function(channels, message) {
		if (indexOf.call(channels, $scope.channel) > -1) {
	    	$scope.$apply(function() {
				if (message['action'] === 'created') {
					$scope.photoList.unshift(message['data']);
				} else {
		    		$scope.dataMapper.mapData($scope.photoList, message);
				}
			});
		}
	});

	var imageArea = angular.element(document.getElementById('user-drop-image'));
	imageArea.on('dragenter', Util.stopEvent);
	imageArea.on('dragover', Util.stopEvent);
	
	$scope.frameHeight = '150px';
	$scope.catchImage = function(e) {
		var imageFile = null;
		var files = e.originalEvent.dataTransfer.files;
		for (var i = 0; i < files.length; ++i) {
			if (files[i].type.indexOf('image') == 0) {
				imageFile = files[i];
				break
			}
		}
		if (imageFile == null) {
			return;
		}
		imageArea.off('drop');
		
		$scope.new_photo.loadImage(imageFile, function(){
			$timeout(function(){});
		});
		return Util.stopEvent(e);
	}
	imageArea.on('drop', $scope.catchImage);

	$scope.showPhotoEditor = function() {
		$('#timeline-photo-editor').show('fast');
	}

	$scope.hidePhotoEditor = function() {
		$('#timeline-photo-editor').hide('fast');
	}

	$scope.save = function() {
		if ($scope.new_photo.imageFile == null) {
			return;
		}
		content = $('#photo-comment-input>.photo-comment-placeholder');
		$scope.new_photo.comment = content.val();
		$scope.new_photo.save(function(data){
			$scope.new_photo = new Photo();
			$scope.hidePhotoEditor();
		});
	}

	$scope.delete = function(id) {
		return;
	}

	$scope.convert = function(photo_id) {
		//var photo = new Photo({'id': photo_id});
		//photo.convert('sepia');		
	}
}]);
