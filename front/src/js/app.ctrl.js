app.controller('AppCtrl', function ($scope, AppSvc, AppConst, UtilsSvc, AuthSvc) {
    $scope.AppConfig=AppConfig;

    $scope.UtilsSvc=UtilsSvc;
    $scope.AppConst=AppConst;
	$scope.AppSvc=AppSvc;
});