app.controller('SearchCtrl', function ($scope, SearchSvc, AppConst, CaruselSvc) {
	$scope.SearchSvc=SearchSvc;
	$scope.CaruselSvc=CaruselSvc;
	$scope.AppConst=AppConst;

	SearchSvc.init();
});