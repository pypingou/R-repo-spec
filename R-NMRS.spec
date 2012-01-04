%global packname  NMRS
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          NMR Spectroscopy

Group:            Applications/Engineering 
License:          GPL version 2 or newer
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-Rwave R-FTICRMS R-tcltk R-tkrplot 

BuildRequires:    R-devel tex(latex) R-Rwave R-FTICRMS R-tcltk R-tkrplot 

%description
NMRS has been developed to load directly the spectra in the Bruker
spectroscopy format. This application displays the spectrum reference and
manages basic operations such as setting the chemical shift of a certain
compound (TSP or DSS) to 0 ppm,zero order and first order phase
corrections, baseline adjustment and spectral area selection

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
%doc %{rlibdir}/NMRS/DESCRIPTION
%doc %{rlibdir}/NMRS/html
%{rlibdir}/NMRS/help
%{rlibdir}/NMRS/Meta
%{rlibdir}/NMRS/R
%{rlibdir}/NMRS/INDEX

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora