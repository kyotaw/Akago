app = angular.module('DashboardApp');


var LangState = {
	'n': { state: true, headline: '名詞' },
	'v': { state: true, headline: '動詞' },
	'adj': { state: true, headline: '形容詞' },
	'adv': { state: true, headline: '副詞' },
	'im': { state: true, headline: '感動詞' },
	'j': { state: false, headline: '助詞' },
	'conj': { state: false, headline: '接続詞' },
	'auv': { state: false, headline: '助動詞' },
	'p': { state: false, headline: '接頭詞' },
	't': { state: false, headline: '連体詞' },
	'unk': { state: false, headline: '未知語' },
	'showMean': false,
}

app.controller('DashboardController', ['$scope', '$timeout', 'Child', '$uibModal', function($scope, $timeout, Child, $uibModal) {
	$scope.motionChart = null;
	$scope.langChart = null;
	$scope.muscleChart = null;

	$scope.muscleChartStep = 5;
	$scope.currentMuscleRange = [0, 15];

	$scope.langChartStep = 5;
	$scope.currentLangRange = [0, 15];
	$scope.langState = LangState;

	$scope.showAllPos = function() {
		$('p.show-all').hide();
		$('#google-line-chart').height('340px');
		$('.dashboard-lang-frame').height('420px');
		$('div.required').addClass('narrow');
		$('div.additional').show();
	}

	$scope.showMeanPos = function() {
		$('.pos-mean').show();
		$('.show-mean').hide();
		$scope.langState.showMean = true;
		$scope.refreshLangChart();
	}

	$scope.refreshLangChart = function() {
		pos_list = {};
		for (pos in $scope.langState) {
			if ($scope.langState[pos].state) {
				pos_list[pos] = $scope.langState[pos].headline
				if ($scope.langState.showMean) {
					pos_list[pos + '_mean'] = $scope.langState[pos].headline + '(平均)';
				}
			}
		}
		if ($scope.langChart) {
			$scope.langChart.clearChart();
			$scope.langChart = null;
		}
		if (Object.keys(pos_list).length == 0) {
			$('.dashboard-lang-chart').hide();
		 } else {
			$('.dashboard-lang-chart').show();
			$scope.drawLangChart(pos_list);
		 }
	}

	$scope.openWordListModal = function(pos) {
		var child = new Child($('#internal-childid-token').text());
		child.words(null, [pos], function(data){
			$uibModal.open({
				templateUrl: 'word-list-modal.html',
				controller: 'WordModalController',
				resolve: {
					Pos: function() { return $scope.langState[pos].headline; },
					Words: function() { return data[pos]['words']; }
				}
			});
		});
	}

	$scope.forwardLangChart = function() {
		$scope.currentLangRange[0] += $scope.langChartStep;
		$scope.currentLangRange[1] += $scope.langChartStep;
		if ($scope.langChart) {
			$scope.langChart.clearChart();
			$scope.langChart = null;
		}
		$scope.refreshLangChart();
	}

	$scope.backwardLangChart = function() {
		var start = $scope.currentLangRange[0] - $scope.langChartStep;
		if (start < 0) {
			return;
		}
		$scope.currentLangRange[0] = start;
		$scope.currentLangRange[1] -= $scope.langChartStep;
		if ($scope.langChart) {
			$scope.langChart.clearChart();
			$scope.langChart = null;
		}
		$scope.refreshLangChart()
	}

	$scope.drawLangChart = function(pos_list) {
		var dataTable = new google.visualization.DataTable();
		dataTable.addColumn('number', '生後(ヶ月)');

		var pos_query = [];
		for (pos in pos_list) {
			dataTable.addColumn('number', pos_list[pos]);
			pos_query.push(pos);
		}
		
		var child = new Child($('#internal-childid-token').text());
		child.words($scope.currentLangRange, pos_query, function(data){
			var res_list = [];
			for (pos in pos_list) {
				res_list.push(data[pos]['monthly']);	
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
		
		var child = new Child($('#internal-childid-token').text());
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

	$scope.drawMuscleChart = function(muscleList) {
		var container = document.getElementById('google-muscle-chart');
		var dataTable = new google.visualization.DataTable();
		dataTable.addColumn('date', '生後(年月日)');
		dataTable.addColumn('number', '腕力');
		var child = new Child($('#internal-childid-token').text());
		child.muscle($scope.currentMuscleRange, muscleList, function(data){
			rows = [];
			var strengthData = data['strength'];
			var count = strengthData['count'];
			for (var i = 0; i < count; ++i) {
				var sampleData = strengthData['values'][i];
				rows.push([new Date(sampleData.years, sampleData.months, sampleData.days), sampleData.value]);
			}
			dataTable.addRows(rows)
			var options = {
				series: {
					0: {axis: 'N'}		
				},
				axes: {
					y: {
						N: {label: 'ニュートン'},
						all: {
							range: {
								min: 0	
							}
						},
					},
					x: {
						all: {
							range: {
							}
						}
					}
				},
			}
			$scope.muscleChart = new google.charts.Line(document.getElementById('google-muscle-chart'));
			$scope.muscleChart.draw(dataTable, options);
		});
	}

	function drawChart() {
		$scope.drawMotionChart(['neck_fix', 'rolling_over', 'sit', 'crawl', 'pullup', 'standup', 'walk']);
		$scope.refreshLangChart();
		$scope.drawMuscleChart(['strength']);
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



