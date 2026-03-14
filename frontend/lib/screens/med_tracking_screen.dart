import 'package:flutter/material.dart';

class MedTrackingScreen extends StatelessWidget {
  const MedTrackingScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('İlaç Takibi'),
      ),
      body: const Center(
        child: Text('İlaç Takibi Ekranı (Sync-Med)'),
      ),
    );
  }
}
