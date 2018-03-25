//
//  ViewController.swift
//  The Knot Classifier
//
//  Created by Joseph Cameron on 23/01/2018.
//  Copyright © 2018 Joseph Cameron. All rights reserved.
//

import UIKit
import AVKit
import Vision

class ViewController: UIViewController, AVCaptureVideoDataOutputSampleBufferDelegate {
    
    @IBOutlet weak var predictionOutput: UILabel!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // Start up the camera here
        
        let captureSession = AVCaptureSession()
        captureSession.sessionPreset = .photo // Collapses the camera's view on the screen.
        guard let captureDevice = AVCaptureDevice.default(for: .video) else { return }
        guard let captureInput = try? AVCaptureDeviceInput(device: captureDevice) else { return }
        captureSession.addInput(captureInput)
        captureSession.startRunning()
        let previewLayer = AVCaptureVideoPreviewLayer(session: captureSession)
        view.layer.addSublayer(previewLayer)
        previewLayer.frame = view.frame
        
        //----------------------------------------------------------------------------------
        
        // Now, we analyse the images
        
        let dataOutput = AVCaptureVideoDataOutput()
        dataOutput.setSampleBufferDelegate(self, queue: DispatchQueue(label: "videoQueue"))
        captureSession.addOutput(dataOutput)
        
    }
    
    func captureOutput(_ output: AVCaptureOutput, didOutput sampleBuffer: CMSampleBuffer, from connection: AVCaptureConnection) {
        
        guard let pixelBuffer: CVPixelBuffer = CMSampleBufferGetImageBuffer(sampleBuffer) else { return }
        
        // Specify knotClassifier.mlmodel as the model
        guard let model = try? VNCoreMLModel(for: knotClassifier().model) else { return }
        
        // Create request for CoreML
        let request = VNCoreMLRequest(model: model) { (finishedReq, err) in
            
            // Get classification results from knotClassifier.mlmodel
            guard let results = finishedReq.results as? [VNClassificationObservation] else { return }
            
            // Get the top-3 VNClassificationObservations
            let top3 = results.prefix(through: 2).map { classification in return String(format: " %@ (%.2f)", classification.identifier, classification.confidence) }
            
            // Does not update the label without a dispatch to the main thread.
            DispatchQueue.main.async {
                // Display each classification and probability on its own line, in order of probability
                self.predictionOutput.text = top3.joined(separator: "\n")
            }
            
        }
        
        try? VNImageRequestHandler(cvPixelBuffer: pixelBuffer, options: [:]).perform([request])
        
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }


}

