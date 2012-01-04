%global packname  pkDACLASS
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          A complete statistical analysis of MALDI-TOF Mass Spectrometry Proteomics data

Group:            Applications/Engineering 
License:          LGPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-PROcess R-plyr R-ROCR R-randomForest R-caMassClass 


BuildRequires:    R-devel tex(latex) R-PROcess R-plyr R-ROCR R-randomForest R-caMassClass



%description
The package pkDACLASS provides unique monoisotopic peaks of peptides. It
will align the detected monoisotopic peaks from multiple samples and
classify the samples with these peaks and report the classification

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
%changelog
* Mon Dec 12 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora