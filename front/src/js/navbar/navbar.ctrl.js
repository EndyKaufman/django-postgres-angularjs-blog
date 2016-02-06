app.controller('NavbarCtrl', function ($scope, NavbarSvc, SearchSvc) {
	$scope.NavbarSvc=NavbarSvc;
	$scope.SearchSvc=SearchSvc;

    NavbarSvc.init();
});