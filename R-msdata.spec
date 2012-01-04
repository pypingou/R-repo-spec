%global packname  msdata
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1.7
Release:          1%{?dist}
Summary:          Various Mass Spectrometry raw data example files

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://bioconductor.org/packages/release/data/experiment/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/data/experiment/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Ion Trap positive ionization mode data in mzData file format. Subset from
500-850 m/z and 1190-1310 seconds, incl. MS2 and MS3, intensity threshold
100.000. Extracts from FTICR Apex III, m/z 400-450. Subset of UPLC -
Bruker micrOTOFq data, both mzData and mzML.

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
%doc %{rlibdir}/msdata/DESCRIPTION
%doc %{rlibdir}/msdata/html
%{rlibdir}/msdata/R
%{rlibdir}/msdata/help
%{rlibdir}/msdata/INDEX
%{rlibdir}/msdata/data
%{rlibdir}/msdata/microtofq
%{rlibdir}/msdata/fticr
%{rlibdir}/msdata/threonine
%{rlibdir}/msdata/NAMESPACE
%{rlibdir}/msdata/Meta
%{rlibdir}/msdata/iontrap

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.7-1
- initial package for Fedora