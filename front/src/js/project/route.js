app.config(function ($routeProvider, $locationProvider) {
    $routeProvider
      .when('/project/update/:projectName', {
        templateUrl: 'views/project/update.html',
        controller: 'ProjectCtrl',
        update: true
      })
      .when('/project/create', {
        templateUrl: 'views/project/create.html',
        controller: 'ProjectCtrl',
        create: true
      })
      .when('/project/:projectName', {
        templateUrl: 'views/project/item.html',
        controller: 'ProjectCtrl',
        item: true
      })
      .when('/project', {
        templateUrl: 'views/project/list.html',
        controller: 'ProjectCtrl',
        list: true
      });
});