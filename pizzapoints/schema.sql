--
--  users
--

DROP TABLE IF EXISTS users;

CREATE TABLE `users` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `hashedPassword` varchar(256) DEFAULT NULL,
  `screenName` varchar(128) NOT NULL,
  `firstName` varchar(128) NOT NULL,
  `lastName` varchar(128) NOT NULL,
  `email` varchar(128) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


--
--  groups
--

DROP TABLE IF EXISTS `groups`;

CREATE TABLE `groups` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `name` varchar(128) NOT NULL,
  `desc` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
--  relUsersGroups
--

DROP TABLE IF EXISTS `relUsersGroups`;

CREATE TABLE `relUsersGroups` (
  `user` int(10) NOT NULL,
  `group` int(10) NOT NULL,
  FOREIGN KEY (`user`) REFERENCES `users`(`id`),
  FOREIGN KEY (`group`) REFERENCES `groups`(`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;