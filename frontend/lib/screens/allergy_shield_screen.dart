import 'package:flutter/material.dart';

class AllergyShieldScreen extends StatelessWidget {
  const AllergyShieldScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Alerji Kalkanı'),
      ),
      body: const Center(
        child: Text('Alerji Kalkanı Ekranı (OCR ve Analiz)'),
      ),
    );
  }
}
