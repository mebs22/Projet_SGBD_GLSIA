// ignore_for_file: prefer_const_constructors

import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:gestion_hotel/pages/Accueil.dart';
import 'package:gestion_hotel/pages/Authentification.dart';
import 'package:gestion_hotel/pages/ChambrePage.dart';
import 'package:gestion_hotel/pages/FacturePage.dart';
import 'dart:io';

import 'package:gestion_hotel/pages/ReservationPage.dart';
import 'package:gestion_hotel/pages/StatsPage.dart';
void main()
{
  String s="click";
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Connexion(),
    );
  }
}


