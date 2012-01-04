%global packname  DoseFinding
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.5.6
Release:          1%{?dist}
Summary:          Planning and Analyzing Dose Finding experiments

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.5-6.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-lattice R-mvtnorm 

BuildRequires:    R-devel tex(latex) R-lattice R-mvtnorm 

%description
The DoseFinding package provides functions for the design and analysis of
dose-finding experiments (for example pharmaceutical Phase II clinical
trials). It provides functions for: multiple contrast tests, fitting
non-linear dose-response models, calculating optimal designs and an
implementation of the MCPMod methodology.

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
%doc %{rlibdir}/DoseFinding/html
%doc %{rlibdir}/DoseFinding/DESCRIPTION
%{rlibdir}/DoseFinding/INDEX
%{rlibdir}/DoseFinding/Meta
%{rlibdir}/DoseFinding/help
%{rlibdir}/DoseFinding/data
%{rlibdir}/DoseFinding/libs
RPM build errors:
%{rlibdir}/DoseFinding/R
%{rlibdir}/DoseFinding/NAMESPACE

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.5.6-1
- initial package for Fedora