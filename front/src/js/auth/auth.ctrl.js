app.controller('AuthCtrl', function ($scope, AuthSvc) {
    $scope.AuthSvc=AuthSvc;

	AuthSvc.init();
});