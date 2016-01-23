app.factory('ProjectRes', function ($http, AppConst) {
    var service={};

    service.getItem=function(name){
        return $http({
                  method: 'GET',
                  url: AppConst.project.urls.getData+'/item/'+name
               });
    };
    service.getList=function(){
        return $http({
                  method: 'GET',
                  url: AppConst.project.urls.getData+'/list'
               });
    };
    service.getSearch=function(searchText){
        return $http({
                  method: 'GET',
                  url: AppConst.project.urls.getData+'/search/'+searchText
               });
    };
    service.getListByTag=function(tagText){
        return $http({
                  method: 'GET',
                  url: AppConst.project.urls.getData+'/listbytag/'+tagText
               });
    };
    service.actionUpdate=function(item){
        var item=angular.copy(item);
        item['csrfmiddlewaretoken']=AppConfig.csrf_token;
        return $http.post(AppConst.project.urls.action+'/update/'+item.id, item);
    }
    service.actionCreate=function(item){
        var item=angular.copy(item);
        item['csrfmiddlewaretoken']=AppConfig.csrf_token;
        return $http.post(AppConst.project.urls.action+'/create', item);
    }
    service.actionDelete=function(item){
        var item=angular.copy(item);
        item['csrfmiddlewaretoken']=AppConfig.csrf_token;
        return $http.post(AppConst.project.urls.action+'/delete/'+item.id, item);
    }

    return service;
  });