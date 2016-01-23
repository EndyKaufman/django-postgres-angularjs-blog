app.controller('SearchCtrl', function ($scope, $rootScope, SearchSvc, AppConst, CaruselSvc) {
	$scope.SearchSvc=SearchSvc;
	$scope.CaruselSvc=CaruselSvc;
	$scope.AppConst=AppConst;

	SearchSvc.init();
});