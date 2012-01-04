%global packname  msDilution
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.2
Release:          1%{?dist}
Summary:          Protein Mass Spectra Dataset from a Dilution Experiment

Group:            Applications/Engineering 
License:          GNU General Public License Version 2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
This package provides a dataset of 280 MALDI-TOF mass spectra generated
from a dilution experiment aimed at elucidating which features in
MALDI-TOF mass spectrometry data are informative for quantifying peptide

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
%doc %{rlibdir}/msDilution/DESCRIPTION
%doc %{rlibdir}/msDilution/doc
%doc %{rlibdir}/msDilution/html
%{rlibdir}/msDilution/NAMESPACE
%{rlibdir}/msDilution/INDEX
%{rlibdir}/msDilution/help
%{rlibdir}/msDilution/LICENSE
%{rlibdir}/msDilution/data
%{rlibdir}/msDilution/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.2-1
- initial package for Fedora