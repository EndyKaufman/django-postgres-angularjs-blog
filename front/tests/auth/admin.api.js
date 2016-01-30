describe('Auth API (admin):', function() {
  var helpers = require('./../helpers.js');

  var adminResponse = undefined, logoutResponse = undefined, profileResponse = undefined;

  beforeEach(function(done){
    browser.driver.manage().window().setSize(1280, 1024);
    browser.get(browser.baseUrl).then(function(){
        helpers.executeAndReturnJson(
            'callback(window.AppConfig);',
            function(data){

                helpers.postJson('/auth/login', {
                    email:'admin@email.com',
                    password:'admin@email.com'
                }, function(response){
                    adminResponse = response;

                    helpers.postJson('/auth/update', {
                        firstname:'New Name',
                        email:'admin@email.com'
                    }, function(response){
                        profileResponse = response;

                        helpers.postJson('/auth/logout', {
                        }, function(response){
                            logoutResponse = response;

                            done()

                        });

                    });

                });

            }
        );
    })
  });

  it('POST /auth/login as admin role & check structure', function() {
    expect(typeof adminResponse).toEqual('object');
    expect(adminResponse.data[0].userData).toBeDefined();
    expect(adminResponse.data[0].userId).toBeDefined();
    var userData = adminResponse.data[0].userData;
    var fields = ['id', 'username', 'email', 'firstname', 'lastname', 'roles'];
    for (var i=0; i<fields.length; i++)
        expect(userData[fields[i]]).toBeDefined();
    if (userData.roles.length>0)
        expect(userData.roles[0]).toEqual('admin');
  });

  it('POST /auth/update & check structure', function() {
    expect(typeof profileResponse).toEqual('object');
    expect(profileResponse.data[0].userData).toBeDefined();
    expect(profileResponse.data[0].userId).toBeDefined();
    var userData = profileResponse.data[0].userData;
    var fields = ['id', 'username', 'email', 'firstname', 'lastname', 'roles'];
    for (var i=0; i<fields.length; i++)
        expect(userData[fields[i]]).toBeDefined();
    if (userData.roles.length>0)
        expect(userData.roles[0]).toEqual('admin');

    expect(userData.firstname).toEqual('New Name');
  });

  it('POST /auth/logout & check structure', function() {
    expect(logoutResponse.code).toEqual('ok');
  });

});