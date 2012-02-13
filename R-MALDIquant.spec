%global packname  MALDIquant
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.5
Release:          1%{dist}
Summary:          Quantitative analysis of MALDI-TOF MS data

Group:            Applications/Engineering 
License:          GPL (>= 3)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods 

BuildRequires:    R-devel tex(latex) R-methods 

%description
Quantitative analysis of MALDI-TOF MS data This package provide an easy
framework for quantitative analysis of MALDI-TOF mass spectrometry data.
MALDIquant supports baseline correction, peak detection and plotting of
mass spectra.

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
%doc %{rlibdir}/MALDIquant/html
%doc %{rlibdir}/MALDIquant/DESCRIPTION
%doc %{rlibdir}/MALDIquant/NEWS
%{rlibdir}/MALDIquant/NAMESPACE
%{rlibdir}/MALDIquant/R
%{rlibdir}/MALDIquant/Meta
%{rlibdir}/MALDIquant/INDEX
%{rlibdir}/MALDIquant/data
%{rlibdir}/MALDIquant/help
%{rlibdir}/MALDIquant/libs

%changelog
* Sun Feb 12 2012 Pierre-Yves Chibon <pingou@pingoured.fr> 0.5-1
- Update to version 0.5

* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.4-1
- initial package for Fedora