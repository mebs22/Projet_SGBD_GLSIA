// ignore_for_file: prefer_const_constructors

import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:gestion_hotel/pages/ChambrePage.dart';
import 'package:gestion_hotel/pages/FacturePage.dart';
import 'dart:io';

import 'package:gestion_hotel/pages/ReservationPage.dart';
import 'package:gestion_hotel/pages/StatsPage.dart';
class Acceuil extends StatelessWidget {
  const Acceuil({
    super.key,
  });

  @override
  Widget build(BuildContext context) {
    return Container(
      decoration: BoxDecoration(
          gradient: LinearGradient(
              begin: Alignment.topRight,
              end: Alignment.bottomLeft,
              colors:[
                Colors.blue,
                Colors.blueAccent
              ]
          )
      ),
        child: Scaffold(

        appBar: AppBar(

          title: const Text(
            "ACCUEIL",),
          backgroundColor: Colors.green,
          centerTitle: true,
        ),

        body:
        Center(


            child: Column(
              children: [
                Padding(padding: EdgeInsets.all(20)),

                ElevatedButton.icon(
                  style: ButtonStyle(
                      fixedSize: MaterialStateProperty.all(Size(200, 50)),
                      backgroundColor: MaterialStatePropertyAll(Colors.green)
                  ),
                  onPressed: () {
                    Navigator.push(
                        context,
                        PageRouteBuilder(
                            pageBuilder: (_, __, ___) => const Chambre()
                        )
                    );
                  },
                  label: const Text("Lister les chambres"),
                  icon: Icon(Icons.list_alt),

                ),
                Padding(padding: EdgeInsets.all(25)),
                ElevatedButton.icon(
                  style: ButtonStyle(
                      fixedSize: MaterialStateProperty.all(Size(200, 50)),
                      backgroundColor: MaterialStatePropertyAll(Colors.green)
                  ),
                  onPressed: () {
                    Navigator.push(
                        context,
                        PageRouteBuilder(
                            pageBuilder: (_, __, ___) => const ReservationPage()
                        )
                    );
                  },
                  label: const Text("Gerer les reservations"),
                  icon: Icon(Icons.margin_outlined),

                ),
                Padding(padding: EdgeInsets.all(25)),
                ElevatedButton.icon(
                  style: ButtonStyle(
                    fixedSize: MaterialStateProperty.all(Size(200, 50)),
                    backgroundColor: MaterialStatePropertyAll(Colors.green),

                  ),
                  onPressed: () {
                    Navigator.push(
                        context,
                        PageRouteBuilder(
                            pageBuilder: (_, __, ___) => const Facture()
                        )
                    );
                  },
                  label: const Text("factures"),
                  icon: Icon(Icons.fact_check_sharp),

                ),
                Padding(padding: EdgeInsets.all(25)),
                ElevatedButton.icon(
                  style: ButtonStyle(
                      fixedSize: MaterialStateProperty.all(Size(200, 50)),
                      backgroundColor: MaterialStatePropertyAll(Colors.green)
                  ),
                  onPressed: () {
                    Navigator.push(
                        context,
                        PageRouteBuilder(
                            pageBuilder: (_, __, ___) => const Stats()
                        )
                    );
                  },
                  label: const Text("Statistiques"),
                  icon: Icon(Icons.query_stats_rounded),

                )
              ],
            )
        )
        )
    );
  }
}
