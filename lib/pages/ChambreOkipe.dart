import 'package:flutter/material.dart';
class ChambreOccupe extends StatelessWidget {
  const ChambreOccupe({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text(
          "CHAMBRES OCCUPEES", ),
        backgroundColor: Colors.green,

        centerTitle: true,

      ),
      body: Center(
        child: ListView(
          children: [

          ],
        ),
      ),
    );
  }
}
