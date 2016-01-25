app.controller('NavbarCtrl', function ($scope, NavbarSvc) {
	$scope.NavbarSvc=NavbarSvc;

    NavbarSvc.init();
});