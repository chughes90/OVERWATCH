# Holds all of the server parameters

# Python 2/3 support
from __future__ import print_function

# General
import socket
import os
import logging

# Bcrypt
from flask_bcrypt import generate_password_hash

# Config
from .sharedParams import sharedParameters

class serverParameters(object):
    """ Contains the parameters used to configure the server.

    Draws a number of settings from :class:`~config.sharedParams.sharedParameters`.

    The stub must be copied, renamed, and filled out with the sensitive information. These sensitive
    attributes include ``_users`` and ``_secretKey``, which are not included in the HTML docs and must
    be viewed in the source file.

    Note: 
        The folder structure for flask can get complicated. See the variables below for their
        purposes. One can generally set staticFolder without staticURLPath, but not the reverse.
        For more information of flask folder structure,
        see (for example): https://stackoverflow.com/a/18746493

    """
    #: Sets the ip address.
    ipAddress = "127.0.0.1"

    #: Sets the port.
    port = 8850

    #: Setup Bcrypt.
    bcryptLogRounds = 12

    #: Default user name
    defaultUsername = ""

    _users = {"username": generate_password_hash("password", bcryptLogRounds)}
    """ Contains the users for authenticating on the server
    This could be more complex, but there isn't any point for such a simple project
    For more security in this file, one could also generate the hash and then just
    copy that here so that the password is not visible in plain text in this file.

    Defined with an underscore since it is a private value.
    
    Other usernames can be added here if desired. Users are defined as:
    
    >>> _users = {"username": generate_password_hash("password", bcryptLogRounds)}
    """

    _secretKey = ''
    """ Secret key for signing cookies

    Defined with an underscore since it is a private value.
    
    Generated using urandom(50), as suggested by the flask developers.
    """

    #: basePath is just a useful value.
    #: It defines a base directory to reference if the static, template, etc folders are
    #: all in the same dir.
    basePath = ""

    #: staticFolder is the disk location of the static folder.
    #: It is a flask defined variable.
    #: To check if the static files are from the front-end webserver, use:
    #: https://stackoverflow.com/questions/16595691/static-files-with-flask-in-production
    #:
    #: (ie. add + "CHANGE" to the staticFolder location specified here).
    staticFolder = os.path.join(basePath, sharedParameters.staticFolderName) 

    #: staticURLPath is the URL of the static folder.
    #: If you want to access "foo", it would be at $BASE_URL/staticURLPath/foo. "" is just the root.
    #: It is a flask defined variable.
    staticURLPath = "/static"

    #: protectedFolder is the disk location of the protected folder.
    #: This folder holds the experimental data.
    protectedFolder = os.path.join(basePath, sharedParameters.dataFolderName)

    #: templateFolder is the disk location of the template folder.
    templateFolder = os.path.join(basePath, sharedParameters.templateFolderName)

    #: The path to the database.
    databaseLocation = sharedParameters.databaseLocation

    #: The file extension to use when printing ROOT files.
    fileExtension = sharedParameters.fileExtension

    #: docsFolder is the disk location of the docs folder.
    docsFolder = "doc"

    #: docsBuildFolder is the disk location of the docs html folder.
    docsBuildFolder = os.path.join(docsFolder, "build/html")

    # Can set alternative values here if necessary, but it does not seem very likely that this will be needed.
    #if "pdsf" in socket.gethostname():
    #    staticURLPath = "/../site_media/aliemcalmonitor"

    #: Enable debugging information.
    debug = sharedParameters.debug

    #: List of subsystems.
    #: Each subsystem listed here will have an individual page for their respective histograms.
    subsystemList = sharedParameters.subsystemList

    #: Subsystems with ROOT files to show
    subsystemsWithRootFilesToShow = sharedParameters.subsystemsWithRootFilesToShow

    qaFunctionsList = sharedParameters.qaFunctionsList
    """ Define which functions are accessible from the QA page.

    See Also: 
        :attr:`config.sharedParams.sharedParameters.qaFunctionsList`
    """

    #: Subsystems which have templates available (determined on startup)
    availableRunPageTemplates = [name for name in os.listdir(templateFolder) if "runPage.html" in name]

logging.info("\nServer Parameters:")
logging.info("ipAddress: {0}".format(serverParameters.ipAddress))
logging.info("port: {0}".format(serverParameters.port))
logging.info("bcryptLogRounds: {0}".format(serverParameters.bcryptLogRounds))
logging.info("defaultUsername: {0}".format(serverParameters.defaultUsername))
logging.info("basePath: {0}".format(serverParameters.basePath))
logging.info("staticFolder: {0}".format(serverParameters.staticFolder))
logging.info("staticURLPath: {0}".format(serverParameters.staticURLPath))
logging.info("protectedFolder: {0}".format(serverParameters.protectedFolder))
logging.info("templateFolder: {0}".format(serverParameters.templateFolder))
logging.info("databaseLocation: {0}".format(serverParameters.databaseLocation))
logging.info("fileExtension: {0}".format(serverParameters.fileExtension))
logging.info("docsFolder: {0}".format(serverParameters.docsFolder))
logging.info("docsBuildFolder: {0}".format(serverParameters.docsBuildFolder))
logging.info("debug: {0}".format(serverParameters.debug))
logging.info("subsystemList: {0}".format(serverParameters.subsystemList))
logging.info("qaFunctionsList: {0}".format(serverParameters.qaFunctionsList))
logging.info("availableRunPageTemplates: {0}".format(serverParameters.availableRunPageTemplates))
