app.controller('AuthCtrl', function ($scope, AuthSvc, AppConst, MessageSvc) {
	$scope.AuthSvc=AuthSvc;

	AuthSvc.init();
});