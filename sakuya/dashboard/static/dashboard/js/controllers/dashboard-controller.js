app = angular.module('DashboardApp');


app.controller('DashboardController', ['$scope', '$timeout', 'Child', function($scope, $timeout, Child) {
	$scope.motionChart = null;
	$scope.langChart = null;

	$scope.showAll = function() {
		$('p.show-all').hide();
		$('#google-line-chart').height('340px');
		$('.dashboard-lang-frame').height('400px');
		$('p.required').addClass('narrow');
		$('p.additional').show();
		$scope.langChart.clearChart();
		$scope.drawLangChart(
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
		);
	}

	$scope.drawLangChart = function(pos_list) {
		var dataTable = new google.visualization.DataTable();
		dataTable.addColumn('number', '生後');
		for (key in pos_list) {
			dataTable.addColumn('number', pos_list[key]);
		}
		
		var child = new Child($('#dashboard-internal-token').text());
		child.words(function(data){
			var res_list = [];
			for (key in pos_list) {
				res_list.push(data[key]['monthly']);	
			}
			rows = [];
			for (var i = 0; i < 16; ++i) {
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
				}
			}

			$scope.langChart = new google.charts.Line(document.getElementById('google-line-chart'));
			$scope.langChart.draw(dataTable, options);
		});	
	}

	function drawChart() {
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
		var options = {
			timeline: { showRowLabels: false },
			backgroundColor: '#ffffff',
			colors: [
				'#d3d3d3',
				'#d3d3d3',
				'#d3d3d3',
				'#00bfff',
				'#d3d3d3',
				'#d3d3d3',
				'#d3d3d3',
			]
		}
		$scope.motionChart = new google.visualization.Timeline(container);
		$scope.motionChart.draw(dataTable, options);

		$scope.drawLangChart(
			{
				'n': '名詞',
				'v': '動詞',
				'adj': '形容詞',
				'adv': '副詞',
				'im': '感動詞'
			}				
		);
	}
	google.load("visualization", "1", {packages: ["timeline", "line"], callback: drawChart});
}]);
/*
		var dataTable = new google.visualization.DataTable();
		dataTable.addColumn('number', '生後');
		dataTable.addColumn('number', '名詞');
		dataTable.addColumn('number', '動詞');
		dataTable.addColumn('number', '形容詞');
		dataTable.addColumn('number', '副詞');
		dataTable.addColumn('number', '感動詞');
		dataTable.addColumn('number', '助詞');
		dataTable.addColumn('number', '接続詞');
		dataTable.addColumn('number', '助動詞');
		dataTable.addColumn('number', '接頭詞');
		dataTable.addColumn('number', '連体詞');
		dataTable.addColumn('number', '未知語');
		
		var child = new Child($('#dashboard-internal-token').text());
		child.words(function(data){
			n = data['n']['monthly'];
			v = data['v']['monthly'];
			adj = data['adj']['monthly'];
			adv = data['adv']['monthly'];
			im = data['im']['monthly'];
		   	j = data['j']['monthly'];
			conj = data['conj']['monthly'];
			auv	= data['auv']['monthly'];
		   	p = data['p']['monthly'];
			t = data['t']['monthly'];
			unk = data['unk']['monthly'];

			rows = [];
			for (var i = 0; i < 16; ++i) {
					rows.push([
						i, 
						n[i]['count'],
						v[i]['count'],
						adj[i]['count'],
						adv[i]['count'],
						im[i]['count'],
						j[i]['count'],
						conj[i]['count'],
						auv[i]['count'],
						p[i]['count'],
						t[i]['count'],
						unk[i]['count']]);
			}
			dataTable.addRows(rows)
			$scope.langChart = new google.charts.Line(document.getElementById('google-line-chart'))
*/
