app.controller('AccountCtrl', function ($scope, AccountSvc) {
    $scope.AccountSvc=AccountSvc;

	AccountSvc.init();
});