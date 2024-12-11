
import sys,array,ROOT,math,os,copy
import argparse

ROOT.gROOT.SetBatch(True)
ROOT.gStyle.SetOptStat(0)
ROOT.gStyle.SetOptTitle(0)


def get_hist(proc, hName, norm=False, lumi=150e6):
    fIn = ROOT.TFile(f"output/{proc}.root")
    hist = fIn.Get(hName)
    hist.SetDirectory(0)
    xsec = fIn.Get("crossSection").GetVal()
    nevents = fIn.Get("eventsProcessed").GetVal()
    if norm:
        hist.Scale(lumi*xsec/nevents)
    return hist, xsec, nevents

def yields():
    procs = ["wzp6_ee_mumu_ecm91p2", "wzp6_ee_tautau_ecm91p2", "p8_ee_gaga_mumu_ecm91p2"]
    luminosity = 44.84 # LEP=44.84, FCC=100e6

    print(f"Integrated luminosity used: {luminosity} pb-1\n")
    for proc in procs:
        hist, xsec, nevents = get_hist(proc, "cutFlow")
        hist_scaled, xsec, nevents = get_hist(proc, "cutFlow", norm=True, lumi=luminosity)
        yields = hist.GetBinContent(5)
        yields_scaled = hist_scaled.GetBinContent(5)
        print(f"Process {proc} xsec={xsec:.2f} pb, nevents={nevents}")
        print(f"   Bare yields: {yields:.2f}")
        print(f"   Normalized yields: {yields_scaled:.2f}")


def acceptance():
    proc = "wzp6_ee_mumu_ecm91p2"
    hist, xsec, nevents = get_hist(proc, "cutFlow")
    n_tot = hist.GetBinContent(1)
    n_sel = hist.GetBinContent(5)
    acc = n_sel / n_tot
    print(f"Acceptance for {proc} = {acc:.03f}")





if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--yields", action="store_true", help="Calculate event yields")
    parser.add_argument("--acceptance", action="store_true", help="Calculate acceptance")
    args = parser.parse_args()

    if args.yields:
        yields()
    elif args.acceptance:
        acceptance()