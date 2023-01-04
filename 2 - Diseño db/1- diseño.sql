-- --------------------------------------------------------
-- Host:                         C:\Users\k3\Desktop\Carrito\integrador.db
-- Versión del servidor:         3.39.0
-- SO del servidor:              
-- HeidiSQL Versión:             12.1.0.6537
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES  */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Volcando estructura de base de datos para integrador
CREATE DATABASE IF NOT EXISTS "integrador";
;

-- Volcando estructura para tabla integrador.carrera
CREATE TABLE IF NOT EXISTS "carrera" (
    "Id" INTEGER NOT NULL CONSTRAINT "PK_carrera" PRIMARY KEY AUTOINCREMENT,
    "instituto_id" INTEGER NOT NULL,
    "codigo" TEXT NULL,
    "nombre" TEXT NULL,
    "resolucion" TEXT NULL,
    "duracion" TEXT NULL,
    "activo" INTEGER NOT NULL,
    CONSTRAINT "FK_carrera_instituto_instituto_id" FOREIGN KEY ("instituto_id") REFERENCES "instituto" ("Id") ON UPDATE CASCADE ON DELETE RESTRICT
);

-- Volcando datos para la tabla integrador.carrera: 0 rows
/*!40000 ALTER TABLE "carrera" DISABLE KEYS */;
/*!40000 ALTER TABLE "carrera" ENABLE KEYS */;

-- Volcando estructura para tabla integrador.cursada
CREATE TABLE IF NOT EXISTS "cursada" (
    "Id" INTEGER NOT NULL CONSTRAINT "PK_cursada" PRIMARY KEY AUTOINCREMENT,
    "estudiante_id" INTEGER NOT NULL,
    "carrera_id" INTEGER NOT NULL,
    "fecha_inscripcion" TEXT NULL,
    "actual" INTEGER NOT NULL,
    "finalizada" INTEGER NOT NULL,
    CONSTRAINT "FK_cursada_carrera_carrera_id" FOREIGN KEY ("carrera_id") REFERENCES "carrera" ("Id") ON UPDATE CASCADE ON DELETE RESTRICT,
    CONSTRAINT "FK_cursada_estudiante_estudiante_id" FOREIGN KEY ("estudiante_id") REFERENCES "estudiante" ("Id") ON UPDATE CASCADE ON DELETE RESTRICT
);

-- Volcando datos para la tabla integrador.cursada: 0 rows
/*!40000 ALTER TABLE "cursada" DISABLE KEYS */;
/*!40000 ALTER TABLE "cursada" ENABLE KEYS */;

-- Volcando estructura para tabla integrador.estudiante
CREATE TABLE IF NOT EXISTS "estudiante" (
    "Id" INTEGER NOT NULL CONSTRAINT "PK_estudiante" PRIMARY KEY AUTOINCREMENT,
    "apellido" TEXT NULL,
    "nombre" TEXT NULL,
    "dni" TEXT NULL,
    "fecha_nacimiento" TEXT NULL,
    "foto_dni" TEXT NULL,
    "foto_secundario" TEXT NULL,
    "telefono" TEXT NULL,
    "email" TEXT NULL
);

-- Volcando datos para la tabla integrador.estudiante: 0 rows
/*!40000 ALTER TABLE "estudiante" DISABLE KEYS */;
/*!40000 ALTER TABLE "estudiante" ENABLE KEYS */;

-- Volcando estructura para tabla integrador.instituto
CREATE TABLE IF NOT EXISTS "instituto" (
    "Id" INTEGER NOT NULL CONSTRAINT "PK_instituto" PRIMARY KEY AUTOINCREMENT,
    "nombre" TEXT NULL,
    "cue" TEXT NULL,
    "direccion" TEXT NULL,
    "telefono" TEXT NULL,
    "web" TEXT NULL
);

-- Volcando datos para la tabla integrador.instituto: 0 rows
/*!40000 ALTER TABLE "instituto" DISABLE KEYS */;
/*!40000 ALTER TABLE "instituto" ENABLE KEYS */;

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
