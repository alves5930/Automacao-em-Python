

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

-- =============================================
-- Banco de dados: db_produtos
-- =============================================

CREATE DATABASE IF NOT EXISTS `db_produtos` 
DEFAULT CHARACTER SET utf8mb4 
COLLATE utf8mb4_general_ci;

USE `db_produtos`;

-- =============================================
-- Tabela: tb_produtos
-- =============================================

DROP TABLE IF EXISTS `tb_produtos`;

CREATE TABLE `tb_produtos` (
  `id_produto` int(9) NOT NULL AUTO_INCREMENT,
  `descricao_produto` varchar(60) NOT NULL,
  `categoria` varchar(25) NOT NULL,
  `valor_compra` decimal(10,2) NOT NULL,
  `lucro_obtido` decimal(10,2) NOT NULL,
  `valor_venda` decimal(10,2) NOT NULL,
  PRIMARY KEY (`id_produto`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- =============================================
-- Finalizando
-- =============================================

COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;