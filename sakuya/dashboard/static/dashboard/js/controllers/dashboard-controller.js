app = angular.module('DashboardApp');


app.controller('DashboardController', ['$scope', '$timeout', 'Child', '$uibModal', function($scope, $timeout, Child, $uibModal) {
	$scope.motionChart = null;
	$scope.langChart = null;

	$scope.langChartStep = 5;
	$scope.currentLangRange = [0, 15];
	$scope.currentLangPosList = 
		{
			'n': '名詞',
			'v': '動詞',
			'adj': '形容詞',
			'adv': '副詞',
			'im': '感動詞'
		}				

	$scope.showAll = function() {
		$('p.show-all').hide();
		$('#google-line-chart').height('340px');
		$('.dashboard-lang-frame').height('420px');
		$('div.required').addClass('narrow');
		$('div.additional').show();
		$scope.langChart.clearChart();
		$scope.currentLangPosList = 
			{
				'n': '名詞',
				'v': '動詞',
				'adj': '形容詞',
				'adv': '副詞',
				'im': '感動詞',
				'j': '助詞',
				'conj': '接続詞',
				'auv': '助動詞',
				'p': '接頭詞',
				't': '連体詞',
				'unk': '未知語'
			}				
		$scope.drawLangChart(self.currentLangPosList);
	}

	$scope.showMean = function() {
		$('.pos-mean').show();
		$('.show-mean').hide();
	}

	$scope.openWordListModal = function(pos) {
		var child = new Child($('#dashboard-internal-token').text());
		child.words(null, [pos], function(data){
			$uibModal.open({
				templateUrl: 'word-list-modal.html',
				controller: 'WordModalController',
				resolve: {
					Pos: function() { return $scope.currentLangPosList[pos]; },
					Words: function() { return data[pos]['words']; }
				}
			});
		});
	}

	$scope.forward = function() {
		$scope.currentLangRange[0] += $scope.langChartStep;
		$scope.currentLangRange[1] += $scope.langChartStep;
		$scope.langChart.clearChart();
		$scope.drawLangChart(self.currentLangPosList);
	}

	$scope.backward = function() {
		var start = $scope.currentLangRange[0] - $scope.langChartStep;
		if (start < 0) {
			return;
		}
		$scope.currentLangRange[0] = start;
		$scope.currentLangRange[1] -= $scope.langChartStep;
		$scope.langChart.clearChart();
		$scope.drawLangChart(self.currentLangPosList);
	}

	$scope.drawLangChart = function(pos_list) {
		var dataTable = new google.visualization.DataTable();
		dataTable.addColumn('number', '生後(ヶ月)');
		for (key in $scope.currentLangPosList) {
			dataTable.addColumn('number', $scope.currentLangPosList[key]);
		}
		
		var child = new Child($('#dashboard-internal-token').text());
		child.words($scope.currentLangRange, [], function(data){
			var res_list = [];
			for (key in $scope.currentLangPosList) {
				res_list.push(data[key]['monthly']);	
			}
		
			rows = [];
			for (var i = $scope.currentLangRange[0]; i <= $scope.currentLangRange[1]; ++i) {
				var row = [];
				row.push(i);
				for (var j = 0; j < res_list.length; ++j) {
					var pos_result = res_list[j]
					row.push(pos_result[i]['count']);
				}
				rows.push(row);
			}
			dataTable.addRows(rows)
				
			var options = {
				axes: {
					y: {
						all: {
							range: {
								min: 0	
							}
						},
					}
				},
			}

			$scope.langChart = new google.charts.Line(document.getElementById('google-line-chart'));
			$scope.langChart.draw(dataTable, options);
		});	
	}

	$scope.drawMotionChart = function(motionList) {
		var container = document.getElementById('google-timeline-chart');
		var dataTable = new google.visualization.DataTable();
		dataTable.addColumn({ type: 'string', id: 'dummy' });
		dataTable.addColumn({ type: 'string', id: 'motion' });
		dataTable.addColumn({ type: 'string', role: 'tooltip' });
		dataTable.addColumn({ type: 'number', id: 'Start' });
		dataTable.addColumn({ type: 'number', id: 'End' });
		dataTable.addRows([
			['1', '首すわり', '0〜4ヶ月', 0, 4000 ], 
			['2', '寝返り', '4〜7ヶ月', 4000, 7000],
			['3', 'ひとりすわり', '4〜7ヶ月', 4000, 7000],
			['4', 'はいはい', '7〜10ヶ月', 7000, 10000],
			['5', 'つかまり立ち', '8〜11ヶ月', 8000, 11000],
			['6', 'ひとり立ち', '10〜13ヶ月', 10000, 13000],
			['7', '二足歩行', '12〜15ヶ月', 12000, 15000],
		]);
		
		var child = new Child($('#dashboard-internal-token').text());
		child.motions(motionList, function(data) {
			var colors = [];
			for (var i = 0; i < motionList.length; ++i) {
				var motion = motionList[i]
				if (data[motion] && data[motion]['count'] > 0) {
					colors.push('#00bfff');
				} else {
					colors.push('#d3d3d3');
				}
			}
			var options = {
				timeline: { showRowLabels: false },
				backgroundColor: '#ffffff',
				colors: colors
			}
			$scope.motionChart = new google.visualization.Timeline(container);
			$scope.motionChart.draw(dataTable, options);
		});
	}

	function drawChart() {
		$scope.drawMotionChart(['neck_fix', 'rolling_over', 'sit', 'crawl', 'pullup', 'standup', 'walk']);
		$scope.drawLangChart(self.currentLangPosList);
	}
	google.load("visualization", "1", {packages: ["timeline", "line"], callback: drawChart});
}]);


app.controller('WordModalController', ['$scope', '$uibModalInstance', 'Words', 'Pos', function($scope, $uibModalInstance, words, pos) {
	$scope.words = words;
	$scope.pos = pos;

	$scope.closeModal = function() {
			$uibModalInstance.close();
	}
}]);



