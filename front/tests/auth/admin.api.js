describe('Auth API (admin):', function() {
  var mytools = require('./../tools.js');

  var adminData = undefined, logoutData = undefined;

  beforeEach(function(done){
    browser.get(browser.baseUrl).then(function(){
        mytools.executeAndReturnJson(
            'callback(window.AppConfig);',
            function(data){

                mytools.postJson('/auth/login', {
                    email:'admin@email.com',
                    password:'admin@email.com'
                }, function(response){
                    adminData = response.data;

                    mytools.postJson('/auth/logout', {
                    }, function(response){
                        logoutData = response;

                        done()

                    });

                });

            }
        );
    })
  });

  it('try post /auth/login as admin role and check structure', function() {
    expect(typeof adminData).toEqual('object');
    expect(typeof adminData.userData).toEqual('object');
    expect(typeof adminData.userId).toEqual('number');
    var data = adminData.userData;
    var fields = ['userName', 'userEmail', 'firstName', 'lastName', 'roles'];
    for (var i=0; i<fields.length; i++)
        expect(data[fields[0]] != undefined ? true : false).toEqual(true);
    if (data.roles.length>0)
        expect(data.roles[0]).toEqual('admin');
  });

  it('try post /auth/logout and check structure', function() {
    expect(logoutData.code).toEqual('ok');
  });

});