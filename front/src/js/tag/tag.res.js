app.factory('TagRes', function ($http, AppConst) {
    var service={};

    service.getList=function(){
        return $http({
                  method: 'GET',
                  url: '/tag/list'
               });
    };

    return service;
  });