%global packname  PopGenKit
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Useful functions for (batch) file conversion and data resampling in microsatellite datasets

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
There are two main purposes to this package. The first is to allow batch
conversion of Genepop (Rousset 2008) input files for use with Arlequin
(Excoffier and Lischer 2010), which has a simple GUI to analyze batch
files. Two commonly used simulation software, BottleSim (Kuo & Janzen
2003) and Easypop (Balloux 2001) produce Genepop output files that can be
analyzed this way. There are also functions to convert to and from
BottleSim format, to quickly produce allele frequency tables or to convert
a file directly for use in ordination analyses (e.g. principal component
analysis). This package also includes functions to calculate allele
rarefaction curves, confidence intervals on heterozygosity and allelic
richness with resampling strategies (bootstrap and jackknife).

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%doc %{rlibdir}/PopGenKit/html
%doc %{rlibdir}/PopGenKit/DESCRIPTION
%{rlibdir}/PopGenKit/Meta
%{rlibdir}/PopGenKit/NAMESPACE
%{rlibdir}/PopGenKit/help
%{rlibdir}/PopGenKit/INDEX
%{rlibdir}/PopGenKit/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora