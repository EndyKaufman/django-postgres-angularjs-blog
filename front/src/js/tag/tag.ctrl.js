app.controller('TagCtrl', function ($scope, TagSvc, AppConst, CaruselSvc, AuthSvc) {
	$scope.TagSvc=TagSvc;
	$scope.CaruselSvc=CaruselSvc;
	$scope.AppConst=AppConst;
	$scope.AuthSvc=AuthSvc;

	TagSvc.init();
});