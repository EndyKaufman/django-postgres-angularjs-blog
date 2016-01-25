app.controller('SearchCtrl', function ($scope, SearchSvc, AppConst, CaruselSvc, AuthSvc) {
	$scope.SearchSvc=SearchSvc;
	$scope.CaruselSvc=CaruselSvc;
	$scope.AppConst=AppConst;
	$scope.AuthSvc=AuthSvc;

	SearchSvc.init();
});