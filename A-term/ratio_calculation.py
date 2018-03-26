def main():
    print("od_inter\tod_finger\tod_top\tod_drive\tdrive_gear\ttop_gear\tfinger_gear\tintermediate_gear\tratio")

    for od_intermediate_gear in range (24, 32, 1):
        for od_finger_gear in range (33, 40, 1):
            for od_top_gear in range (28, 32, 1):
                for od_drive_gear in range (27, 30, 1):
                    for intermediate_gear in range (10, 30, 1):
                        for finger_gear in range (10, 30, 1):
                            for top_gear in range (10, 30, 1):
                                for drive_gear in range (10, 30, 1):
                                    ratio = (drive_gear / top_gear) * (intermediate_gear / finger_gear)
                                    pd_intermediate_gear = (intermediate_gear + 2) / od_intermediate_gear
                                    pd_drive_gear = (drive_gear + 2) / od_drive_gear
                                    pd_top_gear = (top_gear + 2) / od_top_gear
                                    pd_finger_gear = (finger_gear + 2) / od_finger_gear

                                    if (pd_top_gear * 0.995) <= pd_drive_gear <= (pd_top_gear * 1.005) or (pd_drive_gear * 0.995) <= pd_top_gear <= (pd_drive_gear * 1.005):
                                            if (pd_finger_gear * 0.995) <= pd_intermediate_gear <= (pd_finger_gear * 1.005) or (pd_intermediate_gear * 0.995) <= pd_finger_gear <= (pd_intermediate_gear * 1.005):
                                                if ratio == 0.5:
                                                    print(str(od_intermediate_gear) + "\t\t\t" + str(od_finger_gear) + "\t\t\t" +
                                                          str(od_top_gear) + "\t\t" + str(od_drive_gear) + "\t\t\t" +
                                                          str(drive_gear) + "\t\t\t" + str(top_gear) + "\t\t\t" +
                                                          str(finger_gear) + "\t\t\t" +
                                                          str(intermediate_gear) + "\t\t\t\t\t" + str(ratio))

if __name__ == "__main__":
    main()