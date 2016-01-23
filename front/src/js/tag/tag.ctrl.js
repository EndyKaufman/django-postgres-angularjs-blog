app.controller('TagCtrl', function ($scope, $rootScope, TagSvc, AppConst, CaruselSvc) {
	$scope.TagSvc=TagSvc;
	$scope.CaruselSvc=CaruselSvc;
	$scope.AppConst=AppConst;

	TagSvc.init();
});