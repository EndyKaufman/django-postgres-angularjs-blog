app.config(function ($routeProvider, $locationProvider) {
    $routeProvider
      .when('/project/:projectName', {
        templateUrl: 'views/project/item.html',
        controller: 'ProjectCtrl'
      })
      .when('/project/update/:projectName', {
        templateUrl: 'views/project/update.html',
        controller: 'ProjectCtrl'
      })
      .when('/project', {
        templateUrl: 'views/project/list.html',
        controller: 'ProjectCtrl'
      });
});