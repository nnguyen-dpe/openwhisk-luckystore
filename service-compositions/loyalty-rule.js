const composer = require('@ibm-functions/composer')

module.exports = composer.if(
    composer.action('/guest/loyalty-service'),
    composer.action('/guest/notification-service'),
    composer.action('/whisk.system/utils/echo')
)